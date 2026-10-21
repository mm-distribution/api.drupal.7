# DatabaseSchema_mysql::fieldSetDefault()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 375–388 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L375-L388)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

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

    if (!isset($default)) {
      $default = 'NULL';
    }
    else {
      $default = is_string($default) ? "'$default'" : $default;
    }

    $this->connection->query('ALTER TABLE {' . $table . '} ALTER COLUMN `' . $field . '` SET DEFAULT ' . $default);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
