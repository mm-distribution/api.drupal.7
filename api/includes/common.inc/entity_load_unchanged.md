# entity_load_unchanged()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8236–8240 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8236-L8240)

## Signature

```php
function entity_load_unchanged($entity_type, $id)
```

## Documentation

```text
Loads the unchanged, i.e. not modified, entity from the database.

Unlike entity_load() this function ensures the entity is directly loaded from
the database, thus bypassing any static cache. In particular, this function
is useful to determine changes by comparing the entity being saved to the
stored entity.

@param $entity_type
  The entity type to load, e.g. node or user.
@param $id
  The ID of the entity to load.

@return
  The unchanged entity, or FALSE if the entity cannot be loaded.
```

## Code

```php
function entity_load_unchanged($entity_type, $id) {
  entity_get_controller($entity_type)->resetCache(array($id));
  $result = entity_get_controller($entity_type)->load(array($id));
  return reset($result);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
