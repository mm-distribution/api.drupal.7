# _update_7000_field_create_instance()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 364–389 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L364-L389)
- **Module/theme:** field
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_create_instance($field, &$instance)
```

## Documentation

```text
Utility function: write a field instance directly to the database.

This function can be used for databases whose schema is at field module
version 7000 or higher.

@ingroup update_api
```

## Code

```php
function _update_7000_field_create_instance($field, &$instance) {
  // Merge in defaults.
  $instance += array(
    'field_id' => $field['id'],
    'field_name' => $field['field_name'],
    'deleted' => 0,
  );

  // The serialized 'data' column contains everything from $instance that does
  // not have its own column and is not automatically populated when the
  // instance is read.
  $data = $instance;
  unset($data['id'], $data['field_id'], $data['field_name'], $data['entity_type'], $data['bundle'], $data['deleted']);

  $record = array(
    'field_id' => $instance['field_id'],
    'field_name' => $instance['field_name'],
    'entity_type' => $instance['entity_type'],
    'bundle' => $instance['bundle'],
    'data' => serialize($data),
    'deleted' => (int) $instance['deleted'],
  );
  $instance['id'] = db_insert('field_config_instance')
    ->fields($record)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
