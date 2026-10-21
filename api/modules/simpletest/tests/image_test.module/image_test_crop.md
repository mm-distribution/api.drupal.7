# image_test_crop()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 111–114 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L111-L114)
- **Module/theme:** batch_test

## Signature

```php
function image_test_crop(stdClass $image, $x, $y, $width, $height)
```

## Documentation

```text
Image tookit's crop operation.
```

## Code

```php
function image_test_crop(stdClass $image, $x, $y, $width, $height) {
  _image_test_log_call('crop', array($image, $x, $y, $width, $height));
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
