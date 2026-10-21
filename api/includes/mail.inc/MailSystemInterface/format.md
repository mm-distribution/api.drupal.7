# MailSystemInterface::format()

- **Type:** Method
- **File:** [`includes/mail.inc`](../_file.md), lines 313–313 · [local source](../../../../source/includes/mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc#L313)
- **Class:** [MailSystemInterface](../MailSystemInterface.md)

## Signature

```php
public function format(array $message);
```

## Documentation

```text
Format a message composed by drupal_mail() prior sending.

@param $message
  A message array, as described in hook_mail_alter().

@return
  The formatted $message.
```

## Code

```php
   public function format(array $message);
```

---
_Drupal 7.103 · [includes/mail.inc](https://github.com/drupal/drupal/blob/7.103/includes/mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
