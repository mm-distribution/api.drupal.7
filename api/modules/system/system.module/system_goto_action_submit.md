# system_goto_action_submit()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3374–3378 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3374-L3378)
- **Module/theme:** system

## Signature

```php
function system_goto_action_submit($form, $form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function system_goto_action_submit($form, $form_state) {
  return array(
    'url' => $form_state['values']['url']
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
