# UserPasswordResetTestCase::getResetURL()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 540–548 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L540-L548)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
public function getResetURL($bypass_form = FALSE)
```

## Documentation

```text
Retrieves password reset email and extracts the login link.
```

## Code

```php
  public function getResetURL($bypass_form = FALSE) {
    // Assume the most recent email.
    $_emails = $this->drupalGetMails();
    $email = end($_emails);
    $urls = array();
    preg_match('#.+user/reset/.+#', $email['body'], $urls);

    return $urls[0] . ($bypass_form ? '/login' : '');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
