# DatabaseTasks::minimumVersion()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 390–392 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L390-L392)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
public function minimumVersion()
```

## Documentation

```text
Return the minimum required version of the engine.

@return
  A version string. If not NULL, it will be checked against the version
  reported by the Database engine using version_compare().
```

## Code

```php
  public function minimumVersion() {
    return NULL;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
