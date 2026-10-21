# file_test_file_scan_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file.test`](_file.md), lines 28–36 · [local source](../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L28-L36)
- **Module/theme:** batch_test

## Signature

```php
function file_test_file_scan_callback($filepath = NULL)
```

## Documentation

```text
Helper function for testing file_scan_directory().

Each time the function is called the file is stored in a static variable.
When the function is called with no $filepath parameter, the results are
returned.

@param $filepath
  File path
@return
  If $filepath is NULL, an array of all previous $filepath parameters
```

## Code

```php
function file_test_file_scan_callback($filepath = NULL) {
  $files = &drupal_static(__FUNCTION__, array());
  if (isset($filepath)) {
    $files[] = $filepath;
  }
  else {
    return $files;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
