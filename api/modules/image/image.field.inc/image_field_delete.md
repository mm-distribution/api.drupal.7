# image_field_delete()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 267–269 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L267-L269)
- **Module/theme:** image
- **Implements:** [hook_field_delete()](../../field/field.api.php/hook_field_delete.md)

## Signature

```php
function image_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_delete().
```

## Code

```php
function image_field_delete($entity_type, $entity, $field, $instance, $langcode, &$items) {
  file_field_delete($entity_type, $entity, $field, $instance, $langcode, $items);
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
