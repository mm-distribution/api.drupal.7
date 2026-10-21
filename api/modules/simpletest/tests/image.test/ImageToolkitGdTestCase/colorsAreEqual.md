# ImageToolkitGdTestCase::colorsAreEqual()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 230–243 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L230-L243)
- **Class:** [ImageToolkitGdTestCase](../ImageToolkitGdTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function colorsAreEqual($color_a, $color_b)
```

## Documentation

```text
Function to compare two colors by RGBa.
```

## Code

```php
  function colorsAreEqual($color_a, $color_b) {
    // Fully transparent pixels are equal, regardless of RGB.
    if ($color_a[3] == 127 && $color_b[3] == 127) {
      return TRUE;
    }

    foreach ($color_a as $key => $value) {
      if ($color_b[$key] != $value) {
        return FALSE;
      }
    }

    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
