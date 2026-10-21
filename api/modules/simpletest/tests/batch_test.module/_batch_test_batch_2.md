# _batch_test_batch_2()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 375–389 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L375-L389)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_batch_2()
```

## Documentation

```text
Batch 2: single multistep operation.

Operations: op 2 from 1 to 10.
```

## Code

```php
function _batch_test_batch_2() {
  // Ensure the batch takes at least two iterations.
  $total = 10;
  $sleep = (1000000 / $total) * 2;

  $operations = array(
    array('_batch_test_callback_2', array(1, $total, $sleep)),
  );
  $batch = array(
    'operations' => $operations,
    'finished' => '_batch_test_finished_2',
    'file' => drupal_get_path('module', 'batch_test') . '/batch_test.callbacks.inc',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
