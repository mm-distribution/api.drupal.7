# _batch_test_finished_0()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.callbacks.inc`](_file.md), lines 116–118 · [local source](../../../../../source/modules/simpletest/tests/batch_test.callbacks.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc#L116-L118)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_finished_0($success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

'finished' callback for batch 0.
```

## Code

```php
function _batch_test_finished_0($success, $results, $operations) {
  _batch_test_finished_helper(0, $success, $results, $operations);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.callbacks.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
