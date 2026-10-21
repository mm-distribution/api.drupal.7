# update_script_test_flush_caches()

- **Type:** Function
- **File:** [`modules/simpletest/tests/update_script_test.module`](_file.md), lines 16–18 · [local source](../../../../../source/modules/simpletest/tests/update_script_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_script_test.module#L16-L18)
- **Module/theme:** batch_test
- **Implements:** [hook_flush_caches()](../../../system/system.api.php/hook_flush_caches.md)

## Signature

```php
function update_script_test_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().

This sets a message to confirm that all caches are cleared whenever
update.php completes.

@see UpdateScriptFunctionalTest::testRequirements()
```

## Code

```php
function update_script_test_flush_caches() {
  drupal_set_message(t('hook_flush_caches() invoked for update_script_test.module.'));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/update_script_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_script_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
