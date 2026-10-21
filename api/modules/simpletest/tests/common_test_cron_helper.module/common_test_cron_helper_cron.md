# common_test_cron_helper_cron()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test_cron_helper.module`](_file.md), lines 15–17 · [local source](../../../../../source/modules/simpletest/tests/common_test_cron_helper.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test_cron_helper.module#L15-L17)
- **Module/theme:** batch_test
- **Implements:** [hook_cron()](../../../system/system.api.php/hook_cron.md)

## Signature

```php
function common_test_cron_helper_cron()
```

## Documentation

```text
Implements hook_cron().

common_test_cron() throws an exception, but the execution should reach this
function as well.

@see common_test_cron()
```

## Code

```php
function common_test_cron_helper_cron() {
  variable_set('common_test_cron', 'success');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test_cron_helper.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test_cron_helper.module) · Licensed GPL-2.0-or-later (see LICENSE)._
