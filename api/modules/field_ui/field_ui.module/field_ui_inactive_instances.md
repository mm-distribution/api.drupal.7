# field_ui_inactive_instances()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 349–378 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L349-L378)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_inactive_instances($entity_type, $bundle_name = NULL)
```

## Documentation

```text
Identifies inactive fields within a bundle.
```

## Code

```php
function field_ui_inactive_instances($entity_type, $bundle_name = NULL) {
  $params = array('entity_type' => $entity_type);

  if (empty($bundle_name)) {
    $active = field_info_instances($entity_type);
    $inactive = array();
  }
  else {
    // Restrict to the specified bundle. For consistency with the case where
    // $bundle_name is NULL, the $active and  $inactive arrays are keyed by
    // bundle name first.
    $params['bundle'] = $bundle_name;
    $active = array($bundle_name => field_info_instances($entity_type, $bundle_name));
    $inactive = array($bundle_name => array());
  }

  // Iterate on existing definitions, and spot those that do not appear in the
  // $active list collected earlier.
  $all_instances = field_read_instances($params, array('include_inactive' => TRUE));
  foreach ($all_instances as $instance) {
    if (!isset($active[$instance['bundle']][$instance['field_name']])) {
      $inactive[$instance['bundle']][$instance['field_name']] = $instance;
    }
  }

  if (!empty($bundle_name)) {
    return $inactive[$bundle_name];
  }
  return $inactive;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
