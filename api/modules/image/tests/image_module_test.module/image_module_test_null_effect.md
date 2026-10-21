# image_module_test_null_effect()

- **Type:** Function
- **File:** [`modules/image/tests/image_module_test.module`](_file.md), lines 42–44 · [local source](../../../../../source/modules/image/tests/image_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module#L42-L44)
- **Module/theme:** image_module_styles_test

## Signature

```php
function image_module_test_null_effect(&$image, array $data)
```

## Documentation

```text
Image effect callback; Null.

@param $image
  An image object returned by image_load().
@param $data
  An array with no attributes.

@return
  TRUE
```

## Code

```php
function image_module_test_null_effect(&$image, array $data) {
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/tests/image_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
