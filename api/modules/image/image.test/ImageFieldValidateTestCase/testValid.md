# ImageFieldValidateTestCase::testValid()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1260–1305 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1260-L1305)
- **Class:** [ImageFieldValidateTestCase](../ImageFieldValidateTestCase.md)
- **Module/theme:** image

## Signature

```php
public function testValid()
```

## Documentation

```text
Test image validity.
```

## Code

```php
  public function testValid() {
    $image_files = $this->drupalGetTestFiles('image');

    $field_name = strtolower($this->randomName());
    $this->createImageField($field_name, 'article', array(), array('file_directory' => 'test-upload'));
    $expected_path = 'public://test-upload';

    // Create a node with a valid image.
    $node = $this->uploadNodeImage($image_files[0], $field_name, 'article');
    $this->assertTrue(file_exists($expected_path . '/' . $image_files[0]->filename));

    // Remove the image.
    $this->drupalPost('node/' . $node . '/edit', array(), t('Remove'));
    $this->drupalPost(NULL, array(), t('Save'));

    // Get invalid image test files from simpletest.
    $files = file_scan_directory(drupal_get_path('module', 'simpletest') . '/files', '/invalid-img-.*/');
    $invalid_image_files = array();
    foreach ($files as $file) {
      $invalid_image_files[$file->filename] = $file;
    }

    // Try uploading a zero-byte image.
    $zero_size_image = $invalid_image_files['invalid-img-zero-size.png'];
    $edit = array(
      'files[' . $field_name . '_' . LANGUAGE_NONE . '_0]' => drupal_realpath($zero_size_image->uri),
    );
    $this->drupalPost('node/' . $node . '/edit', $edit, t('Upload'));
    $this->assertFalse(file_exists($expected_path . '/' . $zero_size_image->filename));

    // Try uploading an invalid image.
    $invalid_image = $invalid_image_files['invalid-img-test.png'];
    $edit = array(
      'files[' . $field_name . '_' . LANGUAGE_NONE . '_0]' => drupal_realpath($invalid_image->uri),
    );
    $this->drupalPost('node/' . $node . '/edit', $edit, t('Upload'));
    $this->assertFalse(file_exists($expected_path . '/' . $invalid_image->filename));

    // Upload a valid image again.
    $valid_image = $image_files[0];
    $edit = array(
      'files[' . $field_name . '_' . LANGUAGE_NONE . '_0]' => drupal_realpath($valid_image->uri),
    );
    $this->drupalPost('node/' . $node . '/edit', $edit, t('Upload'));
    $this->assertTrue(file_exists($expected_path . '/' . $valid_image->filename));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
