# OpenIDWebTestCase::getPasswordResetURLFromMail()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 31–36 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L31-L36)
- **Class:** [OpenIDWebTestCase](../OpenIDWebTestCase.md)
- **Module/theme:** openid

## Signature

```php
function getPasswordResetURLFromMail()
```

## Documentation

```text
Parses the last sent e-mail and returns the one-time login link URL.
```

## Code

```php
  function getPasswordResetURLFromMail() {
    $mails = $this->drupalGetMails();
    $mail = end($mails);
    preg_match('@.+user/reset/.+@', $mail['body'], $matches);
    return $matches[0];
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
