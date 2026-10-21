# drupal_clean_css_identifier()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3996–4026 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3996-L4026)

## Signature

```php
function drupal_clean_css_identifier($identifier, $filter = array(' ' => '-', '_' => '-', '/' => '-', '[' => '-', ']' => ''))
```

## Documentation

```text
Prepares a string for use as a CSS identifier (element, class, or ID name).

http://www.w3.org/TR/CSS21/syndata.html#characters shows the syntax for valid
CSS identifiers (including element names, classes, and IDs in selectors.)

@param $identifier
  The identifier to clean.
@param $filter
  An array of string replacements to use on the identifier.

@return
  The cleaned identifier.
```

## Code

```php
function drupal_clean_css_identifier($identifier, $filter = array(' ' => '-', '_' => '-', '/' => '-', '[' => '-', ']' => '')) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['allow_css_double_underscores'] = &drupal_static(__FUNCTION__ . ':allow_css_double_underscores');
  }
  $allow_css_double_underscores = &$drupal_static_fast['allow_css_double_underscores'];
  if (!isset($allow_css_double_underscores)) {
    $allow_css_double_underscores = variable_get('allow_css_double_underscores', FALSE);
  }

  // Preserve BEM-style double-underscores depending on custom setting.
  if ($allow_css_double_underscores) {
    $filter['__'] = '__';
  }

  // By default, we filter using Drupal's coding standards.
  $identifier = strtr($identifier, $filter);

  // Valid characters in a CSS identifier are:
  // - the hyphen (U+002D)
  // - a-z (U+0030 - U+0039)
  // - A-Z (U+0041 - U+005A)
  // - the underscore (U+005F)
  // - 0-9 (U+0061 - U+007A)
  // - ISO 10646 characters U+00A1 and higher
  // We strip out any character not in the above list.
  $identifier = preg_replace('/[^\x{002D}\x{0030}-\x{0039}\x{0041}-\x{005A}\x{005F}\x{0061}-\x{007A}\x{00A1}-\x{FFFF}]/u', '', $identifier);

  return $identifier;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
