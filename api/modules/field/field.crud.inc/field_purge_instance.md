# field_purge_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 979–993 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L979-L993)
- **Module/theme:** field
- **Topics:** [field_purge](../../../topics/field_purge.md)

## Signature

```php
function field_purge_instance($instance)
```

## Documentation

```text
Purges a field instance record from the database.

This function assumes all data for the instance has already been purged, and
should only be called by field_purge_batch().

@param $instance
  The instance record to purge.
```

## Code

```php
function field_purge_instance($instance) {
  db_delete('field_config_instance')
    ->condition('id', $instance['id'])
    ->execute();

  // Notify the storage engine.
  $field = field_info_field_by_id($instance['field_id']);
  module_invoke($field['storage']['module'], 'field_storage_purge_instance', $instance);

  // Clear the cache.
  field_info_cache_clear();

  // Invoke external hooks after the cache is cleared for API consistency.
  module_invoke_all('field_purge_instance', $instance);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
