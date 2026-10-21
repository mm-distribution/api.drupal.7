# DatabaseTasks::installable()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 374–376 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L374-L376)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
public function installable()
```

## Documentation

```text
Check whether Drupal is installable on the database.
```

## Code

```php
  public function installable() {
    return $this->hasPdoDriver() && empty($this->error);
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
