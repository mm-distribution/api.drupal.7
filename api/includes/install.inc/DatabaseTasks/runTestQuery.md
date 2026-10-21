# DatabaseTasks::runTestQuery()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 449–458 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L449-L458)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function runTestQuery($query, $pass, $fail, $fatal = FALSE)
```

## Documentation

```text
Run SQL tests to ensure the database can execute commands with the current user.
```

## Code

```php
  protected function runTestQuery($query, $pass, $fail, $fatal = FALSE) {
    try {
      db_query($query);
      $this->pass(st($pass));
    }
    catch (Exception $e) {
      $this->fail(st($fail, array('%query' => $query, '%error' => $e->getMessage(), '%name' => $this->name())));
      return !$fatal;
    }
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
