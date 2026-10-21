# callback_entity_info_language()

- **Type:** Function
- **File:** [`modules/system/system.api.php`](_file.md), lines 4936–4938 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4936-L4938)
- **Module/theme:** system
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_entity_info_language($entity, $entity_type)
```

## Documentation

```text
Return the language code of the entity.

Callback for hook_entity_info().

The language callback is meant to be used primarily for temporary alterations
of the property value.

@param $entity
  The entity for which to return the language.
@param $entity_type
  The entity type; e.g., 'node' or 'user'.

@return
  The language code for the language of the entity.

@see entity_language()
```

## Code

```php
function callback_entity_info_language($entity, $entity_type) {
  return $entity->language;
}
```

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
