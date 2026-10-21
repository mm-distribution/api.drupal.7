# DatabaseTasks::checkEngineVersion()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 463–467 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L463-L467)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
protected function checkEngineVersion()
```

## Documentation

```text
Check the engine version.
```

## Code

```php
  protected function checkEngineVersion() {
    if ($this->minimumVersion() && version_compare(Database::getConnection()->version(), $this->minimumVersion(), '<')) {
      $this->fail(st("The database version %version is less than the minimum required version %minimum_version.", array('%version' => Database::getConnection()->version(), '%minimum_version' => $this->minimumVersion())));
    }
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
