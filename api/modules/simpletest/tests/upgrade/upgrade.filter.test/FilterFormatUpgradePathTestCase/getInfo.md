# FilterFormatUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.filter.test`](../_file.md), lines 11–17 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test#L11-L17)
- **Class:** [FilterFormatUpgradePathTestCase](../FilterFormatUpgradePathTestCase.md)
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
      'name' => 'Filter format upgrade path',
      'description' => 'Verifies that filter formats and references to filter formats are converted properly.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.filter.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
