# system_form_user_profile_form_alter()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1999–2006 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1999-L2006)
- **Module/theme:** system
- **Implements:** [hook_form_FORM_ID_alter()](../system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function system_form_user_profile_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function system_form_user_profile_form_alter(&$form, &$form_state) {
  if ($form['#user_category'] == 'account') {
    if (variable_get('configurable_timezones', 1)) {
      system_user_timezone($form, $form_state);
    }
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
