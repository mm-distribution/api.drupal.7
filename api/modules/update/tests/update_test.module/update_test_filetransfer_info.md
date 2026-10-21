# update_test_filetransfer_info()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 140–154 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L140-L154)
- **Module/theme:** aaa_update_test
- **Implements:** [hook_filetransfer_info()](../../../system/system.api.php/hook_filetransfer_info.md)

## Signature

```php
function update_test_filetransfer_info()
```

## Documentation

```text
Implements hook_filetransfer_info().
```

## Code

```php
function update_test_filetransfer_info() {
  // Define a mock file transfer method, to ensure that there will always be
  // at least one method available in the user interface (regardless of the
  // environment in which the update manager tests are run).
  return array(
    'system_test' => array(
      'title' => t('Update Test FileTransfer'),
      // This should be in an .inc file, but for testing purposes, it is OK to
      // leave it in the main module file.
      'file' => 'update_test.module',
      'class' => 'UpdateTestFileTransfer',
      'weight' => -20,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
