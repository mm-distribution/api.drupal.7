# OpenIDInvalidIdentifierTransitionTestCase::setUp()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 592–596 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L592-L596)
- **Class:** [OpenIDInvalidIdentifierTransitionTestCase](../OpenIDInvalidIdentifierTransitionTestCase.md)
- **Module/theme:** openid

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('openid', 'openid_test');
    variable_set('user_register', USER_REGISTER_VISITORS);
    variable_set('openid_less_obtrusive_transition', TRUE);
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
