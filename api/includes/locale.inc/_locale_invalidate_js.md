# _locale_invalidate_js()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2016–2034 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2016-L2034)
- **Topics:** [locale-api-seek](../../topics/locale-api-seek.md)

## Signature

```php
function _locale_invalidate_js($langcode = NULL)
```

## Documentation

```text
Force the JavaScript translation file(s) to be refreshed.

This function sets a refresh flag for a specified language, or all
languages except English, if none specified. JavaScript translation
files are rebuilt (with locale_update_js_files()) the next time a
request is served in that language.

@param $langcode
  The language code for which the file needs to be refreshed.

@return
  New content of the 'javascript_parsed' variable.
```

## Code

```php
function _locale_invalidate_js($langcode = NULL) {
  $parsed = variable_get('javascript_parsed', array());

  if (empty($langcode)) {
    // Invalidate all languages.
    $languages = language_list();
    unset($languages['en']);
    foreach ($languages as $lcode => $data) {
      $parsed['refresh:' . $lcode] = 'waiting';
    }
  }
  else {
    // Invalidate single language.
    $parsed['refresh:' . $langcode] = 'waiting';
  }

  variable_set('javascript_parsed', $parsed);
  return $parsed;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
