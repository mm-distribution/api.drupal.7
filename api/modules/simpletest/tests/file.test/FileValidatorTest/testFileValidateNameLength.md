# FileValidatorTest::testFileValidateNameLength()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 471–490 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L471-L490)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileValidateNameLength()
```

## Documentation

```text
 This will ensure the filename length is valid.
```

## Code

```php
  function testFileValidateNameLength() {
    // Create a new file object.
    $file = new stdClass();

    // Add a filename with an allowed length and test it.
    $file->filename = str_repeat('x', 240);
    $this->assertEqual(strlen($file->filename), 240);
    $errors = file_validate_name_length($file);
    $this->assertEqual(count($errors), 0, 'No errors reported for 240 length filename.', 'File');

    // Add a filename with a length too long and test it.
    $file->filename = str_repeat('x', 241);
    $errors = file_validate_name_length($file);
    $this->assertEqual(count($errors), 1, 'An error reported for 241 length filename.', 'File');

    // Add a filename with an empty string and test it.
    $file->filename = '';
    $errors = file_validate_name_length($file);
    $this->assertEqual(count($errors), 1, 'An error reported for 0 length filename.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
