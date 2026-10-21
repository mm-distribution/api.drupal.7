# system_site_information_settings_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1578–1611 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1578-L1611)
- **Module/theme:** system

## Signature

```php
function system_site_information_settings_validate($form, &$form_state)
```

## Documentation

```text
Validates the submitted site-information form.
```

## Code

```php
function system_site_information_settings_validate($form, &$form_state) {
  // Validate the e-mail address.
  if ($error = user_validate_mail($form_state['values']['site_mail'])) {
    form_set_error('site_mail', $error);
  }
  // Check for empty front page path.
  if (empty($form_state['values']['site_frontpage'])) {
    // Set to default "node".
    form_set_value($form['front_page']['site_frontpage'], 'node', $form_state);
  }
  else {
    // Get the normal path of the front page.
    form_set_value($form['front_page']['site_frontpage'], drupal_get_normal_path($form_state['values']['site_frontpage']), $form_state);
  }
  // Validate front page path.
  if (!drupal_valid_path($form_state['values']['site_frontpage'])) {
    form_set_error('site_frontpage', t("The path '%path' is either invalid or you do not have access to it.", array('%path' => $form_state['values']['site_frontpage'])));
  }
  // Get the normal paths of both error pages.
  if (!empty($form_state['values']['site_403'])) {
    form_set_value($form['error_page']['site_403'], drupal_get_normal_path($form_state['values']['site_403']), $form_state);
  }
  if (!empty($form_state['values']['site_404'])) {
    form_set_value($form['error_page']['site_404'], drupal_get_normal_path($form_state['values']['site_404']), $form_state);
  }
  // Validate 403 error path.
  if (!empty($form_state['values']['site_403']) && !drupal_valid_path($form_state['values']['site_403'])) {
    form_set_error('site_403', t("The path '%path' is either invalid or you do not have access to it.", array('%path' => $form_state['values']['site_403'])));
  }
  // Validate 404 error path.
  if (!empty($form_state['values']['site_404']) && !drupal_valid_path($form_state['values']['site_404'])) {
    form_set_error('site_404', t("The path '%path' is either invalid or you do not have access to it.", array('%path' => $form_state['values']['site_404'])));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
