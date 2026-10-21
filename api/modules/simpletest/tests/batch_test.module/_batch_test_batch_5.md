# _batch_test_batch_5()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 456–471 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L456-L471)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_batch_5()
```

## Documentation

```text
Batch 5: repeats a simple operation.

Operations: op 1 from 1 to 10.
```

## Code

```php
function _batch_test_batch_5() {
  // Ensure the batch takes at least two iterations.
  $total = 10;
  $sleep = (1000000 / $total) * 2;

  $operations = array();
  for ($i = 1; $i <= $total; $i++) {
    $operations[] = array('_batch_test_callback_5', array($i, $sleep));
  }
  $batch = array(
    'operations' => $operations,
    'finished' => '_batch_test_finished_5',
    'file' => drupal_get_path('module', 'batch_test'). '/batch_test.callbacks.inc',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
