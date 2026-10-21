# language_fallback_get_candidates()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 554–576 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L554-L576)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_fallback_get_candidates($type = LANGUAGE_TYPE_CONTENT)
```

## Documentation

```text
Returns the possible fallback languages ordered by language weight.

@param
  (optional) The language type. Defaults to LANGUAGE_TYPE_CONTENT.

@return
  An array of language codes.
```

## Code

```php
function language_fallback_get_candidates($type = LANGUAGE_TYPE_CONTENT) {
  $fallback_candidates = &drupal_static(__FUNCTION__);

  if (!isset($fallback_candidates)) {
    $fallback_candidates = array();

    // Get languages ordered by weight.
    // Use array keys to avoid duplicated entries.
    foreach (language_list('weight') as $languages) {
      foreach ($languages as $language) {
        $fallback_candidates[$language->language] = NULL;
      }
    }

    $fallback_candidates = array_keys($fallback_candidates);
    $fallback_candidates[] = LANGUAGE_NONE;

    // Let other modules hook in and add/change candidates.
    drupal_alter('language_fallback_candidates', $fallback_candidates);
  }

  return $fallback_candidates;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
