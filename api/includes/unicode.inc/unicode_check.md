# unicode_check()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 88–90 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L88-L90)

## Signature

```php
function unicode_check()
```

## Documentation

```text
Wrapper around _unicode_check().
```

## Code

```php
function unicode_check() {
  list($GLOBALS['multibyte']) = _unicode_check();
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
