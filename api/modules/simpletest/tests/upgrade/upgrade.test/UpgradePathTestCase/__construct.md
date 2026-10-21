# UpgradePathTestCase::__construct()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 52–57 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L52-L57)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function __construct($test_id = NULL)
```

## Documentation

```text
Constructs an UpgradePathTestCase object.

@param $test_id
  (optional) The ID of the test. Tests with the same id are reported
  together.
```

## Code

```php
  function __construct($test_id = NULL) {
    parent::__construct($test_id);
    $connection_info = Database::getConnectionInfo();
    $this->skipUpgradeTest = (bool) ($connection_info['default']['driver'] == 'pgsql');
    $this->zlibInstalled = function_exists('gzopen');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
