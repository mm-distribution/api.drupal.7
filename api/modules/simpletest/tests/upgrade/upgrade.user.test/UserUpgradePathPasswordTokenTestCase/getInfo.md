# UserUpgradePathPasswordTokenTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.user.test`](../_file.md), lines 6–12 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test#L6-L12)
- **Class:** [UserUpgradePathPasswordTokenTestCase](../UserUpgradePathPasswordTokenTestCase.md)
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
      'name'  => 'User upgrade path (password token involved)',
      'description'  => 'User upgrade path tests (password token involved).',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
