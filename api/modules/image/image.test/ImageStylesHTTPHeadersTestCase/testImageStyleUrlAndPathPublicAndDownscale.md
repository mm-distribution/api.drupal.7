# ImageStylesHTTPHeadersTestCase::testImageStyleUrlAndPathPublicAndDownscale()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2180–2185 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2180-L2185)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public function testImageStyleUrlAndPathPublicAndDownscale()
```

## Documentation

```text
Test image_style_url() with a file with public scheme and downscaling.
```

## Code

```php
  public function testImageStyleUrlAndPathPublicAndDownscale() {
    $width = 180;
    $height = 120;
    $this->_imagestyleUpscale($width, $height);
    $this->_testImageStyleUrlAndPath('public', $width, $height);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
