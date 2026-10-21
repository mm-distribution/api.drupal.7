# hook_entity_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 302–306 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L302-L306)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_load($entities, $type)
```

## Documentation

```text
Act on entities when loaded.

This is a generic load hook called for all entity types loaded via the
entity API.

@param $entities
  The entities keyed by entity ID.
@param $type
  The type of entities being loaded (i.e. node, user, comment).
```

## Code

```php
function hook_entity_load($entities, $type) {
  foreach ($entities as $entity) {
    $entity->foo = mymodule_add_something($entity, $type);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_load()".

- [entity_crud_hook_test_entity_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_entity_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [rdf_entity_load()](../../rdf/rdf.module/rdf_entity_load.md) — `modules/rdf/rdf.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
