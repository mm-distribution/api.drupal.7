# DatabaseConnection_mysql::escapeAlias()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 432–435 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L432-L435)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function escapeAlias($field)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function escapeAlias($field) {
    $field = parent::escapeAlias($field);
    return $this->quoteIdentifier($field);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
