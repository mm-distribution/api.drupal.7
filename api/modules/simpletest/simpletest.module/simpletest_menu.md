# simpletest_menu()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 30–61 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L30-L61)
- **Module/theme:** simpletest
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function simpletest_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function simpletest_menu() {
  $items['admin/config/development/testing'] = array(
    'title' => 'Testing',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('simpletest_test_form'),
    'description' => 'Run tests against Drupal core and your active modules. These tests help assure that your site code is working as designed.',
    'access arguments' => array('administer unit tests'),
    'file' => 'simpletest.pages.inc',
    'weight' => -5,
  );
  $items['admin/config/development/testing/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/config/development/testing/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('simpletest_settings_form'),
    'access arguments' => array('administer unit tests'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'simpletest.pages.inc',
  );
  $items['admin/config/development/testing/results/%'] = array(
    'title' => 'Test result',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('simpletest_result_form', 5),
    'description' => 'View result of tests.',
    'access arguments' => array('administer unit tests'),
    'file' => 'simpletest.pages.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
