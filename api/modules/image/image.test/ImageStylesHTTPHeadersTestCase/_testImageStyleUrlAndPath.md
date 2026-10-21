# ImageStylesHTTPHeadersTestCase::_testImageStyleUrlAndPath()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2217–2265 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2217-L2265)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
private function _testImageStyleUrlAndPath($scheme, $width, $height)
```

## Documentation

```text
Function to scale and test.
```

## Code

```php
  private function _testImageStyleUrlAndPath($scheme, $width, $height) {
    $directory = $scheme . '://styles/' . $this->styleName;
    $status = file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
    $this->assertNotIdentical(FALSE, $status, 'Created the directory for the generated images for the test style.');

    // Create an image field that uses the new style.
    $field_name = strtolower($this->randomName(10));
    $this->createImageField($field_name, 'article', array('uri_scheme' => $scheme));
    $instance = field_info_instance('node', $field_name, 'article');
    $instance['display']['default']['type'] = 'image';
    $instance['display']['default']['settings']['image_style'] = $this->styleName;
    field_update_instance($instance);

    // Create a new node with an image attached.
    $images = $this->drupalGetTestFiles('image');
    // Taking image no. 6 because Apache sets own
    // Content-Length if response is smaller than 8000 bytes.
    $test_image = $images[6];
    $nid = $this->uploadNodeImage($test_image, $field_name, 'article');
    $node = node_load($nid);

    // Get image file from created node.
    $field_items = field_get_items('node', $node, $field_name);
    $file = file_load($field_items[0]['fid']);
    $original_uri = $file->uri;

    // Let the image_module_test module know about this file, so it can claim
    // ownership in hook_file_download().
    variable_set('image_module_test_file_download', $original_uri);

    // Get the URL of a file that has not been generated and try to create it.
    $generated_uri = image_style_path($this->styleName, $original_uri);
    $this->assertFalse(file_exists($generated_uri), 'Generated file does not exist.');
    $generate_url = image_style_url($this->styleName, $original_uri);

    // Fetch the URL that generates the file.
    $this->drupalGet($generate_url);
    $this->assertResponse(200, 'Image was generated at the URL.');
    $this->assertTrue(file_exists($generated_uri), 'Generated file does exist after we accessed it: ' . $generated_uri);

    // Store generated image info.
    $generated_image_info = image_get_info($generated_uri);

    // Compare result.
    $this->assertEqual($this->drupalGetHeader('Content-Type'), $generated_image_info['mime_type'], 'Expected Content-Type was reported.');
    $this->assertEqual($this->drupalGetHeader('Content-Length'), $generated_image_info['file_size'], 'Expected Content-Length was reported: ' . $generated_image_info['file_size'] . ' vs. ' . $this->drupalGetHeader('Content-Length'));
    $this->assertEqual($width, $generated_image_info['width'], 'Expected width was reported.');
    $this->assertEqual($height, $generated_image_info['height'], 'Expected height was reported.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
