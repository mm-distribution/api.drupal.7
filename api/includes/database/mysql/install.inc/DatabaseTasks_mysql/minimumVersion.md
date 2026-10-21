# DatabaseTasks_mysql::minimumVersion()

- **Type:** Method
- **File:** [`includes/database/mysql/install.inc`](../_file.md), lines 29–31 · [local source](../../../../../../source/includes/database/mysql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc#L29-L31)
- **Class:** [DatabaseTasks_mysql](../DatabaseTasks_mysql.md)

## Signature

```php
public function minimumVersion()
```

## Documentation

```text
Returns the minimum version for MySQL.
```

## Code

```php
  public function minimumVersion() {
    return '5.0.15';
  }
```

---
_Drupal 7.103 · [includes/database/mysql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
