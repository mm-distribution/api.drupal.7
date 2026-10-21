# actions_list()

- **Type:** Function
- **File:** [`includes/actions.inc`](_file.md), lines 162–171 · [local source](../../../source/includes/actions.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc#L162-L171)

## Signature

```php
function actions_list($reset = FALSE)
```

## Documentation

```text
Discovers all available actions by invoking hook_action_info().

This function contrasts with actions_get_all_actions(); see the
documentation of actions_get_all_actions() for an explanation.

@param $reset
  Reset the action info static cache.

@return
  An associative array keyed on action function name, with the same format
  as the return value of hook_action_info(), containing all
  modules' hook_action_info() return values as modified by any
  hook_action_info_alter() implementations.

@see hook_action_info()
```

## Code

```php
function actions_list($reset = FALSE) {
  $actions = &drupal_static(__FUNCTION__);
  if (!isset($actions) || $reset) {
    $actions = module_invoke_all('action_info');
    drupal_alter('action_info', $actions);
  }

  // See module_implements() for an explanation of this cast.
  return (array) $actions;
}
```

---
_Drupal 7.103 · [includes/actions.inc](https://github.com/drupal/drupal/blob/7.103/includes/actions.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
