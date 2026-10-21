# hook_entity_view_mode_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 480–485 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L480-L485)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_view_mode_alter(&$view_mode, $context)
```

## Documentation

```text
Change the view mode of an entity that is being displayed.

@param string $view_mode
  The view_mode that is to be used to display the entity.
@param array $context
  Array with contextual information, including:
  - entity_type: The type of the entity that is being viewed.
  - entity: The entity object.
  - langcode: The langcode the entity is being viewed in.
```

## Code

```php
function hook_entity_view_mode_alter(&$view_mode, $context) {
  // For nodes, change the view mode when it is teaser.
  if ($context['entity_type'] == 'node' && $view_mode == 'teaser') {
    $view_mode = 'my_custom_view_mode';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_view_mode_alter()".

- [node_test_entity_view_mode_alter()](../../node/tests/node_test.module/node_test_entity_view_mode_alter.md) — `modules/node/tests/node_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
