# ImageFieldValidateTestCase::testResolution()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1310–1355 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1310-L1355)
- **Class:** [ImageFieldValidateTestCase](../ImageFieldValidateTestCase.md)
- **Module/theme:** image

## Signature

```php
function testResolution()
```

## Documentation

```text
Test min/max resolution settings.
```

## Code

```php
  function testResolution() {
    $field_name = strtolower($this->randomName());
    $min_resolution = 50;
    $max_resolution = 100;
    $instance_settings = array(
      'max_resolution' => $max_resolution . 'x' . $max_resolution,
      'min_resolution' => $min_resolution . 'x' . $min_resolution,
    );
    $this->createImageField($field_name, 'article', array(), $instance_settings);

    // We want a test image that is too small, and a test image that is too
    // big, so cycle through test image files until we have what we need.
    $image_that_is_too_big = FALSE;
    $image_that_is_too_small = FALSE;
    foreach ($this->drupalGetTestFiles('image') as $image) {
      $info = image_get_info($image->uri);
      if ($info['width'] > $max_resolution) {
        $image_that_is_too_big = $image;
      }
      if ($info['width'] < $min_resolution) {
        $image_that_is_too_small = $image;
      }
      if ($image_that_is_too_small && $image_that_is_too_big) {
        break;
      }
    }
    $nid = $this->uploadNodeImage($image_that_is_too_small, $field_name, 'article');
    $this->assertText(t('The specified file ' . $image_that_is_too_small->filename . ' could not be uploaded. The image is too small; the minimum dimensions are 50x50 pixels.'), 'Node save failed when minimum image resolution was not met.');
    $nid = $this->uploadNodeImage($image_that_is_too_big, $field_name, 'article');
    $this->assertText(t('The image was resized to fit within the maximum allowed dimensions of 100x100 pixels.'), 'Image exceeding max resolution was properly resized.');

    // Verify that image resolution can contain only positive numbers.
    $edit = array(
      'instance[settings][max_resolution][x]' => -10,
      'instance[settings][max_resolution][y]' => -10,
    );
    $this->drupalPost('admin/structure/types/manage/article/fields/' . $field_name, $edit, t('Save settings'));
    $this->assertRaw(t('Height and width values must be positive numbers.'));

    $edit = array(
      'instance[settings][max_resolution][x]' => 'x',
      'instance[settings][max_resolution][y]' => 'x',
    );
    $this->drupalPost('admin/structure/types/manage/article/fields/' . $field_name, $edit, t('Save settings'));
    $this->assertRaw(t('Height and width values must be numeric.'));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
