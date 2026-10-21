# DrupalEntityControllerInterface

- **Type:** Interface
- **File:** [`includes/entity.inc`](_file.md), lines 14–40 · [local source](../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L14-L40)

## Signature

```php
interface DrupalEntityControllerInterface
```

## Documentation

```text
Interface for entity controller classes.

All entity controller classes specified via the 'controller class' key
returned by hook_entity_info() or hook_entity_info_alter() have to implement
this interface.

Most simple, SQL-based entity controllers will do better by extending
DrupalDefaultEntityController instead of implementing this interface
directly.
```

## Methods (derived index)

- [resetCache()](DrupalEntityControllerInterface/resetCache.md) — Resets the internal, static entity cache.
- [load()](DrupalEntityControllerInterface/load.md) — Loads one or more entities.

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
