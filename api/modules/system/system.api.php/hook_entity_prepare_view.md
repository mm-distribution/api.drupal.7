# hook_entity_prepare_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 547–555 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L547-L555)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_prepare_view($entities, $type, $langcode)
```

## Documentation

```text
Act on entities as they are being prepared for view.

Allows you to operate on multiple entities as they are being prepared for
view. Only use this if attaching the data during the entity_load() phase
is not appropriate, for example when attaching other 'entity' style objects.

@param $entities
  The entities keyed by entity ID.
@param $type
  The type of entities being loaded (i.e. node, user, comment).
@param $langcode
  The language to display the entity in.
```

## Code

```php
function hook_entity_prepare_view($entities, $type, $langcode) {
  // Load a specific node into the user object for later theming.
  if ($type == 'user') {
    $nodes = mymodule_get_user_nodes(array_keys($entities));
    foreach ($entities as $uid => $entity) {
      $entity->user_node = $nodes[$uid];
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_prepare_view()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
