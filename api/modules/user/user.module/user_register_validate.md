# user_register_validate()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3968–3970 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3968-L3970)
- **Module/theme:** user

## Signature

```php
function user_register_validate($form, &$form_state)
```

## Documentation

```text
Validation function for the user registration form.
```

## Code

```php
function user_register_validate($form, &$form_state) {
  entity_form_field_validate('user', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
