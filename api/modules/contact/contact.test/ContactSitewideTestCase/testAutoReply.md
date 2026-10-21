# ContactSitewideTestCase::testAutoReply()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 166–202 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L166-L202)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function testAutoReply()
```

## Documentation

```text
Tests auto-reply on the site-wide contact form.
```

## Code

```php
  function testAutoReply() {
    // Create and login administrative user.
    $admin_user = $this->drupalCreateUser(array('access site-wide contact form', 'administer contact forms', 'administer permissions', 'administer users'));
    $this->drupalLogin($admin_user);

    // Set up three categories, 2 with an auto-reply and one without.
    $foo_autoreply = $this->randomName(40);
    $bar_autoreply = $this->randomName(40);
    $this->addCategory('foo', 'foo@example.com', $foo_autoreply, FALSE);
    $this->addCategory('bar', 'bar@example.com', $bar_autoreply, FALSE);
    $this->addCategory('no_autoreply', 'bar@example.com', '', FALSE);

    // Test the auto-reply for category 'foo'.
    $email = $this->randomName(32) . '@example.com';
    $subject = $this->randomName(64);
    $this->submitContact($this->randomName(16), $email, $subject, 2, $this->randomString(128));

    // We are testing the auto-reply, so there should be one e-mail going to the sender.
    $captured_emails = $this->drupalGetMails(array('id' => 'contact_page_autoreply', 'to' => $email, 'from' => 'foo@example.com'));
    $this->assertEqual(count($captured_emails), 1, 'Auto-reply e-mail was sent to the sender for category "foo".', 'Contact');
    $this->assertEqual($captured_emails[0]['body'], drupal_html_to_text($foo_autoreply), 'Auto-reply e-mail body is correct for category "foo".', 'Contact');

    // Test the auto-reply for category 'bar'.
    $email = $this->randomName(32) . '@example.com';
    $this->submitContact($this->randomName(16), $email, $this->randomString(64), 3, $this->randomString(128));

    // Auto-reply for category 'bar' should result in one auto-reply e-mail to the sender.
    $captured_emails = $this->drupalGetMails(array('id' => 'contact_page_autoreply', 'to' => $email, 'from' => 'bar@example.com'));
    $this->assertEqual(count($captured_emails), 1, 'Auto-reply e-mail was sent to the sender for category "bar".', 'Contact');
    $this->assertEqual($captured_emails[0]['body'], drupal_html_to_text($bar_autoreply), 'Auto-reply e-mail body is correct for category "bar".', 'Contact');

    // Verify that no auto-reply is sent when the auto-reply field is left blank.
    $email = $this->randomName(32) . '@example.com';
    $this->submitContact($this->randomName(16), $email, $this->randomString(64), 4, $this->randomString(128));
    $captured_emails = $this->drupalGetMails(array('id' => 'contact_page_autoreply', 'to' => $email, 'from' => 'no_autoreply@example.com'));
    $this->assertEqual(count($captured_emails), 0, 'No auto-reply e-mail was sent to the sender for category "no-autoreply".', 'Contact');
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
