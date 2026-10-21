# Updater::postInstallTasks()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 401–403 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L401-L403)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function postInstallTasks()
```

## Documentation

```text
Return an array of links to pages that should be visited post operation.

@return array
  Links which provide actions to take after the install is finished.
```

## Code

```php
  public function postInstallTasks() {
    return array();
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
