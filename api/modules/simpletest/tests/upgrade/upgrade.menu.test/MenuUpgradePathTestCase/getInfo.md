# MenuUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.menu.test`](../_file.md), lines 7–13 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.menu.test#L7-L13)
- **Class:** [MenuUpgradePathTestCase](../MenuUpgradePathTestCase.md)
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
      'name'  => 'Menu upgrade path',
      'description'  => 'Menu upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
