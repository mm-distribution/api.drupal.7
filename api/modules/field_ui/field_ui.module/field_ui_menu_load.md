# field_ui_menu_load()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 231–255 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L231-L255)
- **Module/theme:** field_ui
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_ui_menu_load($field_name, $entity_type, $bundle_name, $bundle_pos, $map)
```

## Documentation

```text
Menu loader; Load a field instance based on field and bundle name.

@param $field_name
  The name of the field, as contained in the path.
@param $entity_type
  The name of the entity.
@param $bundle_name
  The name of the bundle, as contained in the path.
@param $bundle_pos
  The position of $bundle_name in $map.
@param $map
  The translated menu router path argument map.

@return
  The field instance array.

@ingroup field
```

## Code

```php
function field_ui_menu_load($field_name, $entity_type, $bundle_name, $bundle_pos, $map) {
  // Extract the actual bundle name from the translated argument map.
  // The menu router path to manage fields of an entity can be shared among
  // multiple bundles. For example:
  // - admin/structure/types/manage/%node_type/fields/%field_ui_menu
  // - admin/structure/types/manage/%comment_node_type/fields/%field_ui_menu
  // The menu system will automatically load the correct bundle depending on the
  // actual path arguments, but this menu loader function only receives the node
  // type string as $bundle_name, which is not the bundle name for comments.
  // We therefore leverage the dynamically translated $map provided by the menu
  // system to retrieve the actual bundle and bundle name for the current path.
  if ($bundle_pos > 0) {
    $bundle = $map[$bundle_pos];
    $bundle_name = field_extract_bundle($entity_type, $bundle);
  }
  // Check whether the field exists at all.
  if ($field = field_info_field($field_name)) {
    // Only return the field if a field instance exists for the given entity
    // type and bundle.
    if ($instance = field_info_instance($entity_type, $field_name, $bundle_name)) {
      return $instance;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
