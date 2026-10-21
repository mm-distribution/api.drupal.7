# locale_translate_edit_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1191–1236 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1191-L1236)
- **Module/theme:** locale
- **Topics:** [locale-translate-edit-delete](../../../topics/locale-translate-edit-delete.md)

## Signature

```php
function locale_translate_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Process string editing form submissions.

Saves all translations of one string submitted from a form.
```

## Code

```php
function locale_translate_edit_form_submit($form, &$form_state) {
  $lid = $form_state['values']['lid'];
  foreach ($form_state['values']['translations'] as $key => $value) {
    $translation = db_query("SELECT translation FROM {locales_target} WHERE lid = :lid AND language = :language", array(':lid' => $lid, ':language' => $key))->fetchField();
    if (!empty($value)) {
      // Only update or insert if we have a value to use.
      if (is_string($translation)) {
        db_update('locales_target')
          ->fields(array(
            'translation' => $value,
          ))
          ->condition('lid', $lid)
          ->condition('language', $key)
          ->execute();
      }
      else {
        db_insert('locales_target')
          ->fields(array(
            'lid' => $lid,
            'translation' => $value,
            'language' => $key,
          ))
          ->execute();
      }
    }
    elseif (!empty($translation)) {
      // Empty translation entered: remove existing entry from database.
      db_delete('locales_target')
        ->condition('lid', $lid)
        ->condition('language', $key)
        ->execute();
    }

    // Force JavaScript translation file recreation for this language.
    _locale_invalidate_js($key);
  }

  drupal_set_message(t('The string has been saved.'));

  // Clear locale cache.
  _locale_invalidate_js();
  cache_clear_all('locale:', 'cache', TRUE);

  $form_state['redirect'] = 'admin/config/regional/translate/translate';
  return;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
