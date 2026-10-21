# TestingMailSystem::mail()

- **Type:** Method
- **File:** [`modules/system/system.mail.inc`](../_file.md), lines 163–168 · [local source](../../../../../source/modules/system/system.mail.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc#L163-L168)
- **Class:** [TestingMailSystem](../TestingMailSystem.md)
- **Module/theme:** system

## Signature

```php
public function mail(array $message)
```

## Documentation

```text
Accept an e-mail message and store it in a variable.

@param $message
  An e-mail message.
```

## Code

```php
  public function mail(array $message) {
    $captured_emails = variable_get('drupal_test_email_collector', array());
    $captured_emails[] = $message;
    variable_set('drupal_test_email_collector', $captured_emails);
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/system/system.mail.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.mail.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
