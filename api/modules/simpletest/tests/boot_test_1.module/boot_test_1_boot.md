# boot_test_1_boot()

- **Type:** Function
- **File:** [`modules/simpletest/tests/boot_test_1.module`](_file.md), lines 11–21 · [local source](../../../../../source/modules/simpletest/tests/boot_test_1.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot_test_1.module#L11-L21)
- **Module/theme:** batch_test
- **Implements:** [hook_boot()](../../../system/system.api.php/hook_boot.md)

## Signature

```php
function boot_test_1_boot()
```

## Documentation

```text
Implements hook_boot().
```

## Code

```php
function boot_test_1_boot() {
  // Calling module_implements during hook_boot() will return "vital" modules
  // only, and this list of modules will be statically cached.
  module_implements('help');
  // Define a special path to test that the static cache isn't written away
  // if we exit before having completed the bootstrap.
  if ($_GET['q'] == 'early_exit') {
    module_implements_write_cache();
    exit();
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/boot_test_1.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/boot_test_1.module) · Licensed GPL-2.0-or-later (see LICENSE)._
