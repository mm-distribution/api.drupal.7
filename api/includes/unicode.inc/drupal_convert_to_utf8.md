# drupal_convert_to_utf8()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 237–253 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L237-L253)

## Signature

```php
function drupal_convert_to_utf8($data, $encoding)
```

## Documentation

```text
Converts data to UTF-8.

Requires the iconv, GNU recode or mbstring PHP extension.

@param $data
  The data to be converted.
@param $encoding
  The encoding that the data is in.

@return
  Converted data or FALSE.
```

## Code

```php
function drupal_convert_to_utf8($data, $encoding) {
  if (function_exists('iconv')) {
    $out = @iconv($encoding, 'utf-8', $data);
  }
  elseif (function_exists('mb_convert_encoding')) {
    $out = @mb_convert_encoding($data, 'utf-8', $encoding);
  }
  elseif (function_exists('recode_string')) {
    $out = @recode_string($encoding . '..utf-8', $data);
  }
  else {
    watchdog('php', 'Unsupported encoding %s. Please install iconv, GNU recode or mbstring for PHP.', array('%s' => $encoding), WATCHDOG_ERROR);
    return FALSE;
  }

  return $out;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
