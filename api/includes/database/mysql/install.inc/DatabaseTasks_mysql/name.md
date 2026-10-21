# DatabaseTasks_mysql::name()

- **Type:** Method
- **File:** [`includes/database/mysql/install.inc`](../_file.md), lines 22–24 · [local source](../../../../../../source/includes/database/mysql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc#L22-L24)
- **Class:** [DatabaseTasks_mysql](../DatabaseTasks_mysql.md)

## Signature

```php
public function name()
```

## Documentation

```text
Returns a human-readable name string for MySQL and equivalent databases.
```

## Code

```php
  public function name() {
    return st('MySQL, MariaDB, or equivalent');
  }
```

---
_Drupal 7.103 · [includes/database/mysql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
