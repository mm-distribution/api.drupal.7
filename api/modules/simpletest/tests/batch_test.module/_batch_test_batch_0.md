# _batch_test_batch_0()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 339–346 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L339-L346)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_batch_0()
```

## Documentation

```text
Batch 0: no operation.
```

## Code

```php
function _batch_test_batch_0() {
  $batch = array(
    'operations' => array(),
    'finished' => '_batch_test_finished_0',
    'file' => drupal_get_path('module', 'batch_test'). '/batch_test.callbacks.inc',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
