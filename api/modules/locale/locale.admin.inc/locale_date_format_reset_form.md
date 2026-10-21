# locale_date_format_reset_form()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1418–1426 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1418-L1426)
- **Module/theme:** locale

## Signature

```php
function locale_date_format_reset_form($form, &$form_state, $langcode)
```

## Documentation

```text
Reset locale specific date formats to the global defaults.

@param $langcode
  Language code, e.g. 'en'.
```

## Code

```php
function locale_date_format_reset_form($form, &$form_state, $langcode) {
  $form['langcode'] = array('#type' => 'value', '#value' => $langcode);
  $languages = language_list();
  return confirm_form($form,
    t('Are you sure you want to reset the date formats for %language to the global defaults?', array('%language' => $languages[$langcode]->name)),
    'admin/config/regional/date-time/locale',
    t('Resetting will remove all localized date formats for this language. This action cannot be undone.'),
    t('Reset'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
