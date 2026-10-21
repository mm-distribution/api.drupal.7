# image_test_load()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 93–96 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L93-L96)
- **Module/theme:** batch_test

## Signature

```php
function image_test_load(stdClass $image)
```

## Documentation

```text
Image tookit's load operation.
```

## Code

```php
function image_test_load(stdClass $image) {
  _image_test_log_call('load', array($image));
  return $image;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
