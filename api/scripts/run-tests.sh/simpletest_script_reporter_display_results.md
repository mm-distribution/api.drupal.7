# simpletest_script_reporter_display_results()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 744–770 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L744-L770)

## Signature

```php
function simpletest_script_reporter_display_results()
```

## Documentation

```text
Display test results.
```

## Code

```php
function simpletest_script_reporter_display_results() {
  global $args, $test_id, $results_map;

  if ($args['verbose']) {
    // Report results.
    echo "Detailed test results\n";
    echo "---------------------\n";

    $results = db_query("SELECT * FROM {simpletest} WHERE test_id = :test_id ORDER BY test_class, message_id", array(':test_id' => $test_id));
    $test_class = '';
    foreach ($results as $result) {
      if (isset($results_map[$result->status]) && (!$args['fail-only'] || $result->status !== 'pass')) {
        if ($result->test_class != $test_class) {
          // Display test class every time results are for new test class.
          echo "\n\n---- $result->test_class ----\n\n\n";
          $test_class = $result->test_class;

          // Print table header.
          echo "Status    Group      Filename          Line Function                            \n";
          echo "--------------------------------------------------------------------------------\n";
        }

        simpletest_script_format_result($result);
      }
    }
  }
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
