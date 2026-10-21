# UserTimeZoneFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1862–1868 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1862-L1868)
- **Class:** [UserTimeZoneFunctionalTest](../UserTimeZoneFunctionalTest.md)
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
      'name' => 'User time zones',
      'description' => 'Set a user time zone and verify that dates are displayed in local time.',
      'group' => 'User',
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
