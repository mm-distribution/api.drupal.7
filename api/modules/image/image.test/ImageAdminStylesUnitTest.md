# ImageAdminStylesUnitTest

- **Type:** Class
- **File:** [`modules/image/image.test`](_file.md), lines 571–936 · [local source](../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L571-L936)
- **Module/theme:** image

## Signature

```php
class ImageAdminStylesUnitTest extends ImageFieldTestCase
```

## Documentation

```text
Tests creation, deletion, and editing of image styles and effects.
```

## Methods (derived index)

- [getInfo()](ImageAdminStylesUnitTest/getInfo.md)
- [setUp()](ImageAdminStylesUnitTest/setUp.md)
- [createSampleImage()](ImageAdminStylesUnitTest/createSampleImage.md) — Given an image style, generate an image.
- [getImageCount()](ImageAdminStylesUnitTest/getImageCount.md) — Count the number of images currently create for a style.
- [testNumericStyleName()](ImageAdminStylesUnitTest/testNumericStyleName.md) — Test creating an image style with a numeric name and ensuring it can be applied to an image.
- [testStyle()](ImageAdminStylesUnitTest/testStyle.md) — General test to add a style, add/remove/edit effects to it, then delete it.
- [testDefaultStyle()](ImageAdminStylesUnitTest/testDefaultStyle.md) — Test to override, edit, then revert a style.
- [testStyleReplacement()](ImageAdminStylesUnitTest/testStyleReplacement.md) — Test deleting a style and choosing a replacement style.
- [testOrphanedEffect()](ImageAdminStylesUnitTest/testOrphanedEffect.md) — Test disabling a module providing an effect in use by an image style.

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
