# OpenIDTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 666–672 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L666-L672)
- **Class:** [OpenIDTestCase](../OpenIDTestCase.md)
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
      'name' => 'OpenID helper functions',
      'description' => 'Test OpenID helper functions.',
      'group' => 'OpenID'
    );
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
