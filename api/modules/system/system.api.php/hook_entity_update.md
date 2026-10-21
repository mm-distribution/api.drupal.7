# hook_entity_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 350–361 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L350-L361)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_update($entity, $type)
```

## Documentation

```text
Act on entities when updated.

@param $entity
  The entity object.
@param $type
  The type of entity being updated (i.e. node, user, comment).
```

## Code

```php
function hook_entity_update($entity, $type) {
  // Update the entity's entry in a fictional table of all entities.
  $info = entity_get_info($type);
  list($id) = entity_extract_ids($type, $entity);
  db_update('example_entity')
    ->fields(array(
      'updated' => REQUEST_TIME,
    ))
    ->condition('type', $type)
    ->condition('id', $id)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_update()".

- [entity_crud_hook_test_entity_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_entity_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
