# common_test_cron()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 292–294 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L292-L294)
- **Module/theme:** batch_test
- **Implements:** [hook_cron()](../../../system/system.api.php/hook_cron.md)

## Signature

```php
function common_test_cron()
```

## Documentation

```text
Implements hook_cron().

System module should handle if a module does not catch an exception and keep
cron going.

@see common_test_cron_helper()
```

## Code

```php
function common_test_cron() {
  throw new Exception(t('Uncaught exception'));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
