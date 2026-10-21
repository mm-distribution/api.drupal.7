# contact_form_user_admin_settings_alter()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 254–266 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L254-L266)
- **Module/theme:** contact
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function contact_form_user_admin_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Add the default personal contact setting on the user settings page.

@see user_admin_settings()
```

## Code

```php
function contact_form_user_admin_settings_alter(&$form, &$form_state) {
  $form['contact'] = array(
    '#type' => 'fieldset',
    '#title' => t('Contact settings'),
    '#weight' => 0,
  );
  $form['contact']['contact_default_status'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable the personal contact form by default for new users.'),
    '#description' => t('Changing this setting will not affect existing users.'),
    '#default_value' => variable_get('contact_default_status', 1),
  );
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
