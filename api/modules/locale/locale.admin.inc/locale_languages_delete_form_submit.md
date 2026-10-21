# locale_languages_delete_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 461–493 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L461-L493)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_delete_form_submit($form, &$form_state)
```

## Documentation

```text
Process language deletion submissions.
```

## Code

```php
function locale_languages_delete_form_submit($form, &$form_state) {
  $languages = language_list();
  if (isset($languages[$form_state['values']['langcode']])) {
    // Remove translations first.
    db_delete('locales_target')
      ->condition('language', $form_state['values']['langcode'])
      ->execute();
    cache_clear_all('locale:' . $form_state['values']['langcode'], 'cache');
    // With no translations, this removes existing JavaScript translations file.
    _locale_rebuild_js($form_state['values']['langcode']);
    // Remove the language.
    db_delete('languages')
      ->condition('language', $form_state['values']['langcode'])
      ->execute();
    db_update('node')
      ->fields(array('language' => ''))
      ->condition('language', $form_state['values']['langcode'])
      ->execute();
    if ($languages[$form_state['values']['langcode']]->enabled) {
      variable_set('language_count', variable_get('language_count', 1) - 1);
    }
    module_invoke_all('multilingual_settings_changed');
    $variables = array('%locale' => $languages[$form_state['values']['langcode']]->name);
    drupal_set_message(t('The language %locale has been removed.', $variables));
    watchdog('locale', 'The language %locale has been removed.', $variables);
  }

  // Changing the language settings impacts the interface:
  cache_clear_all('*', 'cache_page', TRUE);

  $form_state['redirect'] = 'admin/config/regional/language';
  return;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
