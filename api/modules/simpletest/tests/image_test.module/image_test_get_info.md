# image_test_get_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 85–88 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L85-L88)
- **Module/theme:** batch_test

## Signature

```php
function image_test_get_info(stdClass $image)
```

## Documentation

```text
Image toolkit's get_info operation.
```

## Code

```php
function image_test_get_info(stdClass $image) {
  _image_test_log_call('get_info', array($image));
  return array();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
