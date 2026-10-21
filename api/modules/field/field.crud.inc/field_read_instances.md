# field_read_instances()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 728–772 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L728-L772)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_read_instances($params = array(), $include_additional = array())
```

## Documentation

```text
Reads in field instances that match an array of conditions.

@param $param
  An array of properties to use in selecting a field
  instance. Valid keys include any column of the
  field_config_instance table. If NULL, all instances will be returned.
@param $include_additional
  The default behavior of this function is to not return field
  instances that have been marked deleted, or whose field is inactive.
  Setting $include_additional['include_inactive'] or
  $include_additional['include_deleted'] to TRUE will override this
  behavior.
@return
  An array of instances matching the arguments.
```

## Code

```php
function field_read_instances($params = array(), $include_additional = array()) {
  $include_inactive = isset($include_additional['include_inactive']) && $include_additional['include_inactive'];
  $include_deleted = isset($include_additional['include_deleted']) && $include_additional['include_deleted'];

  $query = db_select('field_config_instance', 'fci', array('fetch' => PDO::FETCH_ASSOC));
  $query->join('field_config', 'fc', 'fc.id = fci.field_id');
  $query->fields('fci');

  // Turn the conditions into a query.
  foreach ($params as $key => $value) {
    $query->condition('fci.' . $key, $value);
  }
  if (!$include_inactive) {
    $query
      ->condition('fc.active', 1)
      ->condition('fc.storage_active', 1);
  }
  if (!$include_deleted) {
    $query->condition('fc.deleted', 0);
    $query->condition('fci.deleted', 0);
  }

  $instances = array();
  $query->orderBy('fci.id');
  $results = $query->execute();

  foreach ($results as $record) {
    // Filter out instances on unknown entity types (for instance because the
    // module exposing them was disabled).
    $entity_info = entity_get_info($record['entity_type']);
    if ($include_inactive || $entity_info) {
      $instance = unserialize($record['data']);
      $instance['id'] = $record['id'];
      $instance['field_id'] = $record['field_id'];
      $instance['field_name'] = $record['field_name'];
      $instance['entity_type'] = $record['entity_type'];
      $instance['bundle'] = $record['bundle'];
      $instance['deleted'] = $record['deleted'];

      module_invoke_all('field_read_instance', $instance);
      $instances[] = $instance;
    }
  }
  return $instances;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
