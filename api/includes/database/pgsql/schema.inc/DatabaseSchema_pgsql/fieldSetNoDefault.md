# DatabaseSchema_pgsql::fieldSetNoDefault()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 594–600 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L594-L600)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

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

    $this->connection->query('ALTER TABLE {' . $table . '} ALTER COLUMN "' . $field . '" DROP DEFAULT');
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
