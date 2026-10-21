# mime_header_decode()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 417–422 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L417-L422)

## Signature

```php
function mime_header_decode($header)
```

## Documentation

```text
Decodes MIME/HTTP encoded header values.

@param $header
  The header to decode.

@return string
  The mime-decoded header.

@see mime_header_encode()
```

## Code

```php
function mime_header_decode($header) {
  // First step: encoded chunks followed by other encoded chunks (need to collapse whitespace)
  $header = preg_replace_callback('/=\?([^?]+)\?(Q|B)\?([^?]+|\?(?!=))\?=\s+(?==\?)/', '_mime_header_decode', $header);
  // Second step: remaining chunks (do not collapse whitespace)
  return preg_replace_callback('/=\?([^?]+)\?(Q|B)\?([^?]+|\?(?!=))\?=/', '_mime_header_decode', $header);
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
