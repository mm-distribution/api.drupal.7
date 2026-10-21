# drupal_truncate_bytes()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 274–285 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L274-L285)

## Signature

```php
function drupal_truncate_bytes($string, $len)
```

## Documentation

```text
Truncates a UTF-8-encoded string safely to a number of bytes.

If the end position is in the middle of a UTF-8 sequence, it scans backwards
until the beginning of the byte sequence.

Use this function whenever you want to chop off a string at an unsure
location. On the other hand, if you're sure that you're splitting on a
character boundary (e.g. after using strpos() or similar), you can safely
use substr() instead.

@param $string
  The string to truncate.
@param $len
  An upper limit on the returned string length.

@return
  The truncated string.
```

## Code

```php
function drupal_truncate_bytes($string, $len) {
  if (strlen($string) <= $len) {
    return $string;
  }
  if ((ord($string[$len]) < 0x80) || (ord($string[$len]) >= 0xC0)) {
    return substr($string, 0, $len);
  }
  // Scan backwards to beginning of the byte sequence.
  while (--$len >= 0 && ord($string[$len]) >= 0x80 && ord($string[$len]) < 0xC0);

  return substr($string, 0, $len);
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
