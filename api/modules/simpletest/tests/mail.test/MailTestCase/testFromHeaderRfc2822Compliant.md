# MailTestCase::testFromHeaderRfc2822Compliant()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 96–135 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L96-L135)
- **Class:** [MailTestCase](../MailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFromHeaderRfc2822Compliant()
```

## Documentation

```text
Checks for the site name in an auto-generated From: header.
```

## Code

```php
  function testFromHeaderRfc2822Compliant() {
    global $language;
    $default_from = variable_get('site_mail', ini_get('sendmail_from'));

    // Enable adding a site name to From.
    variable_set('mail_display_name_site_name', TRUE);

    $site_names = array(
      // Simple ASCII characters.
      'Test site' => 'Test site',
      // ASCII with html entity.
      'Test &amp; site' => 'Test & site',
      // Non-ASCII characters.
      'Tést site' => '=?UTF-8?B?VMOpc3Qgc2l0ZQ==?=',
      // Non-ASCII with special characters.
      'Tést; site' => '=?UTF-8?B?VMOpc3Q7IHNpdGU=?=',
      // Non-ASCII with html entity.
      'T&eacute;st; site' => '=?UTF-8?B?VMOpc3Q7IHNpdGU=?=',
      // ASCII with special characters.
      'Test; site' => '"Test; site"',
      // ASCII with special characters as html entity.
      'Test &lt; site' => '"Test < site"',
      // ASCII with special characters and '\'.
      'Test; \ "site"' => '"Test; \\\\ \"site\""',
      // String already RFC-2822 compliant.
      '"Test; site"' => '"Test; site"',
      // String already RFC-2822 compliant.
      '"Test; \\\\ \"site\""' => '"Test; \\\\ \"site\""',
    );

    foreach ($site_names as $original_name => $safe_string) {
      variable_set('site_name', $original_name);

      // Reset the class variable holding a copy of the last sent message.
      self::$sent_message = NULL;
      // Send an e-mail and check that the From-header contains is RFC-2822 compliant.
      drupal_mail('simpletest', 'from_test', 'from_test@example.com', $language);
      $this->assertEqual($safe_string . ' <' . $default_from . '>', self::$sent_message['headers']['From']);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
