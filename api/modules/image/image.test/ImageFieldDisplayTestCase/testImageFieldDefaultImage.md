# ImageFieldDisplayTestCase::testImageFieldDefaultImage()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1142–1212 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1142-L1212)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFieldDefaultImage()
```

## Documentation

```text
Test use of a default image with an image field.
```

## Code

```php
  function testImageFieldDefaultImage() {
    // Create a new image field.
    $field_name = strtolower($this->randomName());
    $this->createImageField($field_name, 'article');

    // Create a new node, with no images and verify that no images are
    // displayed.
    $node = $this->drupalCreateNode(array('type' => 'article'));
    $this->drupalGet('node/' . $node->nid);
    // Verify that no image is displayed on the page by checking for the class
    // that would be used on the image field.
    $this->assertNoPattern('<div class="(.*?)field-name-' . strtr($field_name, '_', '-') . '(.*?)">', 'No image displayed when no image is attached and no default image specified.');

    // Add a default image to the public imagefield instance.
    $images = $this->drupalGetTestFiles('image');
    $edit = array(
      'files[field_settings_default_image]' => drupal_realpath($images[0]->uri),
    );
    $this->drupalPost('admin/structure/types/manage/article/fields/' . $field_name, $edit, t('Save settings'));
    // Clear field info cache so the new default image is detected.
    field_info_cache_clear();
    $field = field_info_field($field_name);
    $image = file_load($field['settings']['default_image']);
    $this->assertTrue($image->status == FILE_STATUS_PERMANENT, 'The default image status is permanent.');
    $default_output = theme('image', array('path' => $image->uri));
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw($default_output, 'Default image displayed when no user supplied image is present.');

    // Create a node with an image attached and ensure that the default image
    // is not displayed.
    $nid = $this->uploadNodeImage($images[1], $field_name, 'article');
    $node = node_load($nid, NULL, TRUE);
    $image_info = array(
      'path' => $node->{$field_name}[LANGUAGE_NONE][0]['uri'],
      'width' => 40,
      'height' => 20,
    );
    $image_output = theme('image', $image_info);
    $this->drupalGet('node/' . $nid);
    $this->assertNoRaw($default_output, 'Default image is not displayed when user supplied image is present.');
    $this->assertRaw($image_output, 'User supplied image is displayed.');

    // Remove default image from the field and make sure it is no longer used.
    $edit = array(
      'field[settings][default_image][fid]' => 0,
    );
    $this->drupalPost('admin/structure/types/manage/article/fields/' . $field_name, $edit, t('Save settings'));
    // Clear field info cache so the new default image is detected.
    field_info_cache_clear();
    $field = field_info_field($field_name);
    $this->assertFalse($field['settings']['default_image'], 'Default image removed from field.');
    // Create an image field that uses the private:// scheme and test that the
    // default image works as expected.
    $private_field_name = strtolower($this->randomName());
    $this->createImageField($private_field_name, 'article', array('uri_scheme' => 'private'));
    // Add a default image to the new field.
    $edit = array(
      'files[field_settings_default_image]' => drupal_realpath($images[1]->uri),
    );
    $this->drupalPost('admin/structure/types/manage/article/fields/' . $private_field_name, $edit, t('Save settings'));
    $private_field = field_info_field($private_field_name);
    $image = file_load($private_field['settings']['default_image']);
    $this->assertEqual('private', file_uri_scheme($image->uri), 'Default image uses private:// scheme.');
    $this->assertTrue($image->status == FILE_STATUS_PERMANENT, 'The default image status is permanent.');
    // Create a new node with no image attached and ensure that default private
    // image is displayed.
    $node = $this->drupalCreateNode(array('type' => 'article'));
    $default_output = theme('image', array('path' => $image->uri));
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw($default_output, 'Default private image displayed when no user supplied image is present.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
