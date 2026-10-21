# file_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 19–28 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L19-L28)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function file_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function file_test_menu() {
  $items['file-test/upload'] = array(
    'title' => 'Upload test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_file_test_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
