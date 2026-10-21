# drupal_substr()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 593–680 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L593-L680)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_substr($text, $start, $length = NULL)
```

## Documentation

```text
Cuts off a piece of a string based on character indices and counts.

Follows the same behavior as PHP's own substr() function. Note that for
cutting off a string at a known character/substring location, the usage of
PHP's normal strpos/substr is safe and much faster.

@param $text
  The input string.
@param $start
  The position at which to start reading.
@param $length
  The number of characters to read.

@return
  The shortened string.

@ingroup php_wrappers
```

## Code

```php
function drupal_substr($text, $start, $length = NULL) {
  global $multibyte;
  $text = (string) $text;
  if ($multibyte == UNICODE_MULTIBYTE) {
    return $length === NULL ? mb_substr($text, $start) : mb_substr($text, $start, $length);
  }
  else {
    $strlen = strlen($text);
    // Find the starting byte offset.
    $bytes = 0;
    if ($start > 0) {
      // Count all the continuation bytes from the start until we have found
      // $start characters or the end of the string.
      $bytes = -1; $chars = -1;
      while ($bytes < $strlen - 1 && $chars < $start) {
        $bytes++;
        $c = ord($text[$bytes]);
        if ($c < 0x80 || $c >= 0xC0) {
          $chars++;
        }
      }
    }
    elseif ($start < 0) {
      // Count all the continuation bytes from the end until we have found
      // abs($start) characters.
      $start = abs($start);
      $bytes = $strlen; $chars = 0;
      while ($bytes > 0 && $chars < $start) {
        $bytes--;
        $c = ord($text[$bytes]);
        if ($c < 0x80 || $c >= 0xC0) {
          $chars++;
        }
      }
    }
    $istart = $bytes;

    // Find the ending byte offset.
    if ($length === NULL) {
      $iend = $strlen;
    }
    elseif ($length > 0) {
      // Count all the continuation bytes from the starting index until we have
      // found $length characters or reached the end of the string, then
      // backtrace one byte.
      $iend = $istart - 1;
      $chars = -1;
      $last_real = FALSE;
      while ($iend < $strlen - 1 && $chars < $length) {
        $iend++;
        $c = ord($text[$iend]);
        $last_real = FALSE;
        if ($c < 0x80 || $c >= 0xC0) {
          $chars++;
          $last_real = TRUE;
        }
      }
      // Backtrace one byte if the last character we found was a real character
      // and we don't need it.
      if ($last_real && $chars >= $length) {
        $iend--;
      }
    }
    elseif ($length < 0) {
      // Count all the continuation bytes from the end until we have found
      // abs($start) characters, then backtrace one byte.
      $length = abs($length);
      $iend = $strlen; $chars = 0;
      while ($iend > 0 && $chars < $length) {
        $iend--;
        $c = ord($text[$iend]);
        if ($c < 0x80 || $c >= 0xC0) {
          $chars++;
        }
      }
      // Backtrace one byte if we are not at the beginning of the string.
      if ($iend > 0) {
        $iend--;
      }
    }
    else {
      // $length == 0, return an empty string.
      return '';
    }

    return substr($text, $istart, max(0, $iend - $istart + 1));
  }
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
