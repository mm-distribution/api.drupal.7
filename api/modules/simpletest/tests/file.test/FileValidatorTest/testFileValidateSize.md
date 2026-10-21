# FileValidatorTest::testFileValidateSize()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 496–508 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L496-L508)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileValidateSize()
```

## Documentation

```text
Test file_validate_size().
```

## Code

```php
  function testFileValidateSize() {
    // Create a file with a size of 1000 bytes, and quotas of only 1 byte.
    $file = new stdClass();
    $file->filesize = 1000;
    $errors = file_validate_size($file, 0, 0);
    $this->assertEqual(count($errors), 0, 'No limits means no errors.', 'File');
    $errors = file_validate_size($file, 1, 0);
    $this->assertEqual(count($errors), 1, 'Error for the file being over the limit.', 'File');
    $errors = file_validate_size($file, 0, 1);
    $this->assertEqual(count($errors), 1, 'Error for the user being over their limit.', 'File');
    $errors = file_validate_size($file, 1, 1);
    $this->assertEqual(count($errors), 2, 'Errors for both the file and their limit.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
