# _update_7000_field_delete_field()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 259–278 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L259-L278)
- **Module/theme:** field
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_delete_field($field_name)
```

## Documentation

```text
Utility function: delete a field stored in SQL storage directly from the database.

To protect user data, this function can only be used to delete fields once
all information it stored is gone. Delete all data from the
field_data_$field_name table before calling by either manually issuing
delete queries against it or using _update_7000_field_delete_instance().

This function can be used for databases whose schema is at field module
version 7000 or higher.

@param $field_name
  The field name to delete.

@ingroup update_api
```

## Code

```php
function _update_7000_field_delete_field($field_name) {
  $table_name = 'field_data_' . $field_name;
  if (db_select($table_name)->range(0, 1)->countQuery()->execute()->fetchField()) {
    $t = get_t();
    throw new Exception($t('This function can only be used to delete fields without data'));
  }
  // Delete all instances.
  db_delete('field_config_instance')
    ->condition('field_name', $field_name)
    ->execute();

  // Nuke field data and revision tables.
  db_drop_table($table_name);
  db_drop_table('field_revision_' . $field_name);

  // Delete the field.
  db_delete('field_config')
    ->condition('field_name', $field_name)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
