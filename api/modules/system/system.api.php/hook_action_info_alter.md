# hook_action_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4066–4068 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4066-L4068)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_action_info_alter(&$actions)
```

## Documentation

```text
Alters the actions declared by another module.

Called by actions_list() to allow modules to alter the return values from
implementations of hook_action_info().

@see trigger_example_action_info_alter()
```

## Code

```php
function hook_action_info_alter(&$actions) {
  $actions['node_unpublish_action']['label'] = t('Unpublish and remove from public view.');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_action_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
