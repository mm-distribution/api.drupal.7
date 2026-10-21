# openid_form_user_login_alter()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 132–134 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L132-L134)
- **Module/theme:** openid
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function openid_form_user_login_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function openid_form_user_login_alter(&$form, &$form_state) {
  _openid_user_login_form_alter($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
