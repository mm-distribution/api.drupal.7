# UpgradePathTriggerTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.trigger.test`](../_file.md), lines 11–17 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test#L11-L17)
- **Class:** [UpgradePathTriggerTestCase](../UpgradePathTriggerTestCase.md)
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
      'name'  => 'Trigger upgrade path',
      'description'  => 'Trigger upgrade path tests for Drupal 6.x.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
