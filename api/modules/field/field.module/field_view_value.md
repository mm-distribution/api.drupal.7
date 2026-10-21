# field_view_value()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 796–817 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L796-L817)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_view_value($entity_type, $entity, $field_name, $item, $display = array(), $langcode = NULL)
```

## Documentation

```text
Returns a renderable array for a single field value.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  The entity containing the field to display. Must at least contain the id
  key and the field data to display.
@param $field_name
  The name of the field to display.
@param $item
  The field value to display, as found in
  $entity->field_name[$langcode][$delta].
@param $display
  Can be either the name of a view mode, or an array of display settings.
  See field_view_field() for more information.
@param $langcode
  (Optional) The language of the value in $item. If not provided, the
  current language will be assumed.
@return
  A renderable array for the field value.
```

## Code

```php
function field_view_value($entity_type, $entity, $field_name, $item, $display = array(), $langcode = NULL) {
  $output = array();

  if ($field = field_info_field($field_name)) {
    // Determine the langcode that will be used by language fallback.
    $langcode = field_language($entity_type, $entity, $field_name, $langcode);

    // Push the item as the single value for the field, and defer to
    // field_view_field() to build the render array for the whole field.
    $clone = clone $entity;
    $clone->{$field_name}[$langcode] = array($item);
    $elements = field_view_field($entity_type, $clone, $field_name, $display, $langcode);

    // Extract the part of the render array we need.
    $output = isset($elements[0]) ? $elements[0] : array();
    if (isset($elements['#access'])) {
      $output['#access'] = $elements['#access'];
    }
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
