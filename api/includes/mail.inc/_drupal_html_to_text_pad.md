# _drupal_html_to_text_pad()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 673–683 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L673-L683)

## Signature

```php
function _drupal_html_to_text_pad($text, $pad, $prefix = '')
```

## Documentation

```text
Pads the last line with the given character.

@see drupal_html_to_text()
```

## Code

```php
function _drupal_html_to_text_pad($text, $pad, $prefix = '') {
  // Remove last line break.
  $text = substr($text, 0, -1);
  // Calculate needed padding space and add it.
  if (($p = strrpos($text, "\n")) === FALSE) {
    $p = -1;
  }
  $n = max(0, 79 - (strlen($text) - $p) - strlen($prefix));
  // Add prefix and padding, and restore linebreak.
  return $text . $prefix . str_repeat($pad, $n) . "\n";
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
