# DatabaseSchema_sqlite::dropField()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 471–493 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L471-L493)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function dropField($table, $field)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropField($table, $field) {
    if (!$this->fieldExists($table, $field)) {
      return FALSE;
    }

    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    unset($new_schema['fields'][$field]);
    foreach ($new_schema['indexes'] as $index => $fields) {
      foreach ($fields as $key => $field_name) {
        if ($field_name == $field) {
          unset($new_schema['indexes'][$index][$key]);
        }
      }
      // If this index has no more fields then remove it.
      if (empty($new_schema['indexes'][$index])) {
        unset($new_schema['indexes'][$index]);
      }
    }
    $this->alterTable($table, $old_schema, $new_schema);
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
