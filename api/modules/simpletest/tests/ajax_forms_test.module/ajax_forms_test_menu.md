# ajax_forms_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_forms_test.module`](_file.md), lines 11–38 · [local source](../../../../../source/modules/simpletest/tests/ajax_forms_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module#L11-L38)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function ajax_forms_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function ajax_forms_test_menu() {
  $items = array();
  $items['ajax_forms_test_get_form'] = array(
    'title' => 'AJAX forms simple form test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('ajax_forms_test_simple_form'),
    'access callback' => TRUE,
  );
  $items['ajax_forms_test_ajax_commands_form'] = array(
    'title' => 'AJAX forms AJAX commands test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('ajax_forms_test_ajax_commands_form'),
    'access callback' => TRUE,
  );
  $items['ajax_validation_test'] = array(
    'title' => 'AJAX Validation Test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('ajax_forms_test_validation_form'),
    'access callback' => TRUE,
  );
  $items['ajax_forms_test_lazy_load_form'] = array(
    'title' => 'AJAX forms lazy load test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('ajax_forms_test_lazy_load_form'),
    'access callback' => TRUE,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_forms_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_forms_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
