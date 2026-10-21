# UserUpgradePathDuplicatedPermissionTestCase::testUserUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.user.test`](../_file.md), lines 95–100 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test#L95-L100)
- **Class:** [UserUpgradePathDuplicatedPermissionTestCase](../UserUpgradePathDuplicatedPermissionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testUserUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  public function testUserUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
