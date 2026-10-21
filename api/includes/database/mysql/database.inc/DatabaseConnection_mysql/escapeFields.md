# DatabaseConnection_mysql::escapeFields()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 422–427 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L422-L427)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function escapeFields(array $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  public function escapeFields(array $fields) {
    foreach ($fields as &$field) {
      $field = $this->escapeField($field);
    }
    return $fields;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
