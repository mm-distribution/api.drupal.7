# user_form_field_ui_field_edit_form_submit()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3893–3899 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3893-L3899)
- **Module/theme:** user

## Signature

```php
function user_form_field_ui_field_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Additional submit handler for the 'Edit field instance' form.

Make sure the 'user_register_form' setting is set for required fields.
```

## Code

```php
function user_form_field_ui_field_edit_form_submit($form, &$form_state) {
  $instance = $form_state['values']['instance'];

  if (!empty($instance['required'])) {
    form_set_value($form['instance']['settings']['user_register_form'], 1, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
