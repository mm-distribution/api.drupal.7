# locale_language_types_info()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 545–563 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L545-L563)
- **Module/theme:** locale
- **Implements:** [hook_language_types_info()](../../system/language.api.php/hook_language_types_info.md)

## Signature

```php
function locale_language_types_info()
```

## Documentation

```text
Implements hook_language_types_info().

Defines the three core language types:
- Interface language is the only configurable language type in core. It is
  used by t() as the default language if none is specified.
- Content language is by default non-configurable and inherits the interface
  language negotiated value. It is used by the Field API to determine the
  display language for fields if no explicit value is specified.
- URL language is by default non-configurable and is determined through the
  URL language provider or the URL fallback provider if no language can be
  detected. It is used by l() as the default language if none is specified.
```

## Code

```php
function locale_language_types_info() {
  require_once DRUPAL_ROOT . '/includes/locale.inc';
  return array(
    LANGUAGE_TYPE_INTERFACE => array(
      'name' => t('User interface text'),
      'description' => t('Order of language detection methods for user interface text. If a translation of user interface text is available in the detected language, it will be displayed.'),
    ),
    LANGUAGE_TYPE_CONTENT => array(
      'name' => t('Content'),
      'description' => t('Order of language detection methods for content. If a version of content is available in the detected language, it will be displayed.'),
      'fixed' => array(LOCALE_LANGUAGE_NEGOTIATION_INTERFACE),
    ),
    LANGUAGE_TYPE_URL => array(
      'name' => t('URL'),
      'description' => t('Order of language detection methods for URLs. The detected language will be used as the default when generating URLs for internal links on the site.'),
      'fixed' => array(LOCALE_LANGUAGE_NEGOTIATION_URL, LOCALE_LANGUAGE_NEGOTIATION_URL_FALLBACK),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
