# locale_date_format_reset_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1431–1436 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1431-L1436)
- **Module/theme:** locale

## Signature

```php
function locale_date_format_reset_form_submit($form, &$form_state)
```

## Documentation

```text
Reset date formats for a specific language to global defaults.
```

## Code

```php
function locale_date_format_reset_form_submit($form, &$form_state) {
  db_delete('date_format_locale')
    ->condition('language', $form_state['values']['langcode'])
    ->execute();
  $form_state['redirect'] = 'admin/config/regional/date-time/locale';
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
