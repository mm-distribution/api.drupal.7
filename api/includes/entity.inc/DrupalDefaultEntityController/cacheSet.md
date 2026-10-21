# DrupalDefaultEntityController::cacheSet()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 433–435 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L433-L435)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function cacheSet($entities)
```

## Documentation

```text
Stores entities in the static entity cache.

@param $entities
  Entities to store in the cache.
```

## Code

```php
  protected function cacheSet($entities) {
    $this->entityCache += $entities;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
