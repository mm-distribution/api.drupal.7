# file_module_test_menu()

- **Type:** Function
- **File:** [`modules/file/tests/file_module_test.module`](_file.md), lines 11–22 · [local source](../../../../../source/modules/file/tests/file_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module#L11-L22)
- **Module/theme:** file_module_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function file_module_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function file_module_test_menu() {
  $items = array();

  $items['file/test'] = array(
    'title' => 'Managed file test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('file_module_test_form'),
    'access arguments' => array('access content'),
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/file/tests/file_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
