# locale_date_format_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1395–1410 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1395-L1410)
- **Module/theme:** locale

## Signature

```php
function locale_date_format_form_submit($form, &$form_state)
```

## Documentation

```text
Submit handler for configuring localized date formats on the locale_date_format_form.
```

## Code

```php
function locale_date_format_form_submit($form, &$form_state) {
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  $langcode = $form_state['values']['langcode'];

  // Get list of date format types.
  $types = system_get_date_types();
  foreach ($types as $type => $type_info) {
    $format = $form_state['values']['date_format_' . $type];
    if ($format == 'custom') {
      $format = $form_state['values']['date_format_' . $type . '_custom'];
    }
    locale_date_format_save($langcode, $type, $format);
  }
  drupal_set_message(t('Configuration saved.'));
  $form_state['redirect'] = 'admin/config/regional/date-time/locale';
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
