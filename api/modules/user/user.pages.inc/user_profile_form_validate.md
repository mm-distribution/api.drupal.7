# user_profile_form_validate()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 440–442 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L440-L442)
- **Module/theme:** user

## Signature

```php
function user_profile_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for user_profile_form().

@see user_profile_form_submit()
```

## Code

```php
function user_profile_form_validate($form, &$form_state) {
  entity_form_field_validate('user', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
