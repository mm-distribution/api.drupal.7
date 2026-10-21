# BasicUpgradePath::testFailedUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 364–372 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L364-L372)
- **Class:** [BasicUpgradePath](../BasicUpgradePath.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFailedUpgrade()
```

## Documentation

```text
Test a failed upgrade, and verify that the failure is reported.
```

## Code

```php
  public function testFailedUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    // Destroy a table that the upgrade process needs.
    db_drop_table('access');
    // Assert that the upgrade fails.
    $this->assertFalse($this->performUpgrade(FALSE) && $this->pendingUpdates, 'A failed upgrade should return messages.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
