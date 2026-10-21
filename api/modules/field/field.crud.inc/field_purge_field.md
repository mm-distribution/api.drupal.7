# field_purge_field()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 1004–1022 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L1004-L1022)
- **Module/theme:** field
- **Topics:** [field_purge](../../../topics/field_purge.md)

## Signature

```php
function field_purge_field($field)
```

## Documentation

```text
Purges a field record from the database.

This function assumes all instances for the field has already been purged,
and should only be called by field_purge_batch().

@param $field
  The field record to purge.
```

## Code

```php
function field_purge_field($field) {
  $instances = field_read_instances(array('field_id' => $field['id']), array('include_deleted' => 1));
  if (count($instances) > 0) {
    throw new FieldException(t('Attempt to purge a field @field_name that still has instances.', array('@field_name' => $field['field_name'])));
  }

  db_delete('field_config')
    ->condition('id', $field['id'])
    ->execute();

  // Notify the storage engine.
  module_invoke($field['storage']['module'], 'field_storage_purge_field', $field);

  // Clear the cache.
  field_info_cache_clear();

  // Invoke external hooks after the cache is cleared for API consistency.
  module_invoke_all('field_purge_field', $field);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
