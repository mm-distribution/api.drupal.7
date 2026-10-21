# ImageStylesHTTPHeadersTestCase::testImageStyleUrlAndPathPublicAndUpscale()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2160–2165 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2160-L2165)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public function testImageStyleUrlAndPathPublicAndUpscale()
```

## Documentation

```text
Test image_style_url() with a file with public scheme and upscaling.
```

## Code

```php
  public function testImageStyleUrlAndPathPublicAndUpscale() {
    $width = 3600;
    $height = 2400;
    $this->_imagestyleUpscale($width, $height);
    $this->_testImageStyleUrlAndPath('public', $width, $height);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
