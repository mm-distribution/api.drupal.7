# filter_xss_bad_protocol()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1769–1781 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1769-L1781)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function filter_xss_bad_protocol($string, $decode = TRUE)
```

## Documentation

```text
Processes an HTML attribute value and strips dangerous protocols from URLs.

@param $string
  The string with the attribute value.
@param $decode
  (deprecated) Whether to decode entities in the $string. Set to FALSE if the
  $string is in plain text, TRUE otherwise. Defaults to TRUE. This parameter
  is deprecated and will be removed in Drupal 8. To process a plain-text URI,
  call drupal_strip_dangerous_protocols() or check_url() instead.

@return
  Cleaned up and HTML-escaped version of $string.
```

## Code

```php
function filter_xss_bad_protocol($string, $decode = TRUE) {
  // Get the plain text representation of the attribute value (i.e. its meaning).
  // @todo Remove the $decode parameter in Drupal 8, and always assume an HTML
  //   string that needs decoding.
  if ($decode) {
    if (!function_exists('decode_entities')) {
      require_once DRUPAL_ROOT . '/includes/unicode.inc';
    }

    $string = decode_entities($string);
  }
  return check_plain(drupal_strip_dangerous_protocols($string));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
