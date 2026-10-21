# image_module_test_file_download()

- **Type:** Function
- **File:** [`modules/image/tests/image_module_test.module`](_file.md), lines 8–15 · [local source](../../../../../source/modules/image/tests/image_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module#L8-L15)
- **Module/theme:** image_module_styles_test

## Signature

```php
function image_module_test_file_download($uri)
```

## Documentation

_No docblock in source._

## Code

```php
function image_module_test_file_download($uri) {
  if (variable_get('image_module_test_file_download', FALSE) == $uri) {
    return array('X-Image-Owned-By' => 'image_module_test');
  }
  if (variable_get('image_module_test_invalid_headers', FALSE) == $uri) {
    return array('Content-Type' => 'image/png');
  }
}
```

---
_Drupal 7.103 · [modules/image/tests/image_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/image/tests/image_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
