# ImageStylesHTTPHeadersTestCase::testImageStyleUrlAndPathPrivateAndUpscale()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2170–2175 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2170-L2175)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
public function testImageStyleUrlAndPathPrivateAndUpscale()
```

## Documentation

```text
Test image_style_url() with a file with private scheme and upscaling.
```

## Code

```php
  public function testImageStyleUrlAndPathPrivateAndUpscale() {
    $width = 3600;
    $height = 2400;
    $this->_imagestyleUpscale($width, $height);
    $this->_testImageStyleUrlAndPath('private', $width, $height);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
