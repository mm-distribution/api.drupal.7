# file_test_get_all_calls()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 201–203 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L201-L203)
- **Module/theme:** batch_test

## Signature

```php
function file_test_get_all_calls()
```

## Documentation

```text
Get an array with the calls for all hooks.

@return
  An array keyed by hook name ('load', 'validate', 'download', 'insert',
  'update', 'copy', 'move', 'delete') with values being arrays of parameters
  passed to each call.
```

## Code

```php
function file_test_get_all_calls() {
  return variable_get('file_test_results', array());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
