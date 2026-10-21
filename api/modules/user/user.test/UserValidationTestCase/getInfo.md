# UserValidationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 259–265 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L259-L265)
- **Class:** [UserValidationTestCase](../UserValidationTestCase.md)
- **Module/theme:** user

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Username/e-mail validation',
      'description' => 'Verify that username/email validity checks behave as designed.',
      'group' => 'User'
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
