# ImageThemeFunctionWebTestCase::testImageFormatterTheme()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 1966–2003 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L1966-L2003)
- **Class:** [ImageThemeFunctionWebTestCase](../ImageThemeFunctionWebTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageFormatterTheme()
```

## Documentation

```text
Tests usage of the image field formatters.
```

## Code

```php
  function testImageFormatterTheme() {
    // Create an image.
    $files = $this->drupalGetTestFiles('image');
    $file = reset($files);
    $original_uri = file_unmanaged_copy($file->uri, 'public://', FILE_EXISTS_RENAME);

    // Create a style.
    image_style_save(array('name' => 'test', 'label' => 'Test'));
    $url = image_style_url('test', $original_uri);

    // Test using theme_image_formatter() without an image title, alt text, or
    // link options.
    $path = $this->randomName();
    $element = array(
      '#theme' => 'image_formatter',
      '#image_style' => 'test',
      '#item' => array(
        'uri' => $original_uri,
      ),
      '#path' => array(
        'path' => $path,
      ),
    );
    $rendered_element = render($element);
    $expected_result = '<a href="' . url($path) . '"><img typeof="foaf:Image" src="' . check_plain($url) . '" alt="" /></a>';
    $this->assertEqual($expected_result, $rendered_element, 'theme_image_formatter() correctly renders without title, alt, or path options.');

    // Link the image to a fragment on the page, and not a full URL.
    $fragment = $this->randomName();
    $element['#path']['path'] = '';
    $element['#path']['options'] = array(
      'external' => TRUE,
      'fragment' => $fragment,
    );
    $rendered_element = render($element);
    $expected_result = '<a href="#' . $fragment . '"><img typeof="foaf:Image" src="' . check_plain($url) . '" alt="" /></a>';
    $this->assertEqual($expected_result, $rendered_element, 'theme_image_formatter() correctly renders a link fragment.');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
