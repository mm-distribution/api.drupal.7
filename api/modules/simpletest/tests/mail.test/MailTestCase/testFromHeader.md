# MailTestCase::testFromHeader()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 65–91 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L65-L91)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFromHeader()
```

## Documentation

```text
Checks for the site name in an auto-generated From: header.
```

## Code

```php
  function testFromHeader() {
    global $language;
    $default_from = variable_get('site_mail', ini_get('sendmail_from'));
    $site_name = variable_get('site_name', 'Drupal');

    // Reset the class variable holding a copy of the last sent message.
    self::$sent_message = NULL;
    // Send an e-mail with a sender address specified.
    $from_email = 'someone_else@example.com';
    $message = drupal_mail('simpletest', 'from_test', 'from_test@example.com', $language, array(), $from_email);
    // Test that the from e-mail is just the e-mail and not the site name and
    // default sender e-mail.
    $this->assertEqual($from_email, self::$sent_message['headers']['From']);

    // Check default behavior is only email in FROM header.
    self::$sent_message = NULL;
    // Send an e-mail and check that the From-header contains only default mail address.
    variable_del('mail_display_name_site_name');
    $message = drupal_mail('simpletest', 'from_test', 'from_test@example.com', $language);
    $this->assertEqual($default_from, self::$sent_message['headers']['From']);

    self::$sent_message = NULL;
    // Send an e-mail and check that the From-header contains the site name.
    variable_set('mail_display_name_site_name', TRUE);
    $message = drupal_mail('simpletest', 'from_test', 'from_test@example.com', $language);
    $this->assertEqual($site_name . ' <' . $default_from . '>', self::$sent_message['headers']['From']);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
