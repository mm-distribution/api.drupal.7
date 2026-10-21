# DefaultMailSystem::format()

- **Type:** Method
- **File:** [`modules/system/system.mail.inc`](../_file.md), lines 21–27 · [local source](../../../../../source/modules/system/system.mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc#L21-L27)
- **Class:** [DefaultMailSystem](../DefaultMailSystem.md)
- **Module/theme:** system

## Signature

```php
public function format(array $message)
```

## Documentation

```text
Concatenate and wrap the e-mail body for plain-text mails.

@param $message
  A message array, as described in hook_mail_alter().

@return
  The formatted $message.
```

## Code

```php
  public function format(array $message) {
    // Join the body array into one string.
    $message['body'] = implode("\n\n", $message['body']);
    // Convert any HTML to plain-text and wrap the mail body for sending.
    $message['body'] = drupal_html_to_text($message['body']);
    return $message;
  }
```

---
_Drupal 7.103 · [modules/system/system.mail.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
