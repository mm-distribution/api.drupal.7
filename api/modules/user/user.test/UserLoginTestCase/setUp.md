# UserLoginTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 333–335 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L333-L335)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('user_session_test', 'user_flood_test');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
