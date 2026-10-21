# ImageFieldDisplayTestCase::_testImageFieldFormatters()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 969–1041 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L969-L1041)
- **Class:** [ImageFieldDisplayTestCase](../ImageFieldDisplayTestCase.md)
- **Module/theme:** image

## Signature

```php
function _testImageFieldFormatters($scheme)
```

## Documentation

```text
Test image formatters on node display.
```

## Code

```php
  function _testImageFieldFormatters($scheme) {
    $field_name = strtolower($this->randomName());
    $this->createImageField($field_name, 'article', array('uri_scheme' => $scheme));
    // Create a new node with an image attached.
    $test_image = current($this->drupalGetTestFiles('image'));
    $nid = $this->uploadNodeImage($test_image, $field_name, 'article');
    $node = node_load($nid, NULL, TRUE);

    // Test that the default formatter is being used.
    $image_uri = $node->{$field_name}[LANGUAGE_NONE][0]['uri'];
    $image_info = array(
      'path' => $image_uri,
      'width' => 40,
      'height' => 20,
    );
    $default_output = theme('image', $image_info);
    $this->assertRaw($default_output, 'Default formatter displaying correctly on full node view.');

    // Test the image linked to file formatter.
    $instance = field_info_instance('node', $field_name, 'article');
    $instance['display']['default']['type'] = 'image';
    $instance['display']['default']['settings']['image_link'] = 'file';
    field_update_instance($instance);
    $default_output = l(theme('image', $image_info), file_create_url($image_uri), array('html' => TRUE));
    $this->drupalGet('node/' . $nid);
    $this->assertRaw($default_output, 'Image linked to file formatter displaying correctly on full node view.');
    // Verify that the image can be downloaded.
    $this->assertEqual(file_get_contents($test_image->uri), $this->drupalGet(file_create_url($image_uri)), 'File was downloaded successfully.');
    if ($scheme == 'private') {
      // Only verify HTTP headers when using private scheme and the headers are
      // sent by Drupal.
      $this->assertEqual($this->drupalGetHeader('Content-Type'), 'image/png', 'Content-Type header was sent.');
      $this->assertEqual($this->drupalGetHeader('Cache-Control'), 'private', 'Cache-Control header was sent.');

      // Log out and try to access the file.
      $this->drupalLogout();
      $this->drupalGet(file_create_url($image_uri));
      $this->assertResponse('403', 'Access denied to original image as anonymous user.');

      // Log in again.
      $this->drupalLogin($this->admin_user);
    }

    // Test the image linked to content formatter.
    $instance['display']['default']['settings']['image_link'] = 'content';
    field_update_instance($instance);
    $default_output = l(theme('image', $image_info), 'node/' . $nid, array('html' => TRUE, 'attributes' => array('class' => 'active')));
    $this->drupalGet('node/' . $nid);
    $this->assertRaw($default_output, 'Image linked to content formatter displaying correctly on full node view.');

    // Test the image style 'thumbnail' formatter.
    $instance['display']['default']['settings']['image_link'] = '';
    $instance['display']['default']['settings']['image_style'] = 'thumbnail';
    field_update_instance($instance);
    // Ensure the derivative image is generated so we do not have to deal with
    // image style callback paths.
    $this->drupalGet(image_style_url('thumbnail', $image_uri));
    // Need to create the URL again since it will change if clean URLs
    // are disabled.
    $image_info['path'] = image_style_url('thumbnail', $image_uri);
    $image_info['width'] = 100;
    $image_info['height'] = 50;
    $default_output = theme('image', $image_info);
    $this->drupalGet('node/' . $nid);
    $this->assertRaw($default_output, 'Image style thumbnail formatter displaying correctly on full node view.');

    if ($scheme == 'private') {
      // Log out and try to access the file.
      $this->drupalLogout();
      $this->drupalGet(image_style_url('thumbnail', $image_uri));
      $this->assertResponse('403', 'Access denied to image style thumbnail as anonymous user.');
    }
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
