# FileDirectoryTest::testFileDirectoryTemp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1228–1235 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1228-L1235)
- **Class:** [FileDirectoryTest](../FileDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileDirectoryTemp()
```

## Documentation

```text
Ensure that the file_directory_temp() function always returns a value.
```

## Code

```php
  function testFileDirectoryTemp() {
    // Start with an empty variable to ensure we have a clean slate.
    variable_set('file_temporary_path', '');
    $tmp_directory = file_directory_temp();
    $this->assertEqual(empty($tmp_directory), FALSE, 'file_directory_temp() returned a non-empty value.');
    $setting = variable_get('file_temporary_path', '');
    $this->assertEqual($setting, $tmp_directory, "The 'file_temporary_path' variable has the same value that file_directory_temp() returned.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
