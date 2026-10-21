# MailTestCase::format()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 142–150 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L142-L150)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function format(array $message)
```

## Documentation

```text
Concatenate and wrap the e-mail body for plain-text mails.

@see DefaultMailSystem
```

## Code

```php
  public function format(array $message) {
    // Join the body array into one string.
    $message['body'] = implode("\n\n", $message['body']);
    // Convert any HTML to plain-text.
    $message['body'] = drupal_html_to_text($message['body']);
    // Wrap the mail body for sending.
    $message['body'] = drupal_wrap_mail($message['body']);
    return $message;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
