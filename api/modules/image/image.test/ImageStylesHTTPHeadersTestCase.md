# ImageStylesHTTPHeadersTestCase

- **Type:** Class
- **File:** [`modules/image/image.test`](_file.md), lines 2116–2267 · [local source](../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L2116-L2267)
- **Module/theme:** image

## Signature

```php
class ImageStylesHTTPHeadersTestCase extends ImageFieldTestCase
```

## Documentation

```text
Tests for correct file size, dimensions and HTTP headers after scaling.
```

## Properties

### $styleName

```php
protected $styleName;
```

```text
Generated style name.

@var string
```

### $styleId

```php
protected $styleId;
```

```text
ID of generated style.

@var int
```

## Methods (derived index)

- [getInfo()](ImageStylesHTTPHeadersTestCase/getInfo.md) — {@inheritdoc}
- [setUp()](ImageStylesHTTPHeadersTestCase/setUp.md) — {@inheritdoc}
- [testImageStyleUrlAndPathPublicAndUpscale()](ImageStylesHTTPHeadersTestCase/testImageStyleUrlAndPathPublicAndUpscale.md) — Test image_style_url() with a file with public scheme and upscaling.
- [testImageStyleUrlAndPathPrivateAndUpscale()](ImageStylesHTTPHeadersTestCase/testImageStyleUrlAndPathPrivateAndUpscale.md) — Test image_style_url() with a file with private scheme and upscaling.
- [testImageStyleUrlAndPathPublicAndDownscale()](ImageStylesHTTPHeadersTestCase/testImageStyleUrlAndPathPublicAndDownscale.md) — Test image_style_url() with a file with public scheme and downscaling.
- [testImageStyleUrlAndPathPrivateAndDownscale()](ImageStylesHTTPHeadersTestCase/testImageStyleUrlAndPathPrivateAndDownscale.md) — Test image_style_url() with a file with private scheme and downscaling.
- [_imagestyleUpscale()](ImageStylesHTTPHeadersTestCase/_imagestyleUpscale.md) — Adding upscale effect to imagestyle.
- [_testImageStyleUrlAndPath()](ImageStylesHTTPHeadersTestCase/_testImageStyleUrlAndPath.md) — Function to scale and test.

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
