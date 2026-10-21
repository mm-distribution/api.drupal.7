# field_default_prepare_view()

- **Type:** Function
- **File:** [`modules/field/field.default.inc`](_file.md), lines 138–168 · [local source](../../../../source/modules/field/field.default.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc#L138-L168)
- **Module/theme:** field

## Signature

```php
function field_default_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $display)
```

## Documentation

```text
Invokes hook_field_formatter_prepare_view() on the relevant formatters.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entities
  An array of entities being displayed, keyed by entity id.
@param $field
  The field structure for the operation.
@param $instances
  Array of instance structures for $field for each entity, keyed by entity
  id.
@param $langcode
  The language associated to $items.
@param $items
  Array of field values already loaded for the entities, keyed by entity id.
@param $display
  Can be either:
  - the name of a view mode
  - or an array of display settings to use for display, as found in the
    'display' entry of $instance definitions.
```

## Code

```php
function field_default_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $display) {
  // Group entities, instances and items by formatter module.
  $modules = array();
  foreach ($instances as $id => $instance) {
    if (is_string($display)) {
      $view_mode = $display;
      $instance_display = field_get_display($instance, $view_mode, $entities[$id]);
    }
    else {
      $instance_display = $display;
    }

    if ($instance_display['type'] !== 'hidden') {
      $module = $instance_display['module'];
      $modules[$module] = $module;
      $grouped_entities[$module][$id] = $entities[$id];
      $grouped_instances[$module][$id] = $instance;
      $grouped_displays[$module][$id] = $instance_display;
      // hook_field_formatter_prepare_view() alters $items by reference.
      $grouped_items[$module][$id] = &$items[$id];
    }
  }

  foreach ($modules as $module) {
    // Invoke hook_field_formatter_prepare_view().
    $function = $module . '_field_formatter_prepare_view';
    if (function_exists($function)) {
      $function($entity_type, $grouped_entities[$module], $field, $grouped_instances[$module], $langcode, $grouped_items[$module], $grouped_displays[$module]);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/field.default.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.default.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
