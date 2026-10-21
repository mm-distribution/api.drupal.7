# DatabaseTasks::hasPdoDriver()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 353–355 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L353-L355)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function hasPdoDriver()
```

## Documentation

```text
Ensure the PDO driver is supported by the version of PHP in use.
```

## Code

```php
  protected function hasPdoDriver() {
    return in_array($this->pdoDriver, PDO::getAvailableDrivers());
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
