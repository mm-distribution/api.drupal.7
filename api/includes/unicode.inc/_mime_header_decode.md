# _mime_header_decode()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 437–447 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L437-L447)

## Signature

```php
function _mime_header_decode($matches)
```

## Documentation

```text
Decodes encoded header data passed from mime_header_decode().

Callback for preg_replace_callback() within mime_header_decode().

@param $matches
  The array of matches from preg_replace_callback().

@return string
  The mime-decoded string.

@see mime_header_decode()
```

## Code

```php
function _mime_header_decode($matches) {
  // Regexp groups:
  // 1: Character set name
  // 2: Escaping method (Q or B)
  // 3: Encoded data
  $data = ($matches[2] == 'B') ? base64_decode($matches[3]) : str_replace('_', ' ', quoted_printable_decode($matches[3]));
  if (strtolower($matches[1]) != 'utf-8') {
    $data = drupal_convert_to_utf8($data, $matches[1]);
  }
  return $data;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
