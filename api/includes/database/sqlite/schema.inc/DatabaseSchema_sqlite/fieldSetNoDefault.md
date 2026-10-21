# DatabaseSchema_sqlite::fieldSetNoDefault()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 659–669 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L659-L669)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function fieldSetNoDefault($table, $field)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fieldSetNoDefault($table, $field) {
    if (!$this->fieldExists($table, $field)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot remove default value of field @table.@field: field doesn't exist.", array('@table' => $table, '@field' => $field)));
    }

    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    unset($new_schema['fields'][$field]['default']);
    $this->alterTable($table, $old_schema, $new_schema);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
