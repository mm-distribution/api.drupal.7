# locale_language_from_browser()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 131–202 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L131-L202)
- **Topics:** [locale-languages-negotiation](../../topics/locale-languages-negotiation.md)

## Signature

```php
function locale_language_from_browser($languages)
```

## Documentation

```text
Identify language from the Accept-language HTTP header we got.

We perform browser accept-language parsing only if page cache is disabled,
otherwise we would cache a user-specific preference.

@param $languages
  An array of language objects for enabled languages ordered by weight.

@return
  A valid language code on success, FALSE otherwise.
```

## Code

```php
function locale_language_from_browser($languages) {
  if (empty($_SERVER['HTTP_ACCEPT_LANGUAGE'])) {
    return FALSE;
  }

  // The Accept-Language header contains information about the language
  // preferences configured in the user's browser / operating system.
  // RFC 2616 (section 14.4) defines the Accept-Language header as follows:
  //   Accept-Language = "Accept-Language" ":"
  //                  1#( language-range [ ";" "q" "=" qvalue ] )
  //   language-range  = ( ( 1*8ALPHA *( "-" 1*8ALPHA ) ) | "*" )
  // Samples: "hu, en-us;q=0.66, en;q=0.33", "hu,en-us;q=0.5"
  $browser_langcodes = array();
  if (preg_match_all('@(?<=[, ]|^)([a-zA-Z-]+|\*)(?:;q=([0-9.]+))?(?:$|\s*,\s*)@', trim($_SERVER['HTTP_ACCEPT_LANGUAGE']), $matches, PREG_SET_ORDER)) {
    foreach ($matches as $match) {
      // We can safely use strtolower() here, tags are ASCII.
      // RFC2616 mandates that the decimal part is no more than three digits,
      // so we multiply the qvalue by 1000 to avoid floating point comparisons.
      $langcode = strtolower($match[1]);
      $qvalue = isset($match[2]) ? (float) $match[2] : 1;
      $browser_langcodes[$langcode] = (int) ($qvalue * 1000);
    }
  }

  // We should take pristine values from the HTTP headers, but Internet Explorer
  // from version 7 sends only specific language tags (eg. fr-CA) without the
  // corresponding generic tag (fr) unless explicitly configured. In that case,
  // we assume that the lowest value of the specific tags is the value of the
  // generic language to be as close to the HTTP 1.1 spec as possible.
  // See http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4 and
  // http://blogs.msdn.com/b/ie/archive/2006/10/17/accept-language-header-for-internet-explorer-7.aspx
  asort($browser_langcodes);
  foreach ($browser_langcodes as $langcode => $qvalue) {
    $generic_tag = strtok($langcode, '-');
    if (!isset($browser_langcodes[$generic_tag])) {
      $browser_langcodes[$generic_tag] = $qvalue;
    }
  }

  // Find the enabled language with the greatest qvalue, following the rules
  // of RFC 2616 (section 14.4). If several languages have the same qvalue,
  // prefer the one with the greatest weight.
  $best_match_langcode = FALSE;
  $max_qvalue = 0;
  foreach ($languages as $langcode => $language) {
    // Language tags are case insensitive (RFC2616, sec 3.10).
    $langcode = strtolower($langcode);

    // If nothing matches below, the default qvalue is the one of the wildcard
    // language, if set, or is 0 (which will never match).
    $qvalue = isset($browser_langcodes['*']) ? $browser_langcodes['*'] : 0;

    // Find the longest possible prefix of the browser-supplied language
    // ('the language-range') that matches this site language ('the language tag').
    $prefix = $langcode;
    do {
      if (isset($browser_langcodes[$prefix])) {
        $qvalue = $browser_langcodes[$prefix];
        break;
      }
    }
    while ($prefix = substr($prefix, 0, strrpos($prefix, '-')));

    // Find the best match.
    if ($qvalue > $max_qvalue) {
      $best_match_langcode = $language->language;
      $max_qvalue = $qvalue;
    }
  }

  return $best_match_langcode;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
