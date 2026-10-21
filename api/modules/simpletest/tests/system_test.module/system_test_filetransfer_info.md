# system_test_filetransfer_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 467–476 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L467-L476)
- **Module/theme:** batch_test
- **Implements:** [hook_filetransfer_info()](../../../system/system.api.php/hook_filetransfer_info.md)

## Signature

```php
function system_test_filetransfer_info()
```

## Documentation

```text
Implements hook_filetransfer_info().
```

## Code

```php
function system_test_filetransfer_info() {
  return array(
    'system_test' => array(
      'title' => t('System Test FileTransfer'),
      'file' => 'system_test.module',  // Should be a .inc, but for test, ok.
      'class' => 'SystemTestFileTransfer',
      'weight' => -10,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
