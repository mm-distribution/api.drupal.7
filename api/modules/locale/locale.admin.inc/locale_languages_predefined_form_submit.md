# locale_languages_predefined_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 348–370 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L348-L370)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_predefined_form_submit($form, &$form_state)
```

## Documentation

```text
Process the language addition form submission.
```

## Code

```php
function locale_languages_predefined_form_submit($form, &$form_state) {
  $langcode = $form_state['values']['langcode'];
  if (isset($form_state['values']['name'])) {
    // Custom language form.
    locale_add_language($langcode, $form_state['values']['name'], $form_state['values']['native'], $form_state['values']['direction'], $form_state['values']['domain'], $form_state['values']['prefix']);
    drupal_set_message(t('The language %language has been created and can now be used. More information is available on the <a href="@locale-help">help screen</a>.', array('%language' => t($form_state['values']['name']), '@locale-help' => url('admin/help/locale'))));
  }
  else {
    // Predefined language selection.
    include_once DRUPAL_ROOT . '/includes/iso.inc';
    $predefined = _locale_get_predefined_list();
    locale_add_language($langcode);
    drupal_set_message(t('The language %language has been created and can now be used. More information is available on the <a href="@locale-help">help screen</a>.', array('%language' => t($predefined[$langcode][0]), '@locale-help' => url('admin/help/locale'))));
  }

  // See if we have language files to import for the newly added
  // language, collect and import them.
  if ($batch = locale_batch_by_language($langcode, '_locale_batch_language_finished')) {
    batch_set($batch);
  }

  $form_state['redirect'] = 'admin/config/regional/language';
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
