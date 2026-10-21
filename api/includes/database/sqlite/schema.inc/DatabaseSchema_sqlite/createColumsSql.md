# DatabaseSchema_sqlite::createColumsSql()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 71–90 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L71-L90)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function createColumsSql($tablename, $schema)
```

## Documentation

```text
Build the SQL expression for creating columns.
```

## Code

```php
  protected function createColumsSql($tablename, $schema) {
    $sql_array = array();

    // Add the SQL statement for each field.
    foreach ($schema['fields'] as $name => $field) {
      if (isset($field['type']) && $field['type'] == 'serial') {
        if (isset($schema['primary key']) && ($key = array_search($name, $schema['primary key'])) !== FALSE) {
          unset($schema['primary key'][$key]);
        }
      }
      $sql_array[] = $this->createFieldSql($name, $this->processField($field));
    }

    // Process keys.
    if (!empty($schema['primary key'])) {
      $sql_array[] = " PRIMARY KEY (" . $this->createKeySql($schema['primary key']) . ")";
    }

    return implode(", \n", $sql_array);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
