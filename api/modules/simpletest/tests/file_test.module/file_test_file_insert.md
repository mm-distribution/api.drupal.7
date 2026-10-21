# file_test_file_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 288–290 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L288-L290)
- **Module/theme:** batch_test
- **Implements:** [hook_file_insert()](../../../system/system.api.php/hook_file_insert.md)

## Signature

```php
function file_test_file_insert($file)
```

## Documentation

```text
Implements hook_file_insert().
```

## Code

```php
function file_test_file_insert($file) {
  _file_test_log_call('insert', array($file));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
