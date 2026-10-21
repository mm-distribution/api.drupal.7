# theme_test_exit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 99–106 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L99-L106)
- **Module/theme:** batch_test
- **Implements:** [hook_exit()](../../../system/system.api.php/hook_exit.md)

## Signature

```php
function theme_test_exit()
```

## Documentation

```text
Implements hook_exit().
```

## Code

```php
function theme_test_exit() {
  if (arg(0) == 'user') {
    // Register a fake registry loading callback. If it gets called by
    // theme_get_registry(), the registry has not been initialized yet.
    _theme_registry_callback('_theme_test_load_registry', array());
    print theme_get_registry() ? 'registry initialized' : 'registry not initialized';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
