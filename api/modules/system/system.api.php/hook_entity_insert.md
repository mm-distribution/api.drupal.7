# hook_entity_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 328–340 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L328-L340)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_insert($entity, $type)
```

## Documentation

```text
Act on entities when inserted.

@param $entity
  The entity object.
@param $type
  The type of entity being inserted (i.e. node, user, comment).
```

## Code

```php
function hook_entity_insert($entity, $type) {
  // Insert the new entity into a fictional table of all entities.
  $info = entity_get_info($type);
  list($id) = entity_extract_ids($type, $entity);
  db_insert('example_entity')
    ->fields(array(
      'type' => $type,
      'id' => $id,
      'created' => REQUEST_TIME,
      'updated' => REQUEST_TIME,
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_insert()".

- [entity_crud_hook_test_entity_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_entity_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
