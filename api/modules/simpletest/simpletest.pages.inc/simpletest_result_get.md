# simpletest_result_get()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 390–406 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L390-L406)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_result_get($test_id)
```

## Documentation

```text
Get test results for $test_id.

@param $test_id The test_id to retrieve results of.
@return Array of results grouped by test_class.
```

## Code

```php
function simpletest_result_get($test_id) {
  $results = db_select('simpletest')
    ->fields('simpletest')
    ->condition('test_id', $test_id)
    ->orderBy('test_class')
    ->orderBy('message_id')
    ->execute();

  $test_results = array();
  foreach ($results as $result) {
    if (!isset($test_results[$result->test_class])) {
      $test_results[$result->test_class] = array();
    }
    $test_results[$result->test_class][] = $result;
  }
  return $test_results;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
