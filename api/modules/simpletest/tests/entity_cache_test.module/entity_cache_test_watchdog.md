# entity_cache_test_watchdog()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_cache_test.module`](_file.md), lines 20–27 · [local source](../../../../../source/modules/simpletest/tests/entity_cache_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_cache_test.module#L20-L27)
- **Module/theme:** batch_test
- **Implements:** [hook_watchdog()](../../../system/system.api.php/hook_watchdog.md)

## Signature

```php
function entity_cache_test_watchdog($log_entry)
```

## Documentation

```text
Implements hook_watchdog().

This hook is called during module_enable() and since this hook
implementation is invoked, we have to expect that this module and dependent
modules have been properly installed already. So we expect to be able to
retrieve the entity information that has been registered by the required
dependency module.

@see EnableDisableTestCase::testEntityCache()
@see entity_cache_test_dependency_entity_info()
```

## Code

```php
function entity_cache_test_watchdog($log_entry) {
  if ($log_entry['type'] == 'system' && $log_entry['message'] == '%module module installed.') {
    $info = entity_get_info('entity_cache_test');
    // Store the information in a system variable to analyze it later in the
    // test case.
    variable_set('entity_cache_test', $info);
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_cache_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_cache_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
