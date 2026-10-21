# FileValidatorTest::testFileValidateImageResolution()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 420–466 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L420-L466)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileValidateImageResolution()
```

## Documentation

```text
 This ensures the resolution of a specific file is within bounds.
 The image will be resized if it's too large.
```

## Code

```php
  function testFileValidateImageResolution() {
    // Non-images.
    $errors = file_validate_image_resolution($this->non_image);
    $this->assertEqual(count($errors), 0, 'Should not get any errors for a non-image file.', 'File');
    $errors = file_validate_image_resolution($this->non_image, '50x50', '100x100');
    $this->assertEqual(count($errors), 0, 'Do not check the resolution on non files.', 'File');

    // Minimum size.
    $errors = file_validate_image_resolution($this->image);
    $this->assertEqual(count($errors), 0, 'No errors for an image when there is no minimum or maximum resolution.', 'File');
    $errors = file_validate_image_resolution($this->image, 0, '200x1');
    $this->assertEqual(count($errors), 1, 'Got an error for an image that was not wide enough.', 'File');
    $errors = file_validate_image_resolution($this->image, 0, '1x200');
    $this->assertEqual(count($errors), 1, 'Got an error for an image that was not tall enough.', 'File');
    $errors = file_validate_image_resolution($this->image, 0, '200x200');
    $this->assertEqual(count($errors), 1, 'Small images report an error.', 'File');

    // Maximum size.
    if (image_get_toolkit()) {
      // Copy the image so that the original doesn't get resized.
      copy('misc/druplicon.png', 'temporary://druplicon.png');
      $this->image->uri = 'temporary://druplicon.png';

      $errors = file_validate_image_resolution($this->image, '10x5');
      $this->assertEqual(count($errors), 0, 'No errors should be reported when an oversized image can be scaled down.', 'File');

      $info = image_get_info($this->image->uri);
      $this->assertTrue($info['width'] <= 10, 'Image scaled to correct width.', 'File');
      $this->assertTrue($info['height'] <= 5, 'Image scaled to correct height.', 'File');

      drupal_unlink('temporary://druplicon.png');

      // Combine maximum and minimum size.
      copy('misc/druplicon.png', 'temporary://druplicon.png');
      $this->image->uri = 'temporary://druplicon.png';

      $errors = file_validate_image_resolution($this->image, '10x5', '5x5');
      $this->assertEqual(count($errors), 1, 'Got an error for an image that was too small after resizing to maximum size.', 'File');

      drupal_unlink('temporary://druplicon.png');
    }
    else {
      // TODO: should check that the error is returned if no toolkit is available.
      $errors = file_validate_image_resolution($this->image, '5x10');
      $this->assertEqual(count($errors), 1, 'Oversize images that cannot be scaled get an error.', 'File');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
