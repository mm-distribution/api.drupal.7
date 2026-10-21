# ImageAdminStylesUnitTest::testDefaultStyle()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 785–872 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L785-L872)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testDefaultStyle()
```

## Documentation

```text
Test to override, edit, then revert a style.
```

## Code

```php
  function testDefaultStyle() {
    // Setup a style to be created and effects to add to it.
    $style_name = 'thumbnail';
    $style_label = 'Thumbnail (100x100)';
    $edit_path = 'admin/config/media/image-styles/edit/' . $style_name;
    $delete_path = 'admin/config/media/image-styles/delete/' . $style_name;
    $revert_path = 'admin/config/media/image-styles/revert/' . $style_name;

    // Ensure deleting a default is not possible.
    $this->drupalGet($delete_path);
    $this->assertText(t('Page not found'), 'Default styles may not be deleted.');

    // Ensure that editing a default is not possible (without overriding).
    $this->drupalGet($edit_path);
    $disabled_field = $this->xpath('//input[@id=:id and @disabled="disabled"]', array(':id' => 'edit-name'));
    $this->assertTrue($disabled_field, 'Default styles may not be renamed.');
    $this->assertNoField('edit-submit', 'Default styles may not be edited.');
    $this->assertNoField('edit-add', 'Default styles may not have new effects added.');

    // Create an image to make sure the default works before overriding.
    drupal_static_reset('image_styles');
    $style = image_style_load($style_name);
    $image_path = $this->createSampleImage($style);
    $this->assertEqual($this->getImageCount($style), 1, format_string('Image style %style image %file successfully generated.', array('%style' => $style['name'], '%file' => $image_path)));

    // Verify that effects attached to a default style do not have an ieid key.
    foreach ($style['effects'] as $effect) {
      $this->assertFalse(isset($effect['ieid']), format_string('The %effect effect does not have an ieid.', array('%effect' => $effect['name'])));
    }

    // Override the default.
    $this->drupalPost($edit_path, array(), t('Override defaults'));
    $this->assertRaw(t('The %style style has been overridden, allowing you to change its settings.', array('%style' => $style_label)), 'Default image style may be overridden.');

    // Add sample effect to the overridden style.
    $this->drupalPost($edit_path, array('new' => 'image_desaturate'), t('Add'));
    drupal_static_reset('image_styles');
    $style = image_style_load($style_name);

    // Verify that effects attached to the style have an ieid now.
    foreach ($style['effects'] as $effect) {
      $this->assertTrue(isset($effect['ieid']), format_string('The %effect effect has an ieid.', array('%effect' => $effect['name'])));
    }

    // The style should now have 2 effect, the original scale provided by core
    // and the desaturate effect we added in the override.
    $effects = array_values($style['effects']);
    $this->assertEqual($effects[0]['name'], 'image_scale', 'The default effect still exists in the overridden style.');
    $this->assertEqual($effects[1]['name'], 'image_desaturate', 'The added effect exists in the overridden style.');

    // Check that we are able to rename an overridden style.
    $this->drupalGet($edit_path);
    $disabled_field = $this->xpath('//input[@id=:id and @disabled="disabled"]', array(':id' => 'edit-name'));
    $this->assertFalse($disabled_field, 'Overridden styles may be renamed.');

    // Create an image to ensure the override works properly.
    $image_path = $this->createSampleImage($style);
    $this->assertEqual($this->getImageCount($style), 1, format_string('Image style %style image %file successfully generated.', array('%style' => $style['label'], '%file' => $image_path)));

    // Revert the image style.
    $this->drupalPost($revert_path, array(), t('Revert'));
    drupal_static_reset('image_styles');
    $style = image_style_load($style_name);

    // The style should now have the single effect for scale.
    $effects = array_values($style['effects']);
    $this->assertEqual($effects[0]['name'], 'image_scale', 'The default effect still exists in the reverted style.');
    $this->assertFalse(array_key_exists(1, $effects), 'The added effect has been removed in the reverted style.');

    // Verify that a new style with the same name as the default one could not
    // be created.
    $edit = array(
      'name' => $style_name,
      'label' => $style_label,
    );
    // The default style is not overriden.
    $this->drupalPost('admin/config/media/image-styles/add', $edit, t('Create new style'));
    $this->assertNoRaw(t('Style %name was created.', array('%name' => $style_label)), 'Image style successfully created.');
    // Override the default.
    $this->drupalPost($edit_path, array(), t('Override defaults'));
    $this->assertRaw(t('The %style style has been overridden, allowing you to change its settings.', array('%style' => $style_label)), 'Default image style may be overridden.');
    // The default style is overriden.
    $this->drupalPost('admin/config/media/image-styles/add', $edit, t('Create new style'));
    $this->assertNoRaw(t('Style %name was created.', array('%name' => $style_label)), 'Image style successfully created.');
    // Revert the image style.
    $this->drupalPost($revert_path, array(), t('Revert'));
    drupal_static_reset('image_styles');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
