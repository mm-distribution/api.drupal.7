# entity_load()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8213–8218 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8213-L8218)

## Signature

```php
function entity_load($entity_type, $ids = FALSE, $conditions = array(), $reset = FALSE)
```

## Documentation

```text
Load entities from the database.

The entities are stored in a static memory cache, and will not require
database access if loaded again during the same page request.

The actual loading is done through a class that has to implement the
DrupalEntityControllerInterface interface. By default,
DrupalDefaultEntityController is used. Entity types can specify that a
different class should be used by setting the 'controller class' key in
hook_entity_info(). These classes can either implement the
DrupalEntityControllerInterface interface, or, most commonly, extend the
DrupalDefaultEntityController class. See node_entity_info() and the
NodeController in node.module as an example.

@param $entity_type
  The entity type to load, e.g. node or user.
@param $ids
  An array of entity IDs, or FALSE to load all entities.
@param $conditions
  (deprecated) An associative array of conditions on the base table, where
  the keys are the database fields and the values are the values those
  fields must have. Instead, it is preferable to use EntityFieldQuery to
  retrieve a list of entity IDs loadable by this function.
@param $reset
  Whether to reset the internal cache for the requested entity type.

@return
  An array of entity objects indexed by their ids. When no results are
  found, an empty array is returned.

@todo Remove $conditions in Drupal 8.

@see hook_entity_info()
@see DrupalEntityControllerInterface
@see DrupalDefaultEntityController
@see EntityFieldQuery
```

## Code

```php
function entity_load($entity_type, $ids = FALSE, $conditions = array(), $reset = FALSE) {
  if ($reset) {
    entity_get_controller($entity_type)->resetCache();
  }
  return entity_get_controller($entity_type)->load($ids, $conditions);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
