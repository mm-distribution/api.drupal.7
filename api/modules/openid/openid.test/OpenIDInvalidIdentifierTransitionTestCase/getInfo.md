# OpenIDInvalidIdentifierTransitionTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 584–590 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L584-L590)
- **Class:** [OpenIDInvalidIdentifierTransitionTestCase](../OpenIDInvalidIdentifierTransitionTestCase.md)
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
      'name' => 'OpenID account update',
      'description' => 'Tries to correct OpenID identifiers attached to accounts if their identifiers were stripped.',
      'group' => 'OpenID',
    );
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
