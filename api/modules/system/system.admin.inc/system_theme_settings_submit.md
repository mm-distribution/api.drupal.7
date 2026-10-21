# system_theme_settings_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 694–741 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L694-L741)
- **Module/theme:** system

## Signature

```php
function system_theme_settings_submit($form, &$form_state)
```

## Documentation

```text
Process system_theme_settings form submissions.
```

## Code

```php
function system_theme_settings_submit($form, &$form_state) {
  // Exclude unnecessary elements before saving.
  form_state_values_clean($form_state);

  $values = $form_state['values'];

  // Extract the name of the theme from the submitted form values, then remove
  // it from the array so that it is not saved as part of the variable.
  $key = $values['var'];
  unset($values['var']);

  // If the user uploaded a new logo or favicon, save it to a permanent location
  // and use it in place of the default theme-provided file.
  if (!empty($values['logo_upload'])) {
    $file = $values['logo_upload'];
    unset($values['logo_upload']);
    $filename = file_unmanaged_copy($file->uri);
    $values['default_logo'] = 0;
    $values['logo_path'] = $filename;
    $values['toggle_logo'] = 1;
  }
  if (!empty($values['favicon_upload'])) {
    $file = $values['favicon_upload'];
    unset($values['favicon_upload']);
    $filename = file_unmanaged_copy($file->uri);
    $values['default_favicon'] = 0;
    $values['favicon_path'] = $filename;
    $values['toggle_favicon'] = 1;
  }

  // If the user entered a path relative to the system files directory for
  // a logo or favicon, store a public:// URI so the theme system can handle it.
  if (!empty($values['logo_path'])) {
    $values['logo_path'] = _system_theme_settings_validate_path($values['logo_path']);
  }
  if (!empty($values['favicon_path'])) {
    $values['favicon_path'] = _system_theme_settings_validate_path($values['favicon_path']);
  }

  if (empty($values['default_favicon']) && !empty($values['favicon_path'])) {
    $values['favicon_mimetype'] = file_get_mimetype($values['favicon_path']);
  }

  variable_set($key, $values);
  drupal_set_message(t('The configuration options have been saved.'));

  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
