# locale_translate_delete_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1259–1271 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1259-L1271)
- **Module/theme:** locale
- **Topics:** [locale-translate-edit-delete](../../../topics/locale-translate-edit-delete.md)

## Signature

```php
function locale_translate_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Process string deletion submissions.
```

## Code

```php
function locale_translate_delete_form_submit($form, &$form_state) {
  db_delete('locales_source')
    ->condition('lid', $form_state['values']['lid'])
    ->execute();
  db_delete('locales_target')
    ->condition('lid', $form_state['values']['lid'])
    ->execute();
  // Force JavaScript translation file recreation for all languages.
  _locale_invalidate_js();
  cache_clear_all('locale:', 'cache', TRUE);
  drupal_set_message(t('The string has been removed.'));
  $form_state['redirect'] = 'admin/config/regional/translate/translate';
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
