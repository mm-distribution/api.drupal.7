# image_test_rotate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 127–130 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L127-L130)
- **Module/theme:** batch_test

## Signature

```php
function image_test_rotate(stdClass $image, $degrees, $background = NULL)
```

## Documentation

```text
Image tookit's rotate operation.
```

## Code

```php
function image_test_rotate(stdClass $image, $degrees, $background = NULL) {
  _image_test_log_call('rotate', array($image, $degrees, $background));
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
