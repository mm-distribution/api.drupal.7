# ImageStyleFlushTest::createSampleImage()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2023–2038 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2023-L2038)
- **Class:** [ImageStyleFlushTest](../ImageStyleFlushTest.md)
- **Module/theme:** image

## Signature

```php
function createSampleImage($style, $wrapper)
```

## Documentation

```text
Given an image style and a wrapper, generate an image.
```

## Code

```php
  function createSampleImage($style, $wrapper) {
    static $file;

    if (!isset($file)) {
      $files = $this->drupalGetTestFiles('image');
      $file = reset($files);
    }

    // Make sure we have an image in our wrapper testing file directory.
    $source_uri = file_unmanaged_copy($file->uri, $wrapper . '://');
    // Build the derivative image.
    $derivative_uri = image_style_path($style['name'], $source_uri);
    $derivative = image_style_create_derivative($style, $source_uri, $derivative_uri);

    return $derivative ? $derivative_uri : FALSE;
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
