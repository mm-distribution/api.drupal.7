# OpenIDFunctionalTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 45–51 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L45-L51)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
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
      'name' => 'OpenID discovery and login',
      'description' => "Adds an identity to a user's profile and uses it to log in.",
      'group' => 'OpenID'
    );
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
