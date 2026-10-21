# UpgradePathTriggerTestCase::testTaxonomyUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.trigger.test`](../_file.md), lines 31–41 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test#L31-L41)
- **Class:** [UpgradePathTriggerTestCase](../UpgradePathTriggerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testTaxonomyUpgrade()
```

## Documentation

```text
Basic tests for the trigger upgrade.
```

## Code

```php
  public function testTaxonomyUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
    $this->drupalGet('admin/structure/trigger/node');
    $this->assertRaw('<td>'. t('Make post sticky') .'</td>');
    $this->assertRaw('<td>'. t('Publish post') .'</td>');
    $this->drupalGet('admin/structure/trigger/comment');
    $this->assertRaw('<td>'. t('Publish comment') .'</td>');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
