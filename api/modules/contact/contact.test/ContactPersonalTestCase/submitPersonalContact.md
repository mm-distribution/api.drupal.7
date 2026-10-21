# ContactPersonalTestCase::submitPersonalContact()

- **Type:** Method
- **File:** [`modules/contact/contact.test`](../_file.md), lines 449–455 · [local source](../../../../../source/modules/contact/contact.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test#L449-L455)
- **Class:** [ContactPersonalTestCase](../ContactPersonalTestCase.md)
- **Module/theme:** contact

## Signature

```php
protected function submitPersonalContact($account, array $message = array())
```

## Documentation

```text
Fills out a user's personal contact form and submits it.

@param $account
  A user object of the user being contacted.
@param $message
  An optional array with the form fields being used.
```

## Code

```php
  protected function submitPersonalContact($account, array $message = array()) {
    $message += array(
      'subject' => $this->randomName(16),
      'message' => $this->randomName(64),
    );
    $this->drupalPost('user/' . $account->uid . '/contact', $message, t('Send message'));
  }
```

---
_Drupal 7.103 · [modules/contact/contact.test](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.test) · Licensed GPL-2.0-or-later (see LICENSE)._
