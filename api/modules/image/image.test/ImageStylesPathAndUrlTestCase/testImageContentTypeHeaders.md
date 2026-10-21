# ImageStylesPathAndUrlTestCase::testImageContentTypeHeaders()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 212–223 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L212-L223)
- **Class:** [ImageStylesPathAndUrlTestCase](../ImageStylesPathAndUrlTestCase.md)
- **Module/theme:** image

## Signature

```php
function testImageContentTypeHeaders()
```

## Documentation

```text
Test that we do not pass an array to drupal_add_http_header.
```

## Code

```php
  function testImageContentTypeHeaders() {
    $files = $this->drupalGetTestFiles('image');
    $file = array_shift($files);
    // Copy the test file to private folder.
    $private_file = file_copy($file, 'private://', FILE_EXISTS_RENAME);
    // Tell image_module_test module to return the headers we want to test.
    variable_set('image_module_test_invalid_headers', $private_file->uri);
    // Invoke image_style_deliver so it will try to set headers.
    $generated_url = image_style_url($this->style_name, $private_file->uri);
    $this->drupalGet($generated_url);
    variable_del('image_module_test_invalid_headers');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
