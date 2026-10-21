# decode_entities()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 462–464 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L462-L464)

## Signature

```php
function decode_entities($text)
```

## Documentation

```text
Decodes all HTML entities (including numerical ones) to regular UTF-8 bytes.

Double-escaped entities will only be decoded once ("&amp;lt;" becomes "&lt;"
, not "<"). Be careful when using this function, as decode_entities can
revert previous sanitization efforts (&lt;script&gt; will become <script>).

@param $text
  The text to decode entities in.

@return
  The input $text, with all HTML entities decoded once.
```

## Code

```php
function decode_entities($text) {
  return html_entity_decode((string) $text, ENT_QUOTES, 'UTF-8');
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
