# DatabaseConnection_mysql::escapeField()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 417–420 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L417-L420)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function escapeField($field)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function escapeField($field) {
    $field = parent::escapeField($field);
    return $this->quoteIdentifier($field);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
