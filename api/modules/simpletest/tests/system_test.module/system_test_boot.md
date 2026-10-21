# system_test_boot()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 318–320 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L318-L320)
- **Module/theme:** batch_test
- **Implements:** [hook_boot()](../../../system/system.api.php/hook_boot.md)

## Signature

```php
function system_test_boot()
```

## Documentation

```text
Implements hook_boot().
```

## Code

```php
function system_test_boot() {
  watchdog('system_test', 'hook_boot');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
