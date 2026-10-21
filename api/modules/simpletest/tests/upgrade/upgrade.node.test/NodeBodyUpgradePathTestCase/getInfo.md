# NodeBodyUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.node.test`](../_file.md), lines 9–15 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test#L9-L15)
- **Class:** [NodeBodyUpgradePathTestCase](../NodeBodyUpgradePathTestCase.md)
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
      'name'  => 'Node body upgrade path',
      'description'  => 'Node body upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.node.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
