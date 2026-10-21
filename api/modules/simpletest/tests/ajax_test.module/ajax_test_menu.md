# ajax_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_test.module`](_file.md), lines 11–32 · [local source](../../../../../source/modules/simpletest/tests/ajax_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module#L11-L32)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function ajax_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function ajax_test_menu() {
  $items['ajax-test/render'] = array(
    'title' => 'ajax_render',
    'page callback' => 'ajax_test_render',
    'delivery callback' => 'ajax_deliver',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['ajax-test/render-error'] = array(
    'title' => 'ajax_render_error',
    'page callback' => 'ajax_test_error',
    'delivery callback' => 'ajax_deliver',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['ajax-test/link'] = array(
    'title' => 'AJAX Link',
    'page callback' => 'ajax_test_link',
    'access callback' => TRUE,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
