# mime_header_encode()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 389–404 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L389-L404)

## Signature

```php
function mime_header_encode($string)
```

## Documentation

```text
Encodes MIME/HTTP header values that contain incorrectly encoded characters.

For example, mime_header_encode('tést.txt') returns "=?UTF-8?B?dMOpc3QudHh0?=".

See http://www.rfc-editor.org/rfc/rfc2047.txt for more information.

Notes:
- Only encode strings that contain non-ASCII characters.
- We progressively cut-off a chunk with truncate_utf8(). This is to ensure
  each chunk starts and ends on a character boundary.
- Using \n as the chunk separator may cause problems on some systems and may
  have to be changed to \r\n or \r.

@param $string
  The header to encode.

@return string
  The mime-encoded header.

@see mime_header_decode()
```

## Code

```php
function mime_header_encode($string) {
  if (preg_match('/[^\x20-\x7E]/', $string)) {
    $chunk_size = 47; // floor((75 - strlen("=?UTF-8?B??=")) * 0.75);
    $len = strlen($string);
    $output = '';
    while ($len > 0) {
      $chunk = drupal_truncate_bytes($string, $chunk_size);
      $output .= ' =?UTF-8?B?' . base64_encode($chunk) . "?=\n";
      $c = strlen($chunk);
      $string = substr($string, $c);
      $len -= $c;
    }
    return trim($output);
  }
  return $string;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
