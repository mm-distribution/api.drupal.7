# ContactSitewideTestCase::submitContact()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 264–272 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L264-L272)
- **Class:** [ContactSitewideTestCase](../ContactSitewideTestCase.md)
- **Module/theme:** contact

## Signature

```php
function submitContact($name, $mail, $subject, $cid, $message)
```

## Documentation

```text
Submits the contact form.

@param string $name
  The name of the sender.
@param string $mail
  The e-mail address of the sender.
@param string $subject
  The subject of the message.
@param integer $cid
  The category ID of the message.
@param string $message
  The message body.
```

## Code

```php
  function submitContact($name, $mail, $subject, $cid, $message) {
    $edit = array();
    $edit['name'] = $name;
    $edit['mail'] = $mail;
    $edit['subject'] = $subject;
    $edit['cid'] = $cid;
    $edit['message'] = $message;
    $this->drupalPost('contact', $edit, t('Send message'));
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
