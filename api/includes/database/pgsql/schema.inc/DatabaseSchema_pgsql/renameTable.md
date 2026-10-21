# DatabaseSchema_pgsql::renameTable()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 479–526 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L479-L526)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
function renameTable($table, $new_name)
```

## Documentation

_No docblock in source._

## Code

```php
  function renameTable($table, $new_name) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot rename @table to @table_new: table @table doesn't exist.", array('@table' => $table, '@table_new' => $new_name)));
    }
    if ($this->tableExists($new_name)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot rename @table to @table_new: table @table_new already exists.", array('@table' => $table, '@table_new' => $new_name)));
    }

    // Get the schema and tablename for the old table.
    $old_full_name = $this->connection->prefixTables('{' . $table . '}');
    list($old_schema, $old_table_name) = strpos($old_full_name, '.') ? explode('.', $old_full_name) : array('public', $old_full_name);

    // Index names and constraint names are global in PostgreSQL, so we need to
    // rename them when renaming the table.
    $indexes = $this->connection->query('SELECT indexname FROM pg_indexes WHERE schemaname = :schema AND tablename = :table', array(':schema' => $old_schema, ':table' => $old_table_name));
    foreach ($indexes as $index) {
      // Get the index type by suffix, e.g. idx/key/pkey
      $index_type = substr($index->indexname, strrpos($index->indexname, '_') + 1);

      // If the index is already rewritten by ensureIdentifiersLength() to not
      // exceed the 63 chars limit of PostgreSQL, we need to take care of that.
      // Example (drupal_Gk7Su_T1jcBHVuvSPeP22_I3Ni4GrVEgTYlIYnBJkro_idx).
      if (strpos($index->indexname, 'drupal_') !== FALSE) {
        preg_match('/^drupal_(.*)_' . preg_quote($index_type) . '/', $index->indexname, $matches);
        $index_name = $matches[1];
      }
      else {
        if ($index_type == 'pkey') {
          // Primary keys do not have a specific name in D7.
          $index_name = '';
        }
        else {
          // Make sure to remove the suffix from index names, because
          // ensureIdentifiersLength() will add the suffix again and thus
          // would result in a wrong index name.
          preg_match('/^' . preg_quote($old_full_name) . '_(.*)_' . preg_quote($index_type) . '/', $index->indexname, $matches);
          $index_name = $matches[1];
        }
      }

      $this->connection->query('ALTER INDEX ' . $index->indexname . ' RENAME TO ' . $this->ensureIdentifiersLength($new_name, $index_name, $index_type));
    }

    // Now rename the table.
    // Ensure the new table name does not include schema syntax.
    $prefixInfo = $this->getPrefixInfo($new_name);
    $this->connection->query('ALTER TABLE {' . $table . '} RENAME TO ' . $prefixInfo['table']);
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
