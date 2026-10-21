# FilterFormatUpgradePathTestCase::testFilterFormatUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.filter.test`](../_file.md), lines 30–57 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test#L30-L57)
- **Class:** [FilterFormatUpgradePathTestCase](../FilterFormatUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFilterFormatUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  function testFilterFormatUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    $format = filter_format_load('1');
    $this->assertTrue($format->format == '1', 'Filter format found.');
    $format->format = 'test_filter';
    $format->name = 'Test filter';
    filter_format_save($format);
    $format = filter_format_load('test_filter');
    $this->assertTrue($format->format == 'test_filter', 'Saved a filter format with machine name.');

    $account = user_load(4);
    user_save($account, array('signature_format' => 'test_filter'));
    $account = user_load(4);
    $this->assertTrue($account->signature_format == 'test_filter', 'Signature format changed successfully to a filter format with machine name.');

    $delta = db_insert('block_custom')
      ->fields(array(
        'body' => 'Test block',
        'info' => 'Test block',
        'format' => 'test_filter',
      ))
      ->execute();
    $this->assertTrue($delta > 0, 'Created a custom block using a filter format with machine name.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.filter.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
