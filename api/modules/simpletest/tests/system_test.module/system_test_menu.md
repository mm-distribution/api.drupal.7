# system_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 6–163 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L6-L163)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function system_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function system_test_menu() {
  $items['system-test/sleep/%'] = array(
    'page callback' => 'system_test_sleep',
    'page arguments' => array(2),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['system-test/auth'] = array(
    'page callback' => 'system_test_basic_auth_page',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['system-test/authorize-init/%'] = array(
    'page callback' => 'system_test_authorize_init_page',
    'page arguments' => array(2),
    'access arguments' => array('administer software updates'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/redirect/%'] = array(
    'title' => 'Redirect',
    'page callback' => 'system_test_redirect',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/multiple-redirects/%'] = array(
    'title' => 'Redirect',
    'page callback' => 'system_test_multiple_redirects',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/set-header'] = array(
    'page callback' => 'system_test_set_header',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/redirect-noscheme'] = array(
    'page callback' => 'system_test_redirect_noscheme',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/redirect-protocol-relative'] = array(
    'page callback' => 'system_test_redirect_protocol_relative',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/redirect-noparse'] = array(
    'page callback' => 'system_test_redirect_noparse',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );
  $items['system-test/redirect-invalid-scheme'] = array(
    'page callback' => 'system_test_redirect_invalid_scheme',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['system-test/variable-get'] = array(
    'title' => 'Variable Get',
    'page callback' => 'variable_get',
    'page arguments' => array('simpletest_bootstrap_variable_test', NULL),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  $items['system-test/lock-acquire'] = array(
    'title' => 'Lock acquire',
    'page callback' => 'system_test_lock_acquire',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/lock-exit'] = array(
    'title' => 'Lock acquire then exit',
    'page callback' => 'system_test_lock_exit',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/drupal-set-message'] = array(
    'title' => 'Set messages with drupal_set_message()',
    'page callback' => 'system_test_drupal_set_message',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/main-content-handling'] = array(
    'title' => 'Test main content handling',
    'page callback' => 'system_test_main_content_fallback',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/main-content-fallback'] = array(
    'title' => 'Test main content fallback',
    'page callback' => 'system_test_main_content_fallback',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/main-content-duplication'] = array(
    'title' => 'Test main content duplication',
    'page callback' => 'system_test_main_content_fallback',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/shutdown-functions'] = array(
    'title' => 'Test main content duplication',
    'page callback' => 'system_test_page_shutdown_functions',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/get-destination'] = array(
    'title' => 'Test $_GET[\'destination\']',
    'page callback' => 'system_test_get_destination',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/request-destination'] = array(
    'title' => 'Test $_REQUEST[\'destination\']',
    'page callback' => 'system_test_request_destination',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/drupal-get-filename'] = array(
    'title' => 'Test drupal_get_filename()',
    'page callback' => 'system_test_drupal_get_filename',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/drupal-get-filename-with-schema-rebuild'] = array(
    'title' => 'Test drupal_get_filename() with a schema rebuild',
    'page callback' => 'system_test_drupal_get_filename_with_schema_rebuild',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/empty-page'] = array(
    'title' => 'Test page cache with empty page.',
    'page callback' => 'system_test_empty_page',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  $items['system-test/page-cache-headers'] = array(
    'page callback' => 'system_test_page_cache_headers',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
