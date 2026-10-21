# ImageAdminStylesUnitTest::createSampleImage()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 588–600 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L588-L600)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function createSampleImage($style)
```

## Documentation

```text
Given an image style, generate an image.
```

## Code

```php
  function createSampleImage($style) {
    static $file_path;

    // First, we need to make sure we have an image in our testing
    // file directory. Copy over an image on the first run.
    if (!isset($file_path)) {
      $files = $this->drupalGetTestFiles('image');
      $file = reset($files);
      $file_path = file_unmanaged_copy($file->uri);
    }

    return image_style_url($style['name'], $file_path) ? $file_path : FALSE;
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
