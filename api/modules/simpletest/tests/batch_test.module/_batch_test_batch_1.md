# _batch_test_batch_1()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 353–368 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L353-L368)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_batch_1()
```

## Documentation

```text
Batch 1: repeats a simple operation.

Operations: op 1 from 1 to 10.
```

## Code

```php
function _batch_test_batch_1() {
  // Ensure the batch takes at least two iterations.
  $total = 10;
  $sleep = (1000000 / $total) * 2;

  $operations = array();
  for ($i = 1; $i <= $total; $i++) {
    $operations[] = array('_batch_test_callback_1', array($i, $sleep));
  }
  $batch = array(
    'operations' => $operations,
    'finished' => '_batch_test_finished_1',
    'file' => drupal_get_path('module', 'batch_test'). '/batch_test.callbacks.inc',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
