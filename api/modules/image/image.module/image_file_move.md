# image_file_move()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 330–333 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L330-L333)
- **Module/theme:** image
- **Implements:** [hook_file_move()](../../system/system.api.php/hook_file_move.md)

## Signature

```php
function image_file_move($file, $source)
```

## Documentation

```text
Implements hook_file_move().
```

## Code

```php
function image_file_move($file, $source) {
  // Delete any image derivatives at the original image path.
  image_path_flush($source->uri);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
