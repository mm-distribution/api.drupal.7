# system_logging_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1681–1695 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1681-L1695)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_logging_settings()
```

## Documentation

```text
Form builder; Configure error reporting settings.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_logging_settings() {
  $form['error_level'] = array(
    '#type' => 'radios',
    '#title' => t('Error messages to display'),
    '#default_value' => variable_get('error_level', ERROR_REPORTING_DISPLAY_ALL),
    '#options' => array(
      ERROR_REPORTING_HIDE => t('None'),
      ERROR_REPORTING_DISPLAY_SOME => t('Errors and warnings'),
      ERROR_REPORTING_DISPLAY_ALL => t('All messages'),
    ),
    '#description' => t('It is recommended that sites running on production environments do not display any errors.'),
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
