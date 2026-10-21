# DatabaseTasks_pgsql::checkBinaryOutput()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 87–126 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L87-L126)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
function checkBinaryOutput()
```

## Documentation

```text
Check Binary Output.

Unserializing does not work on Postgresql 9 when bytea_output is 'hex'.
```

## Code

```php
  function checkBinaryOutput() {
    // PostgreSQL < 9 doesn't support bytea_output, so verify we are running
    // at least PostgreSQL 9.
    $database_connection = Database::getConnection();
    if (version_compare($database_connection->version(), '9') >= 0) {
      if (!$this->checkBinaryOutputSuccess()) {
        // First try to alter the database. If it fails, raise an error telling
        // the user to do it themselves.
        $connection_options = $database_connection->getConnectionOptions();
        // It is safe to include the database name directly here, because this
        // code is only called when a connection to the database is already
        // established, thus the database name is guaranteed to be a correct
        // value.
        $query = "ALTER DATABASE \"" . $connection_options['database'] . "\" SET bytea_output = 'escape';";
        try {
          db_query($query);
        }
        catch (Exception $e) {
          // Ignore possible errors when the user doesn't have the necessary
          // privileges to ALTER the database.
        }

        // Close the database connection so that the configuration parameter
        // is applied to the current connection.
        db_close();

        // Recheck, if it fails, finally just rely on the end user to do the
        // right thing.
        if (!$this->checkBinaryOutputSuccess()) {
          $replacements = array(
            '%setting' => 'bytea_output',
            '%current_value' => 'hex',
            '%needed_value' => 'escape',
            '!query' => "<code>" . $query . "</code>",
          );
          $this->fail(st("The %setting setting is currently set to '%current_value', but needs to be '%needed_value'. Change this by running the following query: !query", $replacements));
        }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
