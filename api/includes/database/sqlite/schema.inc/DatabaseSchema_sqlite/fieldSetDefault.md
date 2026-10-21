# DatabaseSchema_sqlite::fieldSetDefault()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 647–657 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L647-L657)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function fieldSetDefault($table, $field, $default)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fieldSetDefault($table, $field, $default) {
    if (!$this->fieldExists($table, $field)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot set default value of field @table.@field: field doesn't exist.", array('@table' => $table, '@field' => $field)));
    }

    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    $new_schema['fields'][$field]['default'] = $default;
    $this->alterTable($table, $old_schema, $new_schema);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
