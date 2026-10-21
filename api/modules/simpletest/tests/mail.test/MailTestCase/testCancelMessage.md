# MailTestCase::testCancelMessage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 49–60 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L49-L60)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCancelMessage()
```

## Documentation

```text
Test that message sending may be canceled.

@see simpletest_mail_alter()
```

## Code

```php
  function testCancelMessage() {
    global $language;

    // Reset the class variable holding a copy of the last sent message.
    self::$sent_message = NULL;

    // Send a test message that simpletest_mail_alter should cancel.
    $message = drupal_mail('simpletest', 'cancel_test', 'cancel@example.com', $language);

    // Assert that the message was not actually sent.
    $this->assertNull(self::$sent_message, 'Message was canceled.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
