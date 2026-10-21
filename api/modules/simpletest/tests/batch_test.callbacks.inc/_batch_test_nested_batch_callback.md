# _batch_test_nested_batch_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.callbacks.inc`](_file.md), lines 81–84 · [local source](../../../../../source/modules/simpletest/tests/batch_test.callbacks.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc#L81-L84)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_nested_batch_callback()
```

## Documentation

```text
Implements callback_batch_operation().

Batch operation setting up its own batch.
```

## Code

```php
function _batch_test_nested_batch_callback() {
  batch_test_stack('setting up batch 2');
  batch_set(_batch_test_batch_2());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.callbacks.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
