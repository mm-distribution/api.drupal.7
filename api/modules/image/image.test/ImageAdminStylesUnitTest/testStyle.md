# ImageAdminStylesUnitTest::testStyle()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 629–780 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L629-L780)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testStyle()
```

## Documentation

```text
General test to add a style, add/remove/edit effects to it, then delete it.
```

## Code

```php
  function testStyle() {
    // Setup a style to be created and effects to add to it.
    $style_name = strtolower($this->randomName(10));
    $style_label = $this->randomString();
    $style_path = 'admin/config/media/image-styles/edit/' . $style_name;
    $effect_edits = array(
      'image_resize' => array(
        'data[width]' => 100,
        'data[height]' => 101,
      ),
      'image_scale' => array(
        'data[width]' => 110,
        'data[height]' => 111,
        'data[upscale]' => 1,
      ),
      'image_scale_and_crop' => array(
        'data[width]' => 120,
        'data[height]' => 121,
      ),
      'image_crop' => array(
        'data[width]' => 130,
        'data[height]' => 131,
        'data[anchor]' => 'center-center',
      ),
      'image_desaturate' => array(
        // No options for desaturate.
      ),
      'image_rotate' => array(
        'data[degrees]' => 5,
        'data[random]' => 1,
        'data[bgcolor]' => '#FFFF00',
      ),
    );

    // Add style form.

    $edit = array(
      'name' => $style_name,
      'label' => $style_label,
    );
    $this->drupalPost('admin/config/media/image-styles/add', $edit, t('Create new style'));
    $this->assertRaw(t('Style %name was created.', array('%name' => $style_label)), 'Image style successfully created.');

    // Add effect form.

    // Add each sample effect to the style.
    foreach ($effect_edits as $effect => $edit) {
      // Add the effect.
      $this->drupalPost($style_path, array('new' => $effect), t('Add'));
      if (!empty($edit)) {
        $this->drupalPost(NULL, $edit, t('Add effect'));
      }
    }

    // Edit effect form.

    // Revisit each form to make sure the effect was saved.
    drupal_static_reset('image_styles');
    $style = image_style_load($style_name);

    foreach ($style['effects'] as $ieid => $effect) {
      $this->drupalGet($style_path . '/effects/' . $ieid);
      foreach ($effect_edits[$effect['name']] as $field => $value) {
        $this->assertFieldByName($field, $value, format_string('The %field field in the %effect effect has the correct value of %value.', array('%field' => $field, '%effect' => $effect['name'], '%value' => $value)));
      }
    }

    // Image style overview form (ordering and renaming).

    // Confirm the order of effects is maintained according to the order we
    // added the fields.
    $effect_edits_order = array_keys($effect_edits);
    $effects_order = array_values($style['effects']);
    $order_correct = TRUE;
    foreach ($effects_order as $index => $effect) {
      if ($effect_edits_order[$index] != $effect['name']) {
        $order_correct = FALSE;
      }
    }
    $this->assertTrue($order_correct, 'The order of the effects is correctly set by default.');

    // Test the style overview form.
    // Change the name of the style and adjust the weights of effects.
    $style_name = strtolower($this->randomName(10));
    $style_label = $this->randomString();
    $weight = count($effect_edits);
    $edit = array(
      'name' => $style_name,
      'label' => $style_label,
    );
    foreach ($style['effects'] as $ieid => $effect) {
      $edit['effects[' . $ieid . '][weight]'] = $weight;
      $weight--;
    }

    // Create an image to make sure it gets flushed after saving.
    $image_path = $this->createSampleImage($style);
    $this->assertEqual($this->getImageCount($style), 1, format_string('Image style %style image %file successfully generated.', array('%style' => $style['label'], '%file' => $image_path)));

    $this->drupalPost($style_path, $edit, t('Update style'));

    // Note that after changing the style name, the style path is changed.
    $style_path = 'admin/config/media/image-styles/edit/' . $style_name;

    // Check that the URL was updated.
    $this->drupalGet($style_path);
    $this->assertResponse(200, format_string('Image style %original renamed to %new', array('%original' => $style['label'], '%new' => $style_label)));

    // Check that the image was flushed after updating the style.
    // This is especially important when renaming the style. Make sure that
    // the old image directory has been deleted.
    $this->assertEqual($this->getImageCount($style), 0, format_string('Image style %style was flushed after renaming the style and updating the order of effects.', array('%style' => $style['label'])));

    // Load the style by the new name with the new weights.
    drupal_static_reset('image_styles');
    $style = image_style_load($style_name, NULL);

    // Confirm the new style order was saved.
    $effect_edits_order = array_reverse($effect_edits_order);
    $effects_order = array_values($style['effects']);
    $order_correct = TRUE;
    foreach ($effects_order as $index => $effect) {
      if ($effect_edits_order[$index] != $effect['name']) {
        $order_correct = FALSE;
      }
    }
    $this->assertTrue($order_correct, 'The order of the effects is correctly set by default.');

    // Image effect deletion form.

    // Create an image to make sure it gets flushed after deleting an effect.
    $image_path = $this->createSampleImage($style);
    $this->assertEqual($this->getImageCount($style), 1, format_string('Image style %style image %file successfully generated.', array('%style' => $style['label'], '%file' => $image_path)));

    // Test effect deletion form.
    $effect = array_pop($style['effects']);
    $this->drupalPost($style_path . '/effects/' . $effect['ieid'] . '/delete', array(), t('Delete'));
    $this->assertRaw(t('The image effect %name has been deleted.', array('%name' => $effect['label'])), 'Image effect deleted.');

    // Style deletion form.

    // Delete the style.
    $this->drupalPost('admin/config/media/image-styles/delete/' . $style_name, array(), t('Delete'));

    // Confirm the style directory has been removed.
    $directory = file_default_scheme() . '://styles/' . $style_name;
    $this->assertFalse(is_dir($directory), format_string('Image style %style directory removed on style deletion.', array('%style' => $style['label'])));

    drupal_static_reset('image_styles');
    $this->assertFalse(image_style_load($style_name), format_string('Image style %style successfully deleted.', array('%style' => $style['label'])));

  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
