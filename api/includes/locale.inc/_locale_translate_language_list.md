# _locale_translate_language_list()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2176–2195 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2176-L2195)
- **Topics:** [locale-api-seek](../../topics/locale-api-seek.md)

## Signature

```php
function _locale_translate_language_list($string, $limit_language)
```

## Documentation

```text
List languages in search result table
```

## Code

```php
function _locale_translate_language_list($string, $limit_language) {
  // Add CSS.
  drupal_add_css(drupal_get_path('module', 'locale') . '/locale.css');

  // Include both translated and not yet translated target languages in the
  // list. The source language is English for built-in strings and the default
  // language for other strings.
  $languages = language_list();
  $default = language_default();
  $omit = $string['group'] == 'default' ? 'en' : $default->language;
  unset($languages[$omit]);
  $output = '';
  foreach ($languages as $langcode => $language) {
    if (!$limit_language || $limit_language == $langcode) {
      $output .= (!empty($string['languages'][$langcode])) ? $langcode . ' ' : "<em class=\"locale-untranslated\">$langcode</em> ";
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
