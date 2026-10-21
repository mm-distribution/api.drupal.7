# drupal_mail_format_display_name()

- **Type:** Function
- **File:** [`includes/mail.inc`](_file.md), lines 587–618 · [local source](../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L587-L618)

## Signature

```php
function drupal_mail_format_display_name($string)
```

## Documentation

```text
Return a RFC-2822 compliant "display-name" component.

The "display-name" component is used in mail header "Originator" fields
(From, Sender, Reply-to) to give a human-friendly description of the
address, i.e. From: My Display Name <xyz@example.org>. RFC-822 and
RFC-2822 define its syntax and rules. This method gets as input a string
to be used as "display-name" and formats it to be RFC compliant.

@param string $string
  A string to be used as "display-name".

@return string
  A RFC compliant version of the string, ready to be used as
  "display-name" in mail originator header fields.
```

## Code

```php
function drupal_mail_format_display_name($string) {
  // Make sure we don't process html-encoded characters. They may create
  // unneeded trouble if left encoded, besides they will be correctly
  // processed if decoded.
  $string = decode_entities($string);

  // If string contains non-ASCII characters it must be (short) encoded
  // according to RFC-2047. The output of a "B" (Base64) encoded-word is
  // always safe to be used as display-name.
  $safe_display_name = mime_header_encode($string, TRUE);

  // Encoded-words are always safe to be used as display-name because don't
  // contain any RFC 2822 "specials" characters. However
  // mimeHeaderEncode() encodes a string only if it contains any
  // non-ASCII characters, and leaves its value untouched (un-encoded) if
  // ASCII only. For this reason in order to produce a valid display-name we
  // still need to make sure there are no "specials" characters left.
  if (preg_match('/[' . preg_quote(MAIL_RFC_2822_SPECIALS) . ']/', $safe_display_name)) {

    // If string is already quoted, it may or may not be escaped properly, so
    // don't trust it and reset.
    if (preg_match('/^"(.+)"$/', $safe_display_name, $matches)) {
      $safe_display_name = str_replace(array('\\\\', '\\"'), array('\\', '"'), $matches[1]);
    }

    // Transform the string in a RFC-2822 "quoted-string" by wrapping it in
    // double-quotes. Also make sure '"' and '\' occurrences are escaped.
    $safe_display_name = '"' . str_replace(array('\\', '"'), array('\\\\', '\\"'), $safe_display_name) . '"';
  }

  return $safe_display_name;
}
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
