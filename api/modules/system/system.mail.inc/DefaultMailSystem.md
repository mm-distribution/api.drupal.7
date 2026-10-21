# DefaultMailSystem

- **Type:** Class
- **File:** [`modules/system/system.mail.inc`](_file.md), lines 11–149 · [local source](../../../../source/modules/system/system.mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc#L11-L149)
- **Module/theme:** system

## Signature

```php
class DefaultMailSystem implements MailSystemInterface
```

## Documentation

```text
The default Drupal mail backend using PHP's mail function.
```

## Methods (derived index)

- [format()](DefaultMailSystem/format.md) — Concatenate and wrap the e-mail body for plain-text mails.
- [mail()](DefaultMailSystem/mail.md) — Send an e-mail message, using Drupal variables and default settings.
- [_isShellSafe()](DefaultMailSystem/_isShellSafe.md) — Disallows potentially unsafe shell characters.

---
_Drupal 7.103 · [modules/system/system.mail.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
