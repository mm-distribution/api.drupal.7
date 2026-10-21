# UserValidationTestCase::testAlteredMailValidation()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 310–318 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L310-L318)
- **Class:** [UserValidationTestCase](../UserValidationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testAlteredMailValidation()
```

## Documentation

_No docblock in source._

## Code

```php
  function testAlteredMailValidation() {
    // This e-mail is considered as valid.
    $mail = 'foo@example.local';
    $this->assertNull(user_validate_mail($mail), 'E-mail address is valid.');

    // Invalidate all emails ending with .local in alter hook.
    module_enable(array('user_email_validation_test'));
    $this->assertNotNull(user_validate_mail($mail), 'E-mail address is invalid.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
