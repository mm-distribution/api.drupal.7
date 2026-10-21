# image_field_delete_revision()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 274–276 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L274-L276)
- **Module/theme:** image
- **Implements:** [hook_field_delete_revision()](../../field/field.api.php/hook_field_delete_revision.md)

## Signature

```php
function image_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_delete_revision().
```

## Code

```php
function image_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, &$items) {
  file_field_delete_revision($entity_type, $entity, $field, $instance, $langcode, $items);
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
