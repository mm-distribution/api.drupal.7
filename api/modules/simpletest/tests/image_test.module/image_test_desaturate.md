# image_test_desaturate()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 135–138 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L135-L138)
- **Module/theme:** batch_test

## Signature

```php
function image_test_desaturate(stdClass $image)
```

## Documentation

```text
Image tookit's desaturate operation.
```

## Code

```php
function image_test_desaturate(stdClass $image) {
  _image_test_log_call('desaturate', array($image));
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
