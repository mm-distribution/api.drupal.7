# DatabaseSchema_sqlite::introspectSchema()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 410–469 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L410-L469)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function introspectSchema($table)
```

## Documentation

```text
Find out the schema of a table.

This function uses introspection methods provided by the database to
create a schema array. This is useful, for example, during update when
the old schema is not available.

@param $table
  Name of the table.
@return
  An array representing the schema, from drupal_get_schema().
@see drupal_get_schema()
```

## Code

```php
  protected function introspectSchema($table) {
    $mapped_fields = array_flip($this->getFieldTypeMap());
    $schema = array(
      'fields' => array(),
      'primary key' => array(),
      'unique keys' => array(),
      'indexes' => array(),
    );

    $info = $this->getPrefixInfo($table);
    $result = $this->connection->query('PRAGMA ' . $info['schema'] . '.table_info(' . $info['table'] . ')');
    foreach ($result as $row) {
      if (preg_match('/^([^(]+)\((.*)\)$/', $row->type, $matches)) {
        $type = $matches[1];
        $length = $matches[2];
      }
      else {
        $type = $row->type;
        $length = NULL;
      }
      if (isset($mapped_fields[$type])) {
        list($type, $size) = explode(':', $mapped_fields[$type]);
        $schema['fields'][$row->name] = array(
          'type' => $type,
          'size' => $size,
          'not null' => !empty($row->notnull),
          'default' => trim((string) $row->dflt_value, "'"),
        );
        if ($length) {
          $schema['fields'][$row->name]['length'] = $length;
        }
        if ($row->pk) {
          $schema['primary key'][] = $row->name;
        }
      }
      else {
        new Exception("Unable to parse the column type " . $row->type);
      }
    }
    $indexes = array();
    $result = $this->connection->query('PRAGMA ' . $info['schema'] . '.index_list(' . $info['table'] . ')');
    foreach ($result as $row) {
      if (strpos($row->name, 'sqlite_autoindex_') !== 0) {
        $indexes[] = array(
          'schema_key' => $row->unique ? 'unique keys' : 'indexes',
          'name' => $row->name,
        );
      }
    }
    foreach ($indexes as $index) {
      $name = $index['name'];
      // Get index name without prefix.
      $index_name = substr($name, strlen($info['table']) + 1);
      $result = $this->connection->query('PRAGMA ' . $info['schema'] . '.index_info(' . $name . ')');
      foreach ($result as $row) {
        $schema[$index['schema_key']][$index_name][] = $row->name;
      }
    }
    return $schema;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
