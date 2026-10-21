# image_style_add_form_name_exists()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 279–281 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L279-L281)
- **Module/theme:** image

## Signature

```php
function image_style_add_form_name_exists($name)
```

## Documentation

```text
Check if the proposed machine name is already taken.

@param string $name
  An image style machine name.

@return bool
  TRUE if the image style machine name already exists, FALSE otherwise.
```

## Code

```php
function image_style_add_form_name_exists($name) {
  return (bool) image_style_load($name);
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
