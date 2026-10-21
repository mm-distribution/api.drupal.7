# _file_test_log_call()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 217–221 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L217-L221)
- **Module/theme:** batch_test

## Signature

```php
function _file_test_log_call($op, $args)
```

## Documentation

```text
Store the values passed to a hook invocation.

@param $op
  One of the hook_file_* operations: 'load', 'validate', 'download',
  'insert', 'update', 'copy', 'move', 'delete'.
@param $args
  Values passed to hook.

@see file_test_get_calls()
@see file_test_reset()
```

## Code

```php
function _file_test_log_call($op, $args) {
  $results = variable_get('file_test_results', array());
  $results[$op][] = $args;
  variable_set('file_test_results', $results);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
