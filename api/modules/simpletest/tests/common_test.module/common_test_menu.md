# common_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 11–62 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L11-L62)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function common_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function common_test_menu() {
  $items['common-test/drupal_goto'] = array(
    'title' => 'Drupal Goto',
    'page callback' => 'common_test_drupal_goto_land',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/drupal_goto/fail'] = array(
    'title' => 'Drupal Goto',
    'page callback' => 'common_test_drupal_goto_land_fail',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/drupal_goto/redirect'] = array(
    'title' => 'Drupal Goto',
    'page callback' => 'common_test_drupal_goto_redirect',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/drupal_goto/redirect_advanced'] = array(
    'title' => 'Drupal Goto',
    'page callback' => 'common_test_drupal_goto_redirect_advanced',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/drupal_goto/redirect_fail'] = array(
    'title' => 'Drupal Goto Failure',
    'page callback' => 'drupal_goto',
    'page arguments' => array('common-test/drupal_goto/fail'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/destination'] = array(
    'title' => 'Drupal Get Destination',
    'page callback' => 'common_test_destination',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/query-string'] = array(
    'title' => 'Test querystring',
    'page callback' => 'common_test_js_and_css_querystring',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['common-test/html_head_link'] = array(
    'title' => 'Test HTML head link',
    'page callback' => 'common_test_html_head_link',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
