# DatabaseTasks::pass()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 367–369 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L367-L369)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function pass($message)
```

## Documentation

```text
Assert test as a pass.
```

## Code

```php
  protected function pass($message) {
    $this->results[$message] = TRUE;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
