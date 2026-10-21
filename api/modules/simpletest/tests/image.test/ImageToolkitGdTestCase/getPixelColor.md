# ImageToolkitGdTestCase::getPixelColor()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 248–257 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L248-L257)
- **Class:** [ImageToolkitGdTestCase](../ImageToolkitGdTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function getPixelColor($image, $x, $y)
```

## Documentation

```text
Function for finding a pixel's RGBa values.
```

## Code

```php
  function getPixelColor($image, $x, $y) {
    $color_index = imagecolorat($image->resource, $x, $y);

    $transparent_index = imagecolortransparent($image->resource);
    if ($color_index == $transparent_index) {
      return array(0, 0, 0, 127);
    }

    return array_values(imagecolorsforindex($image->resource, $color_index));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
