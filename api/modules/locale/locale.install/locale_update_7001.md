# locale_update_7001()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 58–112 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L58-L112)
- **Module/theme:** locale
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function locale_update_7001()
```

## Documentation

```text
Upgrade language negotiation settings.
```

## Code

```php
function locale_update_7001() {
  require_once DRUPAL_ROOT . '/includes/language.inc';
  require_once DRUPAL_ROOT . '/includes/locale.inc';
  require_once DRUPAL_ROOT . '/modules/locale/locale.module';

  switch (variable_get('language_negotiation', 0)) {
    // LANGUAGE_NEGOTIATION_NONE.
    case 0:
      $negotiation = array();
      break;

    // LANGUAGE_NEGOTIATION_PATH_DEFAULT.
    case 1:
      $negotiation = array(LOCALE_LANGUAGE_NEGOTIATION_URL);
      // In Drupal 6 path prefixes are shown for the default language only when
      // language negotiation is set to LANGUAGE_NEGOTIATION_PATH, while in
      // Drupal 7 path prefixes are always shown if not empty. Hence we need to
      // ensure that the default language has an empty prefix to avoid breaking
      // the site URLs with a prefix that previously was missing.
      $default = language_default();
      $default->prefix = '';
      variable_set('language_default', $default);
      db_update('languages')
        ->fields(array('prefix' => $default->prefix))
        ->condition('language', $default->language)
        ->execute();
      break;

    // LANGUAGE_NEGOTIATION_PATH.
    case 2:
      $negotiation = array(LOCALE_LANGUAGE_NEGOTIATION_URL, LOCALE_LANGUAGE_NEGOTIATION_USER, LOCALE_LANGUAGE_NEGOTIATION_BROWSER);
      break;

    // LANGUAGE_NEGOTIATION_DOMAIN.
    case 3:
      variable_set('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN);
      $negotiation = array(LOCALE_LANGUAGE_NEGOTIATION_URL);
      break;
  }

  // Save the new language negotiation options.
  language_negotiation_set(LANGUAGE_TYPE_INTERFACE, array_flip($negotiation));
  language_negotiation_set(LANGUAGE_TYPE_CONTENT, array(LOCALE_LANGUAGE_NEGOTIATION_INTERFACE => 0));
  language_negotiation_set(LANGUAGE_TYPE_URL, array(LOCALE_LANGUAGE_NEGOTIATION_URL => 0));

  // Save admininstration UI settings.
  $type = LANGUAGE_TYPE_INTERFACE;
  $provider_weights = array_flip(array_keys(locale_language_negotiation_info()));
  variable_set("locale_language_providers_weight_$type", $provider_weights);

  // Unset the old language negotiation system variable.
  variable_del('language_negotiation');

  return array();
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
