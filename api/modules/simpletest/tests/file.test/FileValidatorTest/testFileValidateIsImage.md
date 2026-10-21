# FileValidatorTest::testFileValidateIsImage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 406–414 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L406-L414)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileValidateIsImage()
```

## Documentation

```text
 This ensures a specific file is actually an image.
```

## Code

```php
  function testFileValidateIsImage() {
    $this->assertTrue(file_exists($this->image->uri), 'The image being tested exists.', 'File');
    $errors = file_validate_is_image($this->image);
    $this->assertEqual(count($errors), 0, 'No error reported for our image file.', 'File');

    $this->assertTrue(file_exists($this->non_image->uri), 'The non-image being tested exists.', 'File');
    $errors = file_validate_is_image($this->non_image);
    $this->assertEqual(count($errors), 1, 'An error reported for our non-image file.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
