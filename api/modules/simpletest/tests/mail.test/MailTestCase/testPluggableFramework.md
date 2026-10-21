# MailTestCase::testPluggableFramework()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 34–42 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L34-L42)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPluggableFramework()
```

## Documentation

```text
Assert that the pluggable mail system is functional.
```

## Code

```php
  function testPluggableFramework() {
    global $language;

    // Use MailTestCase for sending a message.
    $message = drupal_mail('simpletest', 'mail_test', 'testing@example.com', $language);

    // Assert whether the message was sent through the send function.
    $this->assertEqual(self::$sent_message['to'], 'testing@example.com', 'Pluggable mail system is extendable.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
