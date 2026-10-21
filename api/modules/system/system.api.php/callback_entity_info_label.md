# callback_entity_info_label()

- **Type:** Function
- **File:** [`modules/system/system.api.php`](_file.md), lines 4914–4916 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4914-L4916)
- **Module/theme:** system
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_entity_info_label($entity, $entity_type)
```

## Documentation

```text
Return the label of an entity.

Callback for hook_entity_info().

@param $entity
  The entity for which to generate the label.
@param $entity_type
  The entity type; e.g., 'node' or 'user'.

@return
  An unsanitized string with the label of the entity.

@see entity_label()
```

## Code

```php
function callback_entity_info_label($entity, $entity_type) {
  return empty($entity->title) ? 'Untitled entity' : $entity->title;
}
```

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
