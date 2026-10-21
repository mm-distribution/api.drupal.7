# DrupalEntityControllerInterface::resetCache()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 23–23 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L23)
- **Class:** [DrupalEntityControllerInterface](../DrupalEntityControllerInterface.md)

## Signature

```php
public function resetCache(array $ids = NULL);
```

## Documentation

```text
Resets the internal, static entity cache.

@param $ids
  (optional) If specified, the cache is reset for the entities with the
  given ids only.
```

## Code

```php
  public function resetCache(array $ids = NULL);
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
