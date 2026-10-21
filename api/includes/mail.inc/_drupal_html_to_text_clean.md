# _drupal_html_to_text_clean()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 664–666 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L664-L666)

## Signature

```php
function _drupal_html_to_text_clean($indent)
```

## Documentation

```text
Replaces non-quotation markers from a given piece of indentation with spaces.

Callback for array_map() within drupal_html_to_text().
```

## Code

```php
function _drupal_html_to_text_clean($indent) {
  return preg_replace('/[^>]/', ' ', $indent);
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
