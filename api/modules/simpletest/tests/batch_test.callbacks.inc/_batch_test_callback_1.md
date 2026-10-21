# _batch_test_callback_1()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.callbacks.inc`](_file.md), lines 14–22 · [local source](../../../../../source/modules/simpletest/tests/batch_test.callbacks.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc#L14-L22)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_callback_1($id, $sleep, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Simple batch operation.
```

## Code

```php
function _batch_test_callback_1($id, $sleep, &$context) {
  // No-op, but ensure the batch take a couple iterations.
  // Batch needs time to run for the test, so sleep a bit.
  usleep($sleep);
  // Track execution, and store some result for post-processing in the
  // 'finished' callback.
  batch_test_stack("op 1 id $id");
  $context['results'][1][] = $id;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.callbacks.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
