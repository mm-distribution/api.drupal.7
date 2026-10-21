# DatabaseSchema_sqlite::alterTable()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 354–395 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L354-L395)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function alterTable($table, $old_schema, $new_schema, array $mapping = array())
```

## Documentation

```text
Create a table with a new schema containing the old content.

As SQLite does not support ALTER TABLE (with a few exceptions) it is
necessary to create a new table and copy over the old content.

@param $table
  Name of the table to be altered.
@param $old_schema
  The old schema array for the table.
@param $new_schema
  The new schema array for the table.
@param $mapping
  An optional mapping between the fields of the old specification and the
  fields of the new specification. An associative array, whose keys are
  the fields of the new table, and values can take two possible forms:
    - a simple string, which is interpreted as the name of a field of the
      old table,
    - an associative array with two keys 'expression' and 'arguments',
      that will be used as an expression field.
```

## Code

```php
  protected function alterTable($table, $old_schema, $new_schema, array $mapping = array()) {
    $i = 0;
    do {
      $new_table = $table . '_' . $i++;
    } while ($this->tableExists($new_table));

    $this->createTable($new_table, $new_schema);

    // Build a SQL query to migrate the data from the old table to the new.
    $select = $this->connection->select($table);

    // Complete the mapping.
    $possible_keys = array_keys($new_schema['fields']);
    $mapping += array_combine($possible_keys, $possible_keys);

    // Now add the fields.
    foreach ($mapping as $field_alias => $field_source) {
      // Just ignore this field (ie. use it's default value).
      if (!isset($field_source)) {
        continue;
      }

      if (is_array($field_source)) {
        $select->addExpression($field_source['expression'], $field_alias, $field_source['arguments']);
      }
      else {
        $select->addField($table, $field_source, $field_alias);
      }
    }

    // Execute the data migration query.
    $this->connection->insert($new_table)
      ->from($select)
      ->execute();

    $old_count = $this->connection->query('SELECT COUNT(*) FROM {' . $table . '}')->fetchField();
    $new_count = $this->connection->query('SELECT COUNT(*) FROM {' . $new_table . '}')->fetchField();
    if ($old_count == $new_count) {
      $this->dropTable($table);
      $this->renameTable($new_table, $table);
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
