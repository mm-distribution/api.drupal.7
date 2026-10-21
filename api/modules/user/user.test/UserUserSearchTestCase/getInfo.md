# UserUserSearchTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2739–2745 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2739-L2745)
- **Class:** [UserUserSearchTestCase](../UserUserSearchTestCase.md)
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
      'name' => 'User search',
      'description' => 'Tests the user search page and verifies that sensitive information is hidden from unauthorized users.',
      'group' => 'User',
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
