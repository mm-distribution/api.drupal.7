# locale_translate_edit_form_validate()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1175–1184 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1175-L1184)
- **Module/theme:** locale
- **Topics:** [locale-translate-edit-delete](../../../topics/locale-translate-edit-delete.md)

## Signature

```php
function locale_translate_edit_form_validate($form, &$form_state)
```

## Documentation

```text
Validate string editing form submissions.
```

## Code

```php
function locale_translate_edit_form_validate($form, &$form_state) {
  // Locale string check is needed for default textgroup only.
  $safe_check_needed = $form_state['values']['textgroup'] == 'default';
  foreach ($form_state['values']['translations'] as $key => $value) {
    if ($safe_check_needed && !locale_string_is_safe($value)) {
      form_set_error('translations', t('The submitted string contains disallowed HTML: %string', array('%string' => $value)));
      watchdog('locale', 'Attempted submission of a translation string with disallowed HTML: %string', array('%string' => $value), WATCHDOG_WARNING);
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
