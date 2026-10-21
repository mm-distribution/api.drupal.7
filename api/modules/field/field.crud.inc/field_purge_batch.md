# field_purge_batch()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 896–936 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L896-L936)
- **Module/theme:** field
- **Topics:** [field_purge](../../../topics/field_purge.md)

## Signature

```php
function field_purge_batch($batch_size)
```

## Documentation

```text
Purges a batch of deleted Field API data, instances, or fields.

This function will purge deleted field data in batches. The batch size
is defined as an argument to the function, and once each batch is finished,
it continues with the next batch until all have completed. If a deleted field
instance with no remaining data records is found, the instance itself will
be purged. If a deleted field with no remaining field instances is found, the
field itself will be purged.

@param $batch_size
  The maximum number of field data records to purge before returning.
```

## Code

```php
function field_purge_batch($batch_size) {
  // Retrieve all deleted field instances. We cannot use field_info_instances()
  // because that function does not return deleted instances.
  $instances = field_read_instances(array('deleted' => 1), array('include_deleted' => 1));

  foreach ($instances as $instance) {
    // field_purge_data() will need the field array.
    $field = field_info_field_by_id($instance['field_id']);
    // Retrieve some entities.
    $query = new EntityFieldQuery();
    $results = $query
      ->fieldCondition($field)
      ->entityCondition('bundle', $instance['bundle'])
      ->deleted(TRUE)
      ->range(0, $batch_size)
      ->execute();

    if ($results) {
      foreach ($results as $entity_type => $stub_entities) {
        field_attach_load($entity_type, $stub_entities, FIELD_LOAD_CURRENT, array('field_id' => $field['id'], 'deleted' => 1));
        foreach ($stub_entities as $stub_entity) {
          // Purge the data for the entity.
          field_purge_data($entity_type, $stub_entity, $field, $instance);
        }
      }
    }
    else {
      // No field data remains for the instance, so we can remove it.
      field_purge_instance($instance);
    }
  }

  // Retrieve all deleted fields. Any that have no instances can be purged.
  $fields = field_read_fields(array('deleted' => 1), array('include_deleted' => 1));
  foreach ($fields as $field) {
    $instances = field_read_instances(array('field_id' => $field['id']), array('include_deleted' => 1));
    if (empty($instances)) {
      field_purge_field($field);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
