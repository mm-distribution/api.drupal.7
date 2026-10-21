# _file_test_get_return()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 235–238 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L235-L238)
- **Module/theme:** batch_test

## Signature

```php
function _file_test_get_return($op)
```

## Documentation

```text
Load the appropriate return value.

@param $op
  One of the hook_file_[validate,download] operations.

@return
  Value set by file_test_set_return().

@see file_test_set_return()
@see file_test_reset()
```

## Code

```php
function _file_test_get_return($op) {
  $return = variable_get('file_test_return', array($op => NULL));
  return $return[$op];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
