# UpgradePathTestCase::refreshVariables()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 199–204 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L199-L204)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function refreshVariables()
```

## Documentation

```text
Specialized refreshVariables().
```

## Code

```php
  protected function refreshVariables() {
    // No operation if the child has not been upgraded yet.
    if (!$this->upgradedSite) {
      return parent::refreshVariables();
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
