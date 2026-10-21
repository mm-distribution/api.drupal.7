# minimal_form_install_configure_form_alter()

- **Type:** Function
- **File:** [`profiles/minimal/minimal.profile`](_file.md), lines 12–15 · [local source](../../../../source/profiles/minimal/minimal.profile) · [GitHub](https://github.com/drupal/drupal/blob/7.103/profiles/minimal/minimal.profile#L12-L15)
- **Module/theme:** minimal
- **Implements:** [hook_form_FORM_ID_alter()](../../../modules/system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function minimal_form_install_configure_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for install_configure_form().

Allows the profile to alter the site configuration form.
```

## Code

```php
function minimal_form_install_configure_form_alter(&$form, $form_state) {
  // Pre-populate the site name with the server name.
  $form['site_information']['site_name']['#default_value'] = $_SERVER['SERVER_NAME'];
}
```

---
_Drupal 7.103 · [profiles/minimal/minimal.profile](https://github.com/drupal/drupal/blob/7.103/profiles/minimal/minimal.profile) · Licensed GPL-2.0-or-later (see LICENSE)._
