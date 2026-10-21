# file_test_get_calls()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 188–191 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L188-L191)
- **Module/theme:** batch_test

## Signature

```php
function file_test_get_calls($op)
```

## Documentation

```text
Get the arguments passed to invocation of a given hook since
file_test_reset() was last called.

@param $op
  One of the hook_file_* operations: 'load', 'validate', 'download',
  'insert', 'update', 'copy', 'move', 'delete'.

@return
  Array of the parameters passed to each call.

@see _file_test_log_call()
@see file_test_reset()
```

## Code

```php
function file_test_get_calls($op) {
  $results = variable_get('file_test_results', array());
  return $results[$op];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
