# DatabaseTasks_pgsql::name()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 33–35 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L33-L35)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
public function name()
```

## Documentation

_No docblock in source._

## Code

```php
  public function name() {
    return st('PostgreSQL');
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
