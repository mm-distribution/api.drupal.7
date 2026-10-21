# user_validate_name()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 631–662 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L631-L662)
- **Module/theme:** user

## Signature

```php
function user_validate_name($name)
```

## Documentation

```text
Verify the syntax of the given name.
```

## Code

```php
function user_validate_name($name) {
  if (!$name) {
    return t('You must enter a username.');
  }
  if (substr($name, 0, 1) == ' ') {
    return t('The username cannot begin with a space.');
  }
  if (substr($name, -1) == ' ') {
    return t('The username cannot end with a space.');
  }
  if (strpos($name, '  ') !== FALSE) {
    return t('The username cannot contain multiple spaces in a row.');
  }
  if (preg_match('/[^\x{80}-\x{F7} a-z0-9@+_.\'-]/i', $name)) {
    return t('The username contains an illegal character.');
  }
  if (preg_match('/[\x{80}-\x{A0}' .         // Non-printable ISO-8859-1 + NBSP
                  '\x{AD}' .                // Soft-hyphen
                  '\x{2000}-\x{200F}' .     // Various space characters
                  '\x{2028}-\x{202F}' .     // Bidirectional text overrides
                  '\x{205F}-\x{206F}' .     // Various text hinting characters
                  '\x{FEFF}' .              // Byte order mark
                  '\x{FF01}-\x{FF60}' .     // Full-width latin
                  '\x{FFF9}-\x{FFFD}' .     // Replacement characters
                  '\x{0}-\x{1F}]/u',        // NULL byte and control characters
                  $name)) {
    return t('The username contains an illegal character.');
  }
  if (drupal_strlen($name) > USERNAME_MAX_LENGTH) {
    return t('The username %name is too long: it must be %max characters or less.', array('%name' => $name, '%max' => USERNAME_MAX_LENGTH));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
