# ImageFieldDisplayTestCase::testMissingImageFieldDisplay()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1217–1242 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1217-L1242)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testMissingImageFieldDisplay()
```

## Documentation

```text
Tests the display of image field with the missing FID.
```

## Code

```php
  function testMissingImageFieldDisplay() {
    $field_name = strtolower($this->randomName());
    $type_name = 'article';
    $field_settings = array(
      'display_field' => '1',
      'display_default' => '1',
    );
    $instance_settings = array(
      'description_field' => '1',
    );
    $widget_settings = array();
    $this->createImageField($field_name, $type_name, $field_settings, $instance_settings, $widget_settings);
    $images = $this->drupalGetTestFiles('image');

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeImage($images[1], $field_name, 'article');
    // Delete uploaded file from file_managed table.
    $max_fid_after = db_query('SELECT MAX(fid) AS fid FROM {file_managed}')->fetchField();
    $uploaded_file = file_load($max_fid_after);
    file_delete($uploaded_file, TRUE);
    // Clear field cache.
    field_cache_clear();
    // Check the node detail if the file is loaded.
    $this->drupalGet('node/' . $nid);
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
