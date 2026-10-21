# drupal_validate_utf8()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1938–1946 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1938-L1946)

## Signature

```php
function drupal_validate_utf8($text)
```

## Documentation

```text
Checks whether a string is valid UTF-8.

All functions designed to filter input should use drupal_validate_utf8
to ensure they operate on valid UTF-8 strings to prevent bypass of the
filter.

When text containing an invalid UTF-8 lead byte (0xC0 - 0xFF) is presented
as UTF-8 to Internet Explorer 6, the program may misinterpret subsequent
bytes. When these subsequent bytes are HTML control characters such as
quotes or angle brackets, parts of the text that were deemed safe by filters
end up in locations that are potentially unsafe; An onerror attribute that
is outside of a tag, and thus deemed safe by a filter, can be interpreted
by the browser as if it were inside the tag.

The function does not return FALSE for strings containing character codes
above U+10FFFF, even though these are prohibited by RFC 3629.

@param $text
  The text to check.

@return
  TRUE if the text is valid UTF-8, FALSE if not.
```

## Code

```php
function drupal_validate_utf8($text) {
  if (strlen((string) $text) == 0) {
    return TRUE;
  }
  // With the PCRE_UTF8 modifier 'u', preg_match() fails silently on strings
  // containing invalid UTF-8 byte sequences. It does not reject character
  // codes above U+10FFFF (represented by 4 or more octets), though.
  return (preg_match('/^./us', $text) == 1);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
