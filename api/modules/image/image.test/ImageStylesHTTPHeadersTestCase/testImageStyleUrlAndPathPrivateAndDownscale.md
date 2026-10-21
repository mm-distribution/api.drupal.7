# ImageStylesHTTPHeadersTestCase::testImageStyleUrlAndPathPrivateAndDownscale()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2190–2195 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2190-L2195)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public function testImageStyleUrlAndPathPrivateAndDownscale()
```

## Documentation

```text
Test image_style_url() with a file with private scheme and downscaling.
```

## Code

```php
  public function testImageStyleUrlAndPathPrivateAndDownscale() {
    $width = 180;
    $height = 120;
    $this->_imagestyleUpscale($width, $height);
    $this->_testImageStyleUrlAndPath('private', $width, $height);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
