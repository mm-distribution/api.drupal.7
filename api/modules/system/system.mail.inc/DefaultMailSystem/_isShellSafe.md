# DefaultMailSystem::_isShellSafe()

- **Type:** Method
- **File:** [`modules/system/system.mail.inc`](../_file.md), lines 139–147 · [local source](../../../../../source/modules/system/system.mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc#L139-L147)
- **Class:** [DefaultMailSystem](../DefaultMailSystem.md)
- **Module/theme:** system

## Signature

```php
protected static function _isShellSafe($string)
```

## Documentation

```text
Disallows potentially unsafe shell characters.

Functionally similar to PHPMailer::isShellSafe() which resulted from
CVE-2016-10045. Note that escapeshellarg and escapeshellcmd are inadequate
for this purpose.

@param string $string
  The string to be validated.

@return bool
  True if the string is shell-safe.

@see https://github.com/PHPMailer/PHPMailer/issues/924
@see https://github.com/PHPMailer/PHPMailer/blob/v5.2.21/class.phpmailer.php#L1430

@todo Rename to ::isShellSafe() and/or discuss whether this is the correct
  location for this helper.
```

## Code

```php
  protected static function _isShellSafe($string) {
    if (escapeshellcmd($string) !== $string || !in_array(escapeshellarg($string), array("'$string'", "\"$string\""))) {
      return FALSE;
    }
    if (preg_match('/[^a-zA-Z0-9@_\-.]/', $string) !== 0) {
      return FALSE;
    }
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/system/system.mail.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
