# _field_invoke_get_instances()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 420–453 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L420-L453)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function _field_invoke_get_instances($entity_type, $bundle, $options)
```

## Documentation

```text
Helper for _field_invoke(): retrieves a list of instances to operate on.

@param $entity_type
  The entity type.
@param $bundle
  The bundle name.
@param $options
  An associative array of options, as provided to _field_invoke(). Only the
  following keys are considered :
  - deleted
  - field_name
  - field_id
  See _field_invoke() for details.

@return
  The array of selected instance definitions.
```

## Code

```php
function _field_invoke_get_instances($entity_type, $bundle, $options) {
  if ($options['deleted']) {
    // Deleted fields are not included in field_info_instances(), and need to
    // be fetched from the database with field_read_instances().
    $params = array('entity_type' => $entity_type, 'bundle' => $bundle);
    if (isset($options['field_id'])) {
      // Single-field mode by field id: field_read_instances() does the filtering.
      // Single-field mode by field name is not compatible with the 'deleted'
      // option.
      $params['field_id'] = $options['field_id'];
    }
    $instances = field_read_instances($params, array('include_deleted' => TRUE));
  }
  elseif (isset($options['field_name'])) {
    // Single-field mode by field name: field_info_instance() does the
    // filtering.
    $instances = array(field_info_instance($entity_type, $options['field_name'], $bundle));
  }
  else {
    $instances = field_info_instances($entity_type, $bundle);
    if (isset($options['field_id'])) {
      // Single-field mode by field id: we need to loop on each instance to
      // find the right one.
      foreach ($instances as $instance) {
        if ($instance['field_id'] == $options['field_id']) {
          $instances = array($instance);
          break;
        }
      }
    }
  }

  return $instances;
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
