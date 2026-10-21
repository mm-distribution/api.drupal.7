# TriggerUpdatePathTestCase::testFilledUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.trigger.test`](../_file.md), lines 34–36 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test#L34-L36)
- **Class:** [TriggerUpdatePathTestCase](../TriggerUpdatePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFilledUpgrade()
```

## Documentation

```text
Tests that the upgrade is successful.
```

## Code

```php
  public function testFilledUpgrade() {
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
