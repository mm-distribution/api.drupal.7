# ImageStyleFlushTest::testFlush()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2050–2109 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2050-L2109)
- **Class:** [ImageStyleFlushTest](../ImageStyleFlushTest.md)
- **Module/theme:** image

## Signature

```php
function testFlush()
```

## Documentation

```text
General test to flush a style.
```

## Code

```php
  function testFlush() {

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
    );

    // Add style form.
    $edit = array(
      'name' => $style_name,
      'label' => $style_label,
    );
    $this->drupalPost('admin/config/media/image-styles/add', $edit, t('Create new style'));
    // Add each sample effect to the style.
    foreach ($effect_edits as $effect => $edit) {
      // Add the effect.
      $this->drupalPost($style_path, array('new' => $effect), t('Add'));
      if (!empty($edit)) {
        $this->drupalPost(NULL, $edit, t('Add effect'));
      }
    }

    // Load the saved image style.
    $style = image_style_load($style_name);

    // Create an image for the 'public' wrapper.
    $image_path = $this->createSampleImage($style, 'public');
    // Expecting to find 2 images, one is the sample.png image shown in
    // image style preview.
    $this->assertEqual($this->getImageCount($style, 'public'), 2, format_string('Image style %style image %file successfully generated.', array('%style' => $style['name'], '%file' => $image_path)));

    // Create an image for the 'private' wrapper.
    $image_path = $this->createSampleImage($style, 'private');
    $this->assertEqual($this->getImageCount($style, 'private'), 1, format_string('Image style %style image %file successfully generated.', array('%style' => $style['name'], '%file' => $image_path)));

    // Remove the 'image_scale' effect and updates the style, which in turn
    // forces an image style flush.
    $effect = array_pop($style['effects']);
    $this->drupalPost($style_path . '/effects/' . $effect['ieid'] . '/delete', array(), t('Delete'));
    $this->assertResponse(200);
    $this->drupalPost($style_path, array(), t('Update style'));
    $this->assertResponse(200);

    // Post flush, expected 1 image in the 'public' wrapper (sample.png).
    $this->assertEqual($this->getImageCount($style, 'public'), 1, format_string('Image style %style flushed correctly for %wrapper wrapper.', array('%style' => $style['name'], '%wrapper' => 'public')));

    // Post flush, expected no image in the 'private' wrapper.
    $this->assertEqual($this->getImageCount($style, 'private'), 0, format_string('Image style %style flushed correctly for %wrapper wrapper.', array('%style' => $style['name'], '%wrapper' => 'private')));
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
