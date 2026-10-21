# ImageDimensionsTestCase::testImageDimensions()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1378–1573 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1378-L1573)
- **Class:** [ImageDimensionsTestCase](../ImageDimensionsTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageDimensions()
```

## Documentation

```text
Test styled image dimensions cumulatively.
```

## Code

```php
  function testImageDimensions() {
    // Create a working copy of the file.
    $files = $this->drupalGetTestFiles('image');
    $file = reset($files);
    $original_uri = file_unmanaged_copy($file->uri, 'public://', FILE_EXISTS_RENAME);

    // Create a style.
    $style = image_style_save(array('name' => 'test', 'label' => 'Test'));
    $generated_uri = 'public://styles/test/public/'. drupal_basename($original_uri);
    $url = image_style_url('test', $original_uri);

    $variables = array(
      'style_name' => 'test',
      'path' => $original_uri,
      'width' => 40,
      'height' => 20,
    );

    // Scale an image that is wider than it is high.
    $effect = array(
      'name' => 'image_scale',
      'data' => array(
        'width' => 120,
        'height' => 90,
        'upscale' => TRUE,
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="120" height="60" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 120, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 60, 'Expected height was found.');

    // Rotate 90 degrees anticlockwise.
    $effect = array(
      'name' => 'image_rotate',
      'data' => array(
        'degrees' => -90,
        'random' => FALSE,
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="60" height="120" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 60, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 120, 'Expected height was found.');

    // Scale an image that is higher than it is wide (rotated by previous effect).
    $effect = array(
      'name' => 'image_scale',
      'data' => array(
        'width' => 120,
        'height' => 90,
        'upscale' => TRUE,
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="45" height="90" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 45, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 90, 'Expected height was found.');

    // Test upscale disabled.
    $effect = array(
      'name' => 'image_scale',
      'data' => array(
        'width' => 400,
        'height' => 200,
        'upscale' => FALSE,
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="45" height="90" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 45, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 90, 'Expected height was found.');

    // Add a desaturate effect.
    $effect = array(
      'name' => 'image_desaturate',
      'data' => array(),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="45" height="90" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 45, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 90, 'Expected height was found.');

    // Add a random rotate effect.
    $effect = array(
      'name' => 'image_rotate',
      'data' => array(
        'degrees' => 180,
        'random' => TRUE,
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');


    // Add a crop effect.
    $effect = array(
      'name' => 'image_crop',
      'data' => array(
        'width' => 30,
        'height' => 30,
        'anchor' => 'center-center',
      ),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" width="30" height="30" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');
    $image_info = image_get_info($generated_uri);
    $this->assertEqual($image_info['width'], 30, 'Expected width was found.');
    $this->assertEqual($image_info['height'], 30, 'Expected height was found.');

    // Rotate to a non-multiple of 90 degrees.
    $effect = array(
      'name' => 'image_rotate',
      'data' => array(
        'degrees' => 57,
        'random' => FALSE,
      ),
      'isid' => $style['isid'],
    );

    $effect = image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" alt="" />', 'Expected img tag was found.');
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $this->drupalGet($url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it.');

    image_effect_delete($effect);

    // Ensure that an effect with no dimensions callback unsets the dimensions.
    // This ensures compatibility with 7.0 contrib modules.
    $effect = array(
      'name' => 'image_module_test_null',
      'data' => array(),
      'isid' => $style['isid'],
    );

    image_effect_save($effect);
    $img_tag = theme_image_style($variables);
    $this->assertEqual($img_tag, '<img typeof="foaf:Image" src="' . check_plain($url) . '" alt="" />', 'Expected img tag was found.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
