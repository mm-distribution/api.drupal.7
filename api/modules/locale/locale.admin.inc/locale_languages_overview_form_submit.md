# locale_languages_overview_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 120–176 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L120-L176)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_overview_form_submit($form, &$form_state)
```

## Documentation

```text
Process language overview form submissions, updating existing languages.
```

## Code

```php
function locale_languages_overview_form_submit($form, &$form_state) {
  $languages = language_list();
  $default = language_default();
  $url_prefixes = variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX) == LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX;
  $enabled_count = 0;

  foreach ($languages as $langcode => $language) {
    if ($form_state['values']['site_default'] == $langcode || $default->language == $langcode) {
      // Automatically enable the default language and the language
      // which was default previously (because we will not get the
      // value from that disabled checkbox).
      $form_state['values']['enabled'][$langcode] = 1;
    }

    // If language URL prefixes are enabled we must clear language domains and
    // assign a valid prefix to each non-default language.
    if ($url_prefixes) {
      $language->domain = '';
      if (empty($language->prefix) && $form_state['values']['site_default'] != $langcode) {
        $language->prefix = $langcode;
      }
    }

    if ($form_state['values']['enabled'][$langcode]) {
      $enabled_count++;
      $language->enabled = 1;
    }
    else {
      $language->enabled = 0;
    }

    $language->weight = $form_state['values']['weight'][$langcode];

    db_update('languages')
      ->fields(array(
        'enabled' => $language->enabled,
        'weight' => $language->weight,
        'prefix' => $language->prefix,
        'domain' => $language->domain,
      ))
      ->condition('language', $langcode)
      ->execute();

    $languages[$langcode] = $language;
  }

  variable_set('language_default', $languages[$form_state['values']['site_default']]);
  variable_set('language_count', $enabled_count);
  drupal_set_message(t('Configuration saved.'));

  // Changing the language settings impacts the interface.
  cache_clear_all('*', 'cache_page', TRUE);
  module_invoke_all('multilingual_settings_changed');

  $form_state['redirect'] = 'admin/config/regional/language';
  return;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
