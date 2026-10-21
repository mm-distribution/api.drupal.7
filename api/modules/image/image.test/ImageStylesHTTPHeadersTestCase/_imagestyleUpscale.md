# ImageStylesHTTPHeadersTestCase::_imagestyleUpscale()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 2200–2212 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2200-L2212)
- **Class:** [ImageStylesHTTPHeadersTestCase](../ImageStylesHTTPHeadersTestCase.md)
- **Module/theme:** image

## Signature

```php
private function _imagestyleUpscale($width, $height)
```

## Documentation

```text
Adding upscale effect to imagestyle.
```

## Code

```php
  private function _imagestyleUpscale($width, $height) {
    // Scale an image that is wider than it is high.
    $effect = array(
      'name' => 'image_scale',
      'data' => array(
        'width' => $width,
        'height' => $height,
        'upscale' => TRUE,
      ),
      'isid' => $this->styleId,
    );
    image_effect_save($effect);
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
