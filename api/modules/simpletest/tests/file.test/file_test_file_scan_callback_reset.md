# file_test_file_scan_callback_reset()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 41–43 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L41-L43)
- **Module/theme:** batch_test

## Signature

```php
function file_test_file_scan_callback_reset()
```

## Documentation

```text
Reset static variables used by file_test_file_scan_callback().
```

## Code

```php
function file_test_file_scan_callback_reset() {
  drupal_static_reset('file_test_file_scan_callback');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
