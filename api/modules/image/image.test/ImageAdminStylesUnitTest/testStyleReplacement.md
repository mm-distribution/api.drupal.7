# ImageAdminStylesUnitTest::testStyleReplacement()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 877–923 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L877-L923)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testStyleReplacement()
```

## Documentation

```text
Test deleting a style and choosing a replacement style.
```

## Code

```php
  function testStyleReplacement() {
    // Create a new style.
    $style_name = strtolower($this->randomName(10));
    $style_label = $this->randomString();
    image_style_save(array('name' => $style_name, 'label' => $style_label));
    $style_path = 'admin/config/media/image-styles/edit/' . $style_name;

    // Create an image field that uses the new style.
    $field_name = strtolower($this->randomName(10));
    $this->createImageField($field_name, 'article');
    $instance = field_info_instance('node', $field_name, 'article');
    $instance['display']['default']['type'] = 'image';
    $instance['display']['default']['settings']['image_style'] = $style_name;
    field_update_instance($instance);

    // Create a new node with an image attached.
    $test_image = current($this->drupalGetTestFiles('image'));
    $nid = $this->uploadNodeImage($test_image, $field_name, 'article');
    $node = node_load($nid);

    // Test that image is displayed using newly created style.
    $this->drupalGet('node/' . $nid);
    $this->assertRaw(check_plain(image_style_url($style_name, $node->{$field_name}[LANGUAGE_NONE][0]['uri'])), format_string('Image displayed using style @style.', array('@style' => $style_name)));

    // Rename the style and make sure the image field is updated.
    $new_style_name = strtolower($this->randomName(10));
    $new_style_label = $this->randomString();
    $edit = array(
      'name' => $new_style_name,
      'label' => $new_style_label,
    );
    $this->drupalPost('admin/config/media/image-styles/edit/' . $style_name, $edit, t('Update style'));
    $this->assertText(t('Changes to the style have been saved.'), format_string('Style %name was renamed to %new_name.', array('%name' => $style_name, '%new_name' => $new_style_name)));
    $this->drupalGet('node/' . $nid);
    $this->assertRaw(check_plain(image_style_url($new_style_name, $node->{$field_name}[LANGUAGE_NONE][0]['uri'])), format_string('Image displayed using style replacement style.'));

    // Delete the style and choose a replacement style.
    $edit = array(
      'replacement' => 'thumbnail',
    );
    $this->drupalPost('admin/config/media/image-styles/delete/' . $new_style_name, $edit, t('Delete'));
    $message = t('Style %name was deleted.', array('%name' => $new_style_label));
    $this->assertRaw($message, $message);

    $this->drupalGet('node/' . $nid);
    $this->assertRaw(check_plain(image_style_url('thumbnail', $node->{$field_name}[LANGUAGE_NONE][0]['uri'])), format_string('Image displayed using style replacement style.'));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
