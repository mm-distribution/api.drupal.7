# DatabaseStatement_sqlite::execute()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 494–549 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L494-L549)
- **Class:** [DatabaseStatement_sqlite](../DatabaseStatement_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function execute($args = array(), $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute($args = array(), $options = array()) {
    try {
      $return = parent::execute($args, $options);
    }
    catch (PDOException $e) {
      if (!empty($e->errorInfo[1]) && $e->errorInfo[1] === 17) {
        // The schema has changed. SQLite specifies that we must resend the query.
        $return = parent::execute($args, $options);
      }
      else {
        // Rethrow the exception.
        throw $e;
      }
    }

    // In some weird cases, SQLite will prefix some column names by the name
    // of the table. We post-process the data, by renaming the column names
    // using the same convention as MySQL and PostgreSQL.
    $rename_columns = array();
    foreach ($this->columnNames as $k => $column) {
      // In some SQLite versions, SELECT DISTINCT(field) will return "(field)"
      // instead of "field".
      if (preg_match("/^\((.*)\)$/", $column, $matches)) {
        $rename_columns[$column] = $matches[1];
        $this->columnNames[$k] = $matches[1];
        $column = $matches[1];
      }

      // Remove "table." prefixes.
      if (preg_match("/^.*\.(.*)$/", $column, $matches)) {
        $rename_columns[$column] = $matches[1];
        $this->columnNames[$k] = $matches[1];
      }
    }
    if ($rename_columns) {
      // DatabaseStatementPrefetch already extracted the first row,
      // put it back into the result set.
      if (isset($this->currentRow)) {
        $this->data[0] = &$this->currentRow;
      }

      // Then rename all the columns across the result set.
      foreach ($this->data as $k => $row) {
        foreach ($rename_columns as $old_column => $new_column) {
          $this->data[$k][$new_column] = $this->data[$k][$old_column];
          unset($this->data[$k][$old_column]);
        }
      }

      // Finally, extract the first row again.
      $this->currentRow = $this->data[0];
      unset($this->data[0]);
    }

    return $return;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
