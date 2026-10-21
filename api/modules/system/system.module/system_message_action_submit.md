# system_message_action_submit()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3332–3334 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3332-L3334)
- **Module/theme:** system

## Signature

```php
function system_message_action_submit($form, $form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function system_message_action_submit($form, $form_state) {
  return array('message' => $form_state['values']['message']);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
