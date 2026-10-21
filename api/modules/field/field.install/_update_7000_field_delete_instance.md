# _update_7000_field_delete_instance()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 290–307 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L290-L307)
- **Module/theme:** field
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_delete_instance($field_name, $entity_type, $bundle)
```

## Documentation

```text
Utility function: delete an instance and all its data of a field stored in SQL Storage.

BEWARE: this function deletes user data from the field storage tables.

This function is valid for a database schema version 7000.

@ingroup update_api
```

## Code

```php
function _update_7000_field_delete_instance($field_name, $entity_type, $bundle) {
  // Delete field instance configuration data.
  db_delete('field_config_instance')
    ->condition('field_name', $field_name)
    ->condition('entity_type', $entity_type)
    ->condition('bundle', $bundle)
    ->execute();

  // Nuke data.
  db_delete('field_data_' . $field_name)
    ->condition('entity_type', $entity_type)
    ->condition('bundle', $bundle)
    ->execute();
  db_delete('field_revision_' . $field_name)
    ->condition('entity_type', $entity_type)
    ->condition('bundle', $bundle)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
