# UserActionsTest::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 3016–3018 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L3016-L3018)
- **Class:** [UserActionsTest](../UserActionsTest.md)
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
    parent::setUp('dblog', 'anonymous_user_unblock_test');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
