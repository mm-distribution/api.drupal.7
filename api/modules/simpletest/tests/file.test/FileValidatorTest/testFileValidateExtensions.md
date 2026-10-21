# FileValidatorTest::testFileValidateExtensions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 392–401 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L392-L401)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileValidateExtensions()
```

## Documentation

```text
Test the file_validate_extensions() function.
```

## Code

```php
  function testFileValidateExtensions() {
    $file = new stdClass();
    $file->filename = 'asdf.txt';
    $errors = file_validate_extensions($file, 'asdf txt pork');
    $this->assertEqual(count($errors), 0, 'Valid extension accepted.', 'File');

    $file->filename = 'asdf.txt';
    $errors = file_validate_extensions($file, 'exe png');
    $this->assertEqual(count($errors), 1, 'Invalid extension blocked.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
