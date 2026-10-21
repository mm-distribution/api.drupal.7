# drupal_json_encode()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5283–5300 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5283-L5300)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_json_encode($var)
```

## Documentation

```text
Converts a PHP variable into its JavaScript equivalent.

We use HTML-safe strings, with several characters escaped.

@see drupal_json_decode()
@see drupal_json_encode_helper()
@ingroup php_wrappers
```

## Code

```php
function drupal_json_encode($var) {
  // The PHP version cannot change within a request.
  static $php530;

  if (!isset($php530)) {
    $php530 = version_compare(PHP_VERSION, '5.3.0', '>=');
  }

  if ($php530) {
    // Encode <, >, ', &, and " using the json_encode() options parameter.
    return json_encode($var, JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_AMP | JSON_HEX_QUOT);
  }

  // json_encode() escapes <, >, ', &, and " using its options parameter, but
  // does not support this parameter prior to PHP 5.3.0.  Use a helper instead.
  include_once DRUPAL_ROOT . '/includes/json-encode.inc';
  return drupal_json_encode_helper($var);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
