# field_sql_storage_schema()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.install`](_file.md), lines 11–25 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install#L11-L25)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_schema()](../../../../system/system.api.php/hook_schema.md)

## Signature

```php
function field_sql_storage_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function field_sql_storage_schema() {
  $schema = array();

  // Dynamic (data) tables.
  if (db_table_exists('field_config')) {
    $fields = field_read_fields(array(), array('include_deleted' => TRUE, 'include_inactive' => TRUE));
    drupal_load('module', 'field_sql_storage');
    foreach ($fields as $field) {
      if ($field['storage']['type'] == 'field_sql_storage') {
        $schema += _field_sql_storage_schema($field);
      }
    }
  }
  return $schema;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install) · Licensed GPL-2.0-or-later (see LICENSE)._
