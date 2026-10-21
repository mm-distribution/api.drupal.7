# ImageStylesPathAndUrlTestCase

- **Type:** Class
- **File:** [`modules/image/image.test`](_file.md), lines 130–392 · [local source](../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L130-L392)
- **Module/theme:** image

## Signature

```php
class ImageStylesPathAndUrlTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the functions for generating paths and URLs for image styles.
```

## Properties

### $style_name

```php
protected $style_name;
```

### $image_info

```php
protected $image_info;
```

### $image_filepath

```php
protected $image_filepath;
```

## Methods (derived index)

- [getInfo()](ImageStylesPathAndUrlTestCase/getInfo.md)
- [setUp()](ImageStylesPathAndUrlTestCase/setUp.md)
- [testImageStylePath()](ImageStylesPathAndUrlTestCase/testImageStylePath.md) — Test image_style_path().
- [testImageStyleUrlAndPathPublic()](ImageStylesPathAndUrlTestCase/testImageStyleUrlAndPathPublic.md) — Test image_style_url() with a file using the "public://" scheme.
- [testImageStyleUrlAndPathPrivate()](ImageStylesPathAndUrlTestCase/testImageStyleUrlAndPathPrivate.md) — Test image_style_url() with a file using the "private://" scheme.
- [testImageStylUrlAndPathPublicUnclean()](ImageStylesPathAndUrlTestCase/testImageStylUrlAndPathPublicUnclean.md) — Test image_style_url() with the "public://" scheme and unclean URLs.
- [testImageStyleUrlAndPathPrivateUnclean()](ImageStylesPathAndUrlTestCase/testImageStyleUrlAndPathPrivateUnclean.md) — Test image_style_url() with the "private://" schema and unclean URLs.
- [testImageStyleUrlExtraSlash()](ImageStylesPathAndUrlTestCase/testImageStyleUrlExtraSlash.md) — Test image_style_url() with a file URL that has an extra slash in it.
- [testImageStyleUrlForMissingSourceImage()](ImageStylesPathAndUrlTestCase/testImageStyleUrlForMissingSourceImage.md) — Test that an invalid source image returns a 404.
- [testImageContentTypeHeaders()](ImageStylesPathAndUrlTestCase/testImageContentTypeHeaders.md) — Test that we do not pass an array to drupal_add_http_header.
- [_testImageStyleUrlAndPath()](ImageStylesPathAndUrlTestCase/_testImageStyleUrlAndPath.md) — Test image_style_url().

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
