# hook_entity_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 316–318 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L316-L318)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_presave($entity, $type)
```

## Documentation

```text
Act on an entity before it is about to be created or updated.

@param $entity
  The entity object.
@param $type
  The type of entity being saved (i.e. node, user, comment).
```

## Code

```php
function hook_entity_presave($entity, $type) {
  $entity->changed = REQUEST_TIME;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_presave()".

- [entity_crud_hook_test_entity_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_entity_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
