# file_test_set_return()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 251–255 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L251-L255)
- **Module/theme:** batch_test

## Signature

```php
function file_test_set_return($op, $value)
```

## Documentation

```text
Assign a return value for a given operation.

@param $op
  One of the hook_file_[validate,download] operations.
@param $value
  Value for the hook to return.

@see _file_test_get_return()
@see file_test_reset()
```

## Code

```php
function file_test_set_return($op, $value) {
  $return = variable_get('file_test_return', array());
  $return[$op] = $value;
  variable_set('file_test_return', $return);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
