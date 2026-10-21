# field_ui_existing_field_options()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1536–1569 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1536-L1569)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_existing_field_options($entity_type, $bundle)
```

## Documentation

```text
Returns an array of existing fields to be added to a bundle.
```

## Code

```php
function field_ui_existing_field_options($entity_type, $bundle) {
  $info = array();
  $field_types = field_info_field_types();

  foreach (field_info_instances() as $existing_entity_type => $bundles) {
    foreach ($bundles as $existing_bundle => $instances) {
      // No need to look in the current bundle.
      if (!($existing_bundle == $bundle && $existing_entity_type == $entity_type)) {
        foreach ($instances as $instance) {
          $field = field_info_field($instance['field_name']);
          // Don't show
          // - locked fields,
          // - fields already in the current bundle,
          // - fields that cannot be added to the entity type,
          // - fields that should not be added via user interface.

          if (empty($field['locked'])
            && !field_info_instance($entity_type, $field['field_name'], $bundle)
            && (empty($field['entity_types']) || in_array($entity_type, $field['entity_types']))
            && empty($field_types[$field['type']]['no_ui'])) {
            $info[$instance['field_name']] = array(
              'type' => $field['type'],
              'type_label' => $field_types[$field['type']]['label'],
              'field' => $field['field_name'],
              'label' => $instance['label'],
              'widget_type' => $instance['widget']['type'],
            );
          }
        }
      }
    }
  }
  return $info;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
