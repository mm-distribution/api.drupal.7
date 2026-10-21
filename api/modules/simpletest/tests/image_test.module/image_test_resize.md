# image_test_resize()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 119–122 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L119-L122)
- **Module/theme:** batch_test

## Signature

```php
function image_test_resize(stdClass $image, $width, $height)
```

## Documentation

```text
Image tookit's resize operation.
```

## Code

```php
function image_test_resize(stdClass $image, $width, $height) {
  _image_test_log_call('resize', array($image, $width, $height));
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
