# image_field_load()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 198–200 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L198-L200)
- **Module/theme:** image
- **Implements:** [hook_field_load()](../../field/field.api.php/hook_field_load.md)

## Signature

```php
function image_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age)
```

## Documentation

```text
Implements hook_field_load().
```

## Code

```php
function image_field_load($entity_type, $entities, $field, $instances, $langcode, &$items, $age) {
  file_field_load($entity_type, $entities, $field, $instances, $langcode, $items, $age);
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
