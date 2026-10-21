# common_test_library_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 243–250 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L243-L250)
- **Module/theme:** batch_test
- **Implements:** [hook_library_alter()](../../../system/system.api.php/hook_library_alter.md)

## Signature

```php
function common_test_library_alter(&$libraries, $module)
```

## Documentation

```text
Implements hook_library_alter().
```

## Code

```php
function common_test_library_alter(&$libraries, $module) {
  if ($module == 'system' && isset($libraries['farbtastic'])) {
    // Change the title of Farbtastic to "Farbtastic: Altered Library".
    $libraries['farbtastic']['title'] = 'Farbtastic: Altered Library';
    // Make Farbtastic depend on jQuery Form to test library dependencies.
    $libraries['farbtastic']['dependencies'][] = array('system', 'form');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
