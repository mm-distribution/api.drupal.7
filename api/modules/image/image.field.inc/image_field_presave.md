# image_field_presave()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 234–248 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L234-L248)
- **Module/theme:** image
- **Implements:** [hook_field_presave()](../../field/field.api.php/hook_field_presave.md)

## Signature

```php
function image_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_presave().
```

## Code

```php
function image_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items) {
  file_field_presave($entity_type, $entity, $field, $instance, $langcode, $items);

  // Determine the dimensions if necessary.
  foreach ($items as &$item) {
    if (!isset($item['width']) || !isset($item['height'])) {
      $info = image_get_info(file_load($item['fid'])->uri);

      if (is_array($info)) {
        $item['width'] = $info['width'];
        $item['height'] = $info['height'];
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
