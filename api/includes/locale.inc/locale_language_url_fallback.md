# locale_language_url_fallback()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 339–352 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L339-L352)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_url_fallback($language = NULL, $language_type = LANGUAGE_TYPE_INTERFACE)
```

## Documentation

```text
Determines the language to be assigned to URLs when none is detected.

The language negotiation process has a fallback chain that ends with the
default language provider. Each built-in language type has a separate
initialization:
- Interface language, which is the only configurable one, always gets a valid
  value. If no request-specific language is detected, the default language
  will be used.
- Content language merely inherits the interface language by default.
- URL language is detected from the requested URL and will be used to rewrite
  URLs appearing in the page being rendered. If no language can be detected,
  there are two possibilities:
  - If the default language has no configured path prefix or domain, then the
    default language is used. This guarantees that (missing) URL prefixes are
    preserved when navigating through the site.
  - If the default language has a configured path prefix or domain, a
    requested URL having an empty prefix or domain is an anomaly that must be
    fixed. This is done by introducing a prefix or domain in the rendered
    page matching the detected interface language.

@param $languages
  (optional) An array of valid language objects. This is passed by
  language_provider_invoke() to every language provider callback, but it is
  not actually needed here. Defaults to NULL.
@param $language_type
  (optional) The language type to fall back to. Defaults to the interface
  language.

@return
  A valid language code.
```

## Code

```php
function locale_language_url_fallback($language = NULL, $language_type = LANGUAGE_TYPE_INTERFACE) {
  $default = language_default();
  $prefix = (variable_get('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX) == LOCALE_LANGUAGE_NEGOTIATION_URL_PREFIX);

  // If the default language is not configured to convey language information,
  // a missing URL language information indicates that URL language should be
  // the default one, otherwise we fall back to an already detected language.
  if (($prefix && empty($default->prefix)) || (!$prefix && empty($default->domain))) {
    return $default->language;
  }
  else {
    return $GLOBALS[$language_type]->language;
  }
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
