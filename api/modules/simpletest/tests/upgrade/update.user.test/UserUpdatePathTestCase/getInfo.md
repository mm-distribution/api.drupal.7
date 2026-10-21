# UserUpdatePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.user.test`](../_file.md), lines 12–18 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test#L12-L18)
- **Class:** [UserUpdatePathTestCase](../UserUpdatePathTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'User update path',
      'description' => 'User update path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
