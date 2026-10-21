# drupal_placeholder()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3835–3837 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3835-L3837)

## Signature

```php
function drupal_placeholder($text)
```

## Documentation

```text
Formats text for emphasized display in a placeholder inside a sentence.

Used automatically by format_string().

@param $text
  The text to format (plain-text).

@return
  The formatted text (html).
```

## Code

```php
function drupal_placeholder($text) {
  return '<em class="placeholder">' . check_plain($text) . '</em>';
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
