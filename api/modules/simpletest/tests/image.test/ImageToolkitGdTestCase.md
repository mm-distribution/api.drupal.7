# ImageToolkitGdTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/image.test`](_file.md), lines 203–539 · [local source](../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L203-L539)
- **Module/theme:** batch_test

## Signature

```php
class ImageToolkitGdTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test the core GD image manipulation functions.
```

## Properties

### $black

```php
protected $black       = array(0, 0, 0, 0);
```

### $red

```php
protected $red         = array(255, 0, 0, 0);
```

### $green

```php
protected $green       = array(0, 255, 0, 0);
```

### $blue

```php
protected $blue        = array(0, 0, 255, 0);
```

### $yellow

```php
protected $yellow      = array(255, 255, 0, 0);
```

### $white

```php
protected $white       = array(255, 255, 255, 0);
```

### $transparent

```php
protected $transparent = array(0, 0, 0, 127);
```

### $fuchsia

```php
protected $fuchsia            = array(255, 0, 255, 0);
```

### $rotate_transparent

```php
protected $rotate_transparent = array(255, 255, 255, 127);
```

### $width

```php
protected $width = 40;
```

### $height

```php
protected $height = 20;
```

## Methods (derived index)

- [getInfo()](ImageToolkitGdTestCase/getInfo.md)
- [colorsAreEqual()](ImageToolkitGdTestCase/colorsAreEqual.md) — Function to compare two colors by RGBa.
- [getPixelColor()](ImageToolkitGdTestCase/getPixelColor.md) — Function for finding a pixel's RGBa values.
- [testManipulations()](ImageToolkitGdTestCase/testManipulations.md) — Since PHP can't visually check that our images have been manipulated properly, build a list of expected color values for each of the corners and the expected height and widths for the final images.
- [testTransparentColorOutOfRange()](ImageToolkitGdTestCase/testTransparentColorOutOfRange.md) — Tests loading an image whose transparent color index is out of range.

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
