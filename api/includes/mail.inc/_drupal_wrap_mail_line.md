# _drupal_wrap_mail_line()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 625–630 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L625-L630)

## Signature

```php
function _drupal_wrap_mail_line(&$line, $key, $values)
```

## Documentation

```text
Wraps words on a single line.

Callback for array_walk() within drupal_wrap_mail().
```

## Code

```php
function _drupal_wrap_mail_line(&$line, $key, $values) {
  // Use soft-breaks only for purely quoted or unindented text.
  $line = wordwrap($line, 77 - $values['length'], $values['soft'] ? "  \n" : "\n");
  // Break really long words at the maximum width allowed.
  $line = wordwrap($line, 996 - $values['length'], $values['soft'] ? " \n" : "\n", TRUE);
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
