# system_form_user_register_form_alter()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2011–2024 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2011-L2024)
- **Module/theme:** system
- **Implements:** [hook_form_FORM_ID_alter()](../system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function system_form_user_register_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function system_form_user_register_form_alter(&$form, &$form_state) {
  if (variable_get('configurable_timezones', 1)) {
    if (variable_get('user_default_timezone', DRUPAL_USER_TIMEZONE_DEFAULT) == DRUPAL_USER_TIMEZONE_SELECT) {
      system_user_timezone($form, $form_state);
    }
    else {
      $form['account']['timezone'] = array(
        '#type' => 'hidden',
        '#value' => variable_get('user_default_timezone', DRUPAL_USER_TIMEZONE_DEFAULT) ? '' : variable_get('date_default_timezone', ''),
      );
    }
    return $form;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
