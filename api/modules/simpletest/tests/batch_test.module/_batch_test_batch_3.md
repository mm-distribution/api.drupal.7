# _batch_test_batch_3()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 400–420 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L400-L420)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_batch_3()
```

## Documentation

```text
Batch 3: both single and multistep operations.

Operations:
- op 1 from 1 to 5,
- op 2 from 1 to 5,
- op 1 from 6 to 10,
- op 2 from 6 to 10.
```

## Code

```php
function _batch_test_batch_3() {
  // Ensure the batch takes at least two iterations.
  $total = 10;
  $sleep = (1000000 / $total) * 2;

  $operations = array();
  for ($i = 1; $i <= round($total / 2); $i++) {
    $operations[] = array('_batch_test_callback_1', array($i, $sleep));
  }
  $operations[] = array('_batch_test_callback_2', array(1, $total / 2, $sleep));
  for ($i = round($total / 2) + 1; $i <= $total; $i++) {
    $operations[] = array('_batch_test_callback_1', array($i, $sleep));
  }
  $operations[] = array('_batch_test_callback_2', array(6, $total / 2, $sleep));
  $batch = array(
    'operations' => $operations,
    'finished' => '_batch_test_finished_3',
    'file' => drupal_get_path('module', 'batch_test') . '/batch_test.callbacks.inc',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
