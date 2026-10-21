# locale_language_negotiation_info()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 568–636 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L568-L636)
- **Module/theme:** locale
- **Implements:** [hook_language_negotiation_info()](../../system/language.api.php/hook_language_negotiation_info.md)

## Signature

```php
function locale_language_negotiation_info()
```

## Documentation

```text
Implements hook_language_negotiation_info().
```

## Code

```php
function locale_language_negotiation_info() {
  require_once DRUPAL_ROOT . '/includes/locale.inc';
  $file = 'includes/locale.inc';
  $providers = array();

  $providers[LOCALE_LANGUAGE_NEGOTIATION_URL] = array(
    'types' => array(LANGUAGE_TYPE_CONTENT, LANGUAGE_TYPE_INTERFACE, LANGUAGE_TYPE_URL),
    'callbacks' => array(
      'language' => 'locale_language_from_url',
      'switcher' => 'locale_language_switcher_url',
      'url_rewrite' => 'locale_language_url_rewrite_url',
    ),
    'file' => $file,
    'weight' => -8,
    'name' => t('URL'),
    'description' => t('Determine the language from the URL (Path prefix or domain).'),
    'config' => 'admin/config/regional/language/configure/url',
  );

  $providers[LOCALE_LANGUAGE_NEGOTIATION_SESSION] = array(
    'callbacks' => array(
      'language' => 'locale_language_from_session',
      'switcher' => 'locale_language_switcher_session',
      'url_rewrite' => 'locale_language_url_rewrite_session',
    ),
    'file' => $file,
    'weight' => -6,
    'name' => t('Session'),
    'description' => t('Determine the language from a request/session parameter.'),
    'config' => 'admin/config/regional/language/configure/session',
  );

  $providers[LOCALE_LANGUAGE_NEGOTIATION_USER] = array(
    'callbacks' => array('language' => 'locale_language_from_user'),
    'file' => $file,
    'weight' => -4,
    'name' => t('User'),
    'description' => t("Follow the user's language preference."),
  );

  $providers[LOCALE_LANGUAGE_NEGOTIATION_BROWSER] = array(
    'callbacks' => array('language' => 'locale_language_from_browser'),
    'file' => $file,
    'weight' => -2,
    'cache' => 0,
    'name' => t('Browser'),
    'description' => t("Determine the language from the browser's language settings."),
  );

  $providers[LOCALE_LANGUAGE_NEGOTIATION_INTERFACE] = array(
    'types' => array(LANGUAGE_TYPE_CONTENT),
    'callbacks' => array('language' => 'locale_language_from_interface'),
    'file' => $file,
    'weight' => 8,
    'name' => t('Interface'),
    'description' => t('Use the detected interface language.'),
  );

  $providers[LOCALE_LANGUAGE_NEGOTIATION_URL_FALLBACK] = array(
    'types' => array(LANGUAGE_TYPE_URL),
    'callbacks' => array('language' => 'locale_language_url_fallback'),
    'file' => $file,
    'weight' => 8,
    'name' => t('URL fallback'),
    'description' => t('Use an already detected language for URLs if none is found.'),
  );

  return $providers;
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
