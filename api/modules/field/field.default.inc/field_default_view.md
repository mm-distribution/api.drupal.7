# field_default_view()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 191–237 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L191-L237)
- **Module/theme:** field

## Signature

```php
function field_default_view($entity_type, $entity, $field, $instance, $langcode, $items, $display)
```

## Documentation

```text
Builds a renderable array for one field on one entity instance.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  A single object of type $entity_type.
@param $field
  The field structure for the operation.
@param $instance
  An array containing each field on $entity's bundle.
@param $langcode
  The language associated to $items.
@param $items
  Array of field values already loaded for the entities, keyed by entity id.
@param $display
  Can be either:
  - the name of a view mode;
  - or an array of custom display settings, as found in the 'display' entry
    of $instance definitions.
```

## Code

```php
function field_default_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  $addition = array();

  // Prepare incoming display specifications.
  if (is_string($display)) {
    $view_mode = $display;
    $display = field_get_display($instance, $view_mode, $entity);
  }
  else {
    $view_mode = '_custom_display';
  }

  if ($display['type'] !== 'hidden') {
    // Calling the formatter function through module_invoke() can have a
    // performance impact on pages with many fields and values.
    $function = $display['module'] . '_field_formatter_view';
    if (function_exists($function)) {
      $elements = $function($entity_type, $entity, $field, $instance, $langcode, $items, $display);

      if ($elements) {
        $info = array(
          '#theme' => 'field',
          '#weight' => $display['weight'],
          '#title' => $instance['label'],
          '#access' => field_access('view', $field, $entity_type, $entity),
          '#label_display' => $display['label'],
          '#view_mode' => $view_mode,
          '#language' => $langcode,
          '#field_name' => $field['field_name'],
          '#field_type' => $field['type'],
          '#field_translatable' => $field['translatable'],
          '#entity_type' => $entity_type,
          '#bundle' => $bundle,
          '#object' => $entity,
          '#items' => $items,
          '#formatter' => $display['type']
        );

        $addition[$field['field_name']] = array_merge($info, $elements);
      }
    }
  }

  return $addition;
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
