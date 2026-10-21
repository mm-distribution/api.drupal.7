# DrupalDefaultEntityController::resetCache()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 143–152 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L143-L152)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
public function resetCache(array $ids = NULL)
```

## Documentation

```text
Implements DrupalEntityControllerInterface::resetCache().
```

## Code

```php
  public function resetCache(array $ids = NULL) {
    if (isset($ids)) {
      foreach ($ids as $id) {
        unset($this->entityCache[$id]);
      }
    }
    else {
      $this->entityCache = array();
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
