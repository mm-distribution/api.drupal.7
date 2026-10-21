# image_field_is_empty()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 281–283 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L281-L283)
- **Module/theme:** image
- **Implements:** [hook_field_is_empty()](../../field/field.api.php/hook_field_is_empty.md)

## Signature

```php
function image_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function image_field_is_empty($item, $field) {
  return file_field_is_empty($item, $field);
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
