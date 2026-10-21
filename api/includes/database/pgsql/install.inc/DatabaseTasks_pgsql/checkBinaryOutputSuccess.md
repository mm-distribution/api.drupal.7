# DatabaseTasks_pgsql::checkBinaryOutputSuccess()

- **Type:** Method
- **File:** [`includes/database/pgsql/install.inc`](../_file.md), lines 131–134 · [local source](../../../../../../source/includes/database/pgsql/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc#L131-L134)
- **Class:** [DatabaseTasks_pgsql](../DatabaseTasks_pgsql.md)

## Signature

```php
protected function checkBinaryOutputSuccess()
```

## Documentation

```text
Verify that a binary data roundtrip returns the original string.
```

## Code

```php
  protected function checkBinaryOutputSuccess() {
    $bytea_output = db_query("SELECT 'encoding'::bytea AS output")->fetchField();
    return ($bytea_output == 'encoding');
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
