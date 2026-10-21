# _batch_test_finished_helper()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.callbacks.inc`](_file.md), lines 91–109 · [local source](../../../../../source/modules/simpletest/tests/batch_test.callbacks.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc#L91-L109)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_finished_helper($batch_id, $success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

Common 'finished' callbacks for batches 1 to 4.
```

## Code

```php
function _batch_test_finished_helper($batch_id, $success, $results, $operations) {
  $messages = array("results for batch $batch_id");
  if ($results) {
    foreach ($results as $op => $op_results) {
      $messages[] = 'op '. $op . ': processed ' . count($op_results) . ' elements';
    }
  }
  else {
    $messages[] = 'none';
  }

  if (!$success) {
    // A fatal error occurred during the processing.
    $error_operation = reset($operations);
    $messages[] = t('An error occurred while processing @op with arguments:<br/>@args', array('@op' => $error_operation[0], '@args' => print_r($error_operation[1], TRUE)));
  }

  drupal_set_message(implode('<br />', $messages));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.callbacks.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
