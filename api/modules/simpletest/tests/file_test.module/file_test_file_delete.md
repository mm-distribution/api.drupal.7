# file_test_file_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 316–318 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L316-L318)
- **Module/theme:** batch_test
- **Implements:** [hook_file_delete()](../../../system/system.api.php/hook_file_delete.md)

## Signature

```php
function file_test_file_delete($file)
```

## Documentation

```text
Implements hook_file_delete().
```

## Code

```php
function file_test_file_delete($file) {
  _file_test_log_call('delete', array($file));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
