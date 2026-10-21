# file_test_file_validate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 272–275 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L272-L275)
- **Module/theme:** batch_test
- **Implements:** [hook_file_validate()](../../../system/system.api.php/hook_file_validate.md)

## Signature

```php
function file_test_file_validate($file)
```

## Documentation

```text
Implements hook_file_validate().
```

## Code

```php
function file_test_file_validate($file) {
  _file_test_log_call('validate', array($file));
  return _file_test_get_return('validate');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
