# form_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 11–258 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L11-L258)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function form_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function form_test_menu() {
  $items['form-test/alter'] = array(
    'title' => 'Form altering test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_alter_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['form-test/validate'] = array(
    'title' => 'Form validation handlers test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_validate_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['form-test/validate-required'] = array(
    'title' => 'Form #required validation',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_validate_required_form'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['form-test/validate-required-no-title'] = array(
    'title' => 'Form #required validation without #title',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_validate_required_form_no_title'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['form-test/validate-no-token'] = array(
    'title' => 'Form validation without a CSRF token',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_validate_no_token'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['form-test/limit-validation-errors'] = array(
    'title' => 'Form validation with some error suppression',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_limit_validation_errors_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/tableselect/multiple-true'] = array(
    'title' => 'Tableselect checkboxes test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_tableselect_multiple_true_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['form_test/tableselect/multiple-false'] = array(
    'title' => 'Tableselect radio button test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_tableselect_multiple_false_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['form_test/tableselect/empty-text'] = array(
    'title' => 'Tableselect empty text test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_tableselect_empty_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['form_test/tableselect/advanced-select'] = array(
    'title' => 'Tableselect js_select tests',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_tableselect_js_select_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/vertical-tabs'] = array(
    'title' => 'Vertical tabs tests',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_vertical_tabs_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-storage'] = array(
    'title' => 'Form storage test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_storage_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-storage-legacy'] = array(
    'title' => 'Emulate legacy AHAH-style ajax callback',
    'page callback' => 'form_test_storage_legacy_handler',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-storage-page-cache'] = array(
    'title' => 'Form storage with page cache test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_storage_page_cache_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/wrapper-callback'] = array(
    'title' => 'Form wrapper callback test',
    'page callback' => 'form_test_wrapper_callback',
    'page arguments' => array('form_test_wrapper_callback_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-state-values-clean'] = array(
    'title' => 'Form state values clearance test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_form_state_values_clean_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-state-values-clean-advanced'] = array(
    'title' => 'Form state values clearance advanced test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_form_state_values_clean_advanced_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form-test/checkbox'] = array(
    'title' => t('Form test'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_checkbox'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['form-test/select'] = array(
    'title' => t('Select'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_select'),
    'access callback' => TRUE,
  );
  $items['form-test/checkboxes-radios'] = array(
    'title' => t('Checkboxes, Radios'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_checkboxes_radios'),
    'access callback' => TRUE,
  );

  $items['form-test/disabled-elements'] = array(
    'title' => t('Form test'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_disabled_elements'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['form-test/input-forgery'] = array(
    'title' => t('Form test'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('_form_test_input_forgery'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['form-test/form-rebuild-preserve-values'] = array(
    'title' => 'Form values preservation during rebuild test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_form_rebuild_preserve_values_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form-test/redirect'] = array(
    'title' => 'Redirect test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_redirect'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['form_test/form-labels'] = array(
    'title' => 'Form label test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_label_test_form'),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['form-test/state-persist'] = array(
    'title' => 'Form state persistence without storage',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_state_persist'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['form-test/clicked-button'] = array(
    'title' => 'Clicked button test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_clicked_button'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  if (module_exists('node')) {
    $items['form-test/two-instances-of-same-form'] = array(
      'title' => 'AJAX test with two form instances',
      'page callback' => 'form_test_two_instances',
      'access callback' => 'node_access',
      'access arguments' => array('create', 'page'),
      'file path' => drupal_get_path('module', 'node'),
      'file' => 'node.pages.inc',
      'type' => MENU_CALLBACK,
    );
  }
  $items['form-test/double-form'] = array(
    'title' => 'Double form test',
    'page callback' => 'form_test_double_form',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['form-test/load-include-menu'] = array(
    'title' => 'FAPI test loading includes',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_load_include_menu'),
    'access callback' => TRUE,
    'file' => 'form_test.file.inc',
    'type' => MENU_CALLBACK,
  );

  $items['form-test/load-include-custom'] = array(
    'title' => 'FAPI test loading includes',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_load_include_custom'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['form-test/checkboxes-zero'] = array(
    'title' => 'FAPI test involving checkboxes and zero',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('form_test_checkboxes_zero'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
