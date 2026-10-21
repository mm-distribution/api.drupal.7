# image_test_settings()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 77–80 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L77-L80)
- **Module/theme:** batch_test

## Signature

```php
function image_test_settings()
```

## Documentation

```text
Image tookit's settings operation.
```

## Code

```php
function image_test_settings() {
  _image_test_log_call('settings', array());
  return array();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
