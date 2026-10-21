# image_field_prepare_view()

- **Type:** Function
- **File:** [`modules/image/image.field.inc`](_file.md), lines 205–229 · [local source](../../../../source/modules/image/image.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc#L205-L229)
- **Module/theme:** image
- **Implements:** [hook_field_prepare_view()](../../field/field.api.php/hook_field_prepare_view.md)

## Signature

```php
function image_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_prepare_view().
```

## Code

```php
function image_field_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items) {
  // If there are no files specified at all, use the default.
  foreach ($entities as $id => $entity) {
    if (empty($items[$id])) {
      $fid = 0;
      // Use the default for the instance if one is available.
      if (!empty($instances[$id]['settings']['default_image'])) {
        $fid = $instances[$id]['settings']['default_image'];
      }
      // Otherwise, use the default for the field.
      elseif (!empty($field['settings']['default_image'])) {
        $fid = $field['settings']['default_image'];
      }

      // Add the default image if one is found.
      if ($fid && ($file = file_load($fid))) {
        $items[$id][0] = (array) $file + array(
          'is_default' => TRUE,
          'alt' => '',
          'title' => '',
        );
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
