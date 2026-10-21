# ImageFieldDisplayTestCase::testImageFieldSettings()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1046–1120 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1046-L1120)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFieldSettings()
```

## Documentation

```text
Tests for image field settings.
```

## Code

```php
  function testImageFieldSettings() {
    $test_image = current($this->drupalGetTestFiles('image'));
    list(, $test_image_extension) = explode('.', $test_image->filename);
    $field_name = strtolower($this->randomName());
    $instance_settings = array(
      'alt_field' => 1,
      'file_extensions' => $test_image_extension,
      'max_filesize' => '50 KB',
      'max_resolution' => '100x100',
      'min_resolution' => '10x10',
      'title_field' => 1,
    );
    $widget_settings = array(
      'preview_image_style' => 'medium',
    );
    $field = $this->createImageField($field_name, 'article', array(), $instance_settings, $widget_settings);
    $field['deleted'] = 0;
    $table = _field_sql_storage_tablename($field);
    $schema = drupal_get_schema($table, TRUE);
    $instance = field_info_instance('node', $field_name, 'article');

    $this->drupalGet('node/add/article');
    $this->assertText(t('Files must be less than 50 KB.'), 'Image widget max file size is displayed on article form.');
    $this->assertText(t('Allowed file types: ' . $test_image_extension . '.'), 'Image widget allowed file types displayed on article form.');
    $this->assertText(t('Images must be at least 10x10 pixels. Images larger than 100x100 pixels will be resized.'), 'Image widget allowed resolution displayed on article form.');

    // We have to create the article first and then edit it because the alt
    // and title fields do not display until the image has been attached.
    $nid = $this->uploadNodeImage($test_image, $field_name, 'article');
    $this->drupalGet('node/' . $nid . '/edit');
    $this->assertFieldByName($field_name . '[' . LANGUAGE_NONE . '][0][alt]', '', 'Alt field displayed on article form.');
    $this->assertFieldByName($field_name . '[' . LANGUAGE_NONE . '][0][title]', '', 'Title field displayed on article form.');
    // Verify that the attached image is being previewed using the 'medium'
    // style.
    $node = node_load($nid, NULL, TRUE);
    $image_info = array(
      'path' => image_style_url('medium', $node->{$field_name}[LANGUAGE_NONE][0]['uri']),
      'width' => 220,
      'height' => 110,
    );
    $default_output = theme('image', $image_info);
    $this->assertRaw($default_output, "Preview image is displayed using 'medium' style.");

    // Add alt/title fields to the image and verify that they are displayed.
    $image_info = array(
      'path' => $node->{$field_name}[LANGUAGE_NONE][0]['uri'],
      'alt' => $this->randomName(),
      'title' => $this->randomName(),
      'width' => 40,
      'height' => 20,
    );
    $edit = array(
      $field_name . '[' . LANGUAGE_NONE . '][0][alt]' => $image_info['alt'],
      $field_name . '[' . LANGUAGE_NONE . '][0][title]' => $image_info['title'],
    );
    $this->drupalPost('node/' . $nid . '/edit', $edit, t('Save'));
    $default_output = theme('image', $image_info);
    $this->assertRaw($default_output, 'Image displayed using user supplied alt and title attributes.');

    // Verify that alt/title longer than allowed results in a validation error.
    $test_size = 2000;
    $edit = array(
      $field_name . '[' . LANGUAGE_NONE . '][0][alt]' => $this->randomName($test_size),
      $field_name . '[' . LANGUAGE_NONE . '][0][title]' => $this->randomName($test_size),
    );
    $this->drupalPost('node/' . $nid . '/edit', $edit, t('Save'));
    $this->assertRaw(t('Alternate text cannot be longer than %max characters but is currently %length characters long.', array(
      '%max' => $schema['fields'][$field_name .'_alt']['length'],
      '%length' => $test_size,
    )));
    $this->assertRaw(t('Title cannot be longer than %max characters but is currently %length characters long.', array(
      '%max' => $schema['fields'][$field_name .'_title']['length'],
      '%length' => $test_size,
    )));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
