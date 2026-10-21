# DatabaseTasks::fail()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 360–362 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L360-L362)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function fail($message)
```

## Documentation

```text
Assert test as failed.
```

## Code

```php
  protected function fail($message) {
    $this->results[$message] = FALSE;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
