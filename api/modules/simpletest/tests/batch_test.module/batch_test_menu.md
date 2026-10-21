# batch_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 11–93 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L11-L93)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function batch_test_menu()
```

## Documentation

```text
Implement hook_menu().
```

## Code

```php
function batch_test_menu() {
  $items = array();

  $items['batch-test'] = array(
    'title' => 'Batch test',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('batch_test_simple_form'),
    'access callback' => TRUE,
  );
  // Simple form: one submit handler, setting a batch.
  $items['batch-test/simple'] = array(
    'title' => 'Simple',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => 0,
  );
  // Multistep form: two steps, each setting a batch.
  $items['batch-test/multistep'] = array(
    'title' => 'Multistep',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('batch_test_multistep_form'),
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 1,
  );
  // Chained form: four submit handlers, several of which set a batch.
  $items['batch-test/chained'] = array(
    'title' => 'Chained',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('batch_test_chained_form'),
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 2,
  );
  // Programmatic form: the page submits the 'Chained' form through
  // drupal_form_submit().
  $items['batch-test/programmatic'] = array(
    'title' => 'Programmatic',
    'page callback' => 'batch_test_programmatic',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 3,
  );
  // No form: fire a batch simply by accessing a page.
  $items['batch-test/no-form'] = array(
    'title' => 'Simple page',
    'page callback' => 'batch_test_no_form',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 4,
  );
  // No form: fire a batch; return > 100% complete
  $items['batch-test/large-percentage'] = array(
    'title' => 'Simple page with batch over 100% complete',
    'page callback' => 'batch_test_large_percentage',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 5,
  );
  // Tests programmatic form submission within a batch operation.
  $items['batch-test/nested-programmatic'] = array(
    'title' => 'Nested programmatic',
    'page callback' => 'batch_test_nested_drupal_form_submit',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 6,
  );
  // Landing page to test redirects.
  $items['batch-test/redirect'] = array(
    'title' => 'Redirect',
    'page callback' => 'batch_test_redirect_page',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
    'weight' => 7,
  );
  // This item lives under 'admin' so that the page uses the admin theme.
  $items['admin/batch-test/test-theme'] = array(
    'page callback' => 'batch_test_theme_batch',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
