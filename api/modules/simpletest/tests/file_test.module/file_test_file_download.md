# file_test_file_download()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 280–283 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L280-L283)
- **Module/theme:** batch_test
- **Implements:** [hook_file_download()](../../../system/system.api.php/hook_file_download.md)

## Signature

```php
function file_test_file_download($uri)
```

## Documentation

```text
Implements hook_file_download().
```

## Code

```php
function file_test_file_download($uri) {
  _file_test_log_call('download', array($uri));
  return _file_test_get_return('download');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
