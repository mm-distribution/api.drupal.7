# system_actions_configure_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3192–3198 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3192-L3198)
- **Module/theme:** system

## Signature

```php
function system_actions_configure_validate($form, &$form_state)
```

## Documentation

```text
Validate system_actions_configure() form submissions.
```

## Code

```php
function system_actions_configure_validate($form, &$form_state) {
  $function = actions_function_lookup($form_state['values']['actions_action']) . '_validate';
  // Hand off validation to the action.
  if (function_exists($function)) {
    $function($form, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
