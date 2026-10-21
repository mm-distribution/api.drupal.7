# file_test_file_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 295–297 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L295-L297)
- **Module/theme:** batch_test
- **Implements:** [hook_file_update()](../../../system/system.api.php/hook_file_update.md)

## Signature

```php
function file_test_file_update($file)
```

## Documentation

```text
Implements hook_file_update().
```

## Code

```php
function file_test_file_update($file) {
  _file_test_log_call('update', array($file));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
