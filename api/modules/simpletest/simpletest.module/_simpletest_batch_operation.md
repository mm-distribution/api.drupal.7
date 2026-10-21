# _simpletest_batch_operation()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 159–206 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L159-L206)
- **Module/theme:** simpletest

## Signature

```php
function _simpletest_batch_operation($test_list_init, $test_id, &$context)
```

## Documentation

```text
Implements callback_batch_operation().
```

## Code

```php
function _simpletest_batch_operation($test_list_init, $test_id, &$context) {
  simpletest_classloader_register();
  // Get working values.
  if (!isset($context['sandbox']['max'])) {
    // First iteration: initialize working values.
    $test_list = $test_list_init;
    $context['sandbox']['max'] = count($test_list);
    $test_results = array('#pass' => 0, '#fail' => 0, '#exception' => 0, '#debug' => 0);
  }
  else {
    // Nth iteration: get the current values where we last stored them.
    $test_list = $context['sandbox']['tests'];
    $test_results = $context['sandbox']['test_results'];
  }
  $max = $context['sandbox']['max'];

  // Perform the next test.
  $test_class = array_shift($test_list);
  $test = new $test_class($test_id);
  $test->run();
  $size = count($test_list);
  $info = $test->getInfo();

  module_invoke_all('test_finished', $test->results);

  // Gather results and compose the report.
  $test_results[$test_class] = $test->results;
  foreach ($test_results[$test_class] as $key => $value) {
    $test_results[$key] += $value;
  }
  $test_results[$test_class]['#name'] = $info['name'];
  $items = array();
  foreach (element_children($test_results) as $class) {
    array_unshift($items, '<div class="simpletest-' . ($test_results[$class]['#fail'] + $test_results[$class]['#exception'] ? 'fail' : 'pass') . '">' . t('@name: @summary', array('@name' => $test_results[$class]['#name'], '@summary' => _simpletest_format_summary_line($test_results[$class]))) . '</div>');
  }
  $context['message'] = t('Processed test @num of @max - %test.', array('%test' => $info['name'], '@num' => $max - $size, '@max' => $max));
  $context['message'] .= '<div class="simpletest-' . ($test_results['#fail'] + $test_results['#exception'] ? 'fail' : 'pass') . '">Overall results: ' . _simpletest_format_summary_line($test_results) . '</div>';
  $context['message'] .= theme('item_list', array('items' => $items));

  // Save working values for the next iteration.
  $context['sandbox']['tests'] = $test_list;
  $context['sandbox']['test_results'] = $test_results;
  // The test_id is the only thing we need to save for the report page.
  $context['results']['test_id'] = $test_id;

  // Multistep processing: report progress.
  $context['finished'] = 1 - $size / $max;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
