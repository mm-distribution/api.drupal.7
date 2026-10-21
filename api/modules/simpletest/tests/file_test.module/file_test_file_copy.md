# file_test_file_copy()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 302–304 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L302-L304)
- **Module/theme:** batch_test
- **Implements:** [hook_file_copy()](../../../system/system.api.php/hook_file_copy.md)

## Signature

```php
function file_test_file_copy($file, $source)
```

## Documentation

```text
Implements hook_file_copy().
```

## Code

```php
function file_test_file_copy($file, $source) {
  _file_test_log_call('copy', array($file, $source));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
