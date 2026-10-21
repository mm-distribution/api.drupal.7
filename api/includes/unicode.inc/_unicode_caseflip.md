# _unicode_caseflip()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 554–556 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L554-L556)

## Signature

```php
function _unicode_caseflip($matches)
```

## Documentation

```text
Flips U+C0-U+DE to U+E0-U+FD and back.

@param $matches
  An array of matches.

@return array
  The Latin-1 version of the array of matches.

@see drupal_strtolower()
```

## Code

```php
function _unicode_caseflip($matches) {
  return $matches[0][0] . chr(ord($matches[0][1]) ^ 32);
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
