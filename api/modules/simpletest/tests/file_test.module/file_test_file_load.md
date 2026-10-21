# file_test_file_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 260–267 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L260-L267)
- **Module/theme:** batch_test
- **Implements:** [hook_file_load()](../../../system/system.api.php/hook_file_load.md)

## Signature

```php
function file_test_file_load($files)
```

## Documentation

```text
Implements hook_file_load().
```

## Code

```php
function file_test_file_load($files) {
  foreach ($files as $file) {
    _file_test_log_call('load', array($file));
    // Assign a value on the object so that we can test that the $file is passed
    // by reference.
    $file->file_test['loaded'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
