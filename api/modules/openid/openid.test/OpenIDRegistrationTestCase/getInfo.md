# OpenIDRegistrationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 404–410 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L404-L410)
- **Class:** [OpenIDRegistrationTestCase](../OpenIDRegistrationTestCase.md)
- **Module/theme:** openid

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
      'name' => 'OpenID account registration',
      'description' => 'Creates a user account using auto-registration.',
      'group' => 'OpenID'
    );
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
