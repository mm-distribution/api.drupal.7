# simpletest_run_tests()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 125–154 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L125-L154)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_run_tests($test_list, $reporter = 'drupal')
```

## Documentation

```text
Actually runs tests.

@param $test_list
  List of tests to run.
@param $reporter
  Which reporter to use. Allowed values are: text, xml, html and drupal,
  drupal being the default.
```

## Code

```php
function simpletest_run_tests($test_list, $reporter = 'drupal') {
  $test_id = db_insert('simpletest_test_id')
    ->useDefaults(array('test_id'))
    ->execute();

  // Clear out the previous verbose files.
  file_unmanaged_delete_recursive('public://simpletest/verbose');

  // Get the info for the first test being run.
  $first_test = array_shift($test_list);
  $first_instance = new $first_test();
  array_unshift($test_list, $first_test);
  $info = $first_instance->getInfo();

  $batch = array(
    'title' => t('Running tests'),
    'operations' => array(
      array('_simpletest_batch_operation', array($test_list, $test_id)),
    ),
    'finished' => '_simpletest_batch_finished',
    'progress_message' => '',
    'css' => array(drupal_get_path('module', 'simpletest') . '/simpletest.css'),
    'init_message' => t('Processing test @num of @max - %test.', array('%test' => $info['name'], '@num' => '1', '@max' => count($test_list))),
  );
  batch_set($batch);

  module_invoke_all('test_group_started');

  return $test_id;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
