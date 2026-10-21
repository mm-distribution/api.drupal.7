# _update_7000_field_read_fields()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 329–354 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L329-L354)
- **Module/theme:** field
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_read_fields(array $conditions = array(), $key = 'id')
```

## Documentation

```text
Utility function: fetch all the field definitions from the database.

Warning: unlike the field_read_fields() API function, this function returns
all fields by default, including deleted and inactive fields, unless
specified otherwise in the $conditions parameter.

@param $conditions
  An array of conditions to limit the select query to.
@param $key
  The name of the field property the return array is indexed by. Using
  anything else than 'id' might cause incomplete results if the $conditions
  do not filter out deleted fields.

@return
  An array of fields matching $conditions, keyed by the property specified
  by the $key parameter.

@ingroup update_api
```

## Code

```php
function _update_7000_field_read_fields(array $conditions = array(), $key = 'id') {
  $fields = array();
  $query = db_select('field_config', 'fc', array('fetch' => PDO::FETCH_ASSOC))
    ->fields('fc');
  foreach ($conditions as $column => $value) {
    $query->condition($column, $value);
  }
  foreach ($query->execute() as $record) {
    $field = unserialize($record['data']);
    $field['id'] = $record['id'];
    $field['field_name'] = $record['field_name'];
    $field['type'] = $record['type'];
    $field['module'] = $record['module'];
    $field['active'] = $record['active'];
    $field['storage']['type'] = $record['storage_type'];
    $field['storage']['module'] = $record['storage_module'];
    $field['storage']['active'] = $record['storage_active'];
    $field['locked'] = $record['locked'];
    $field['cardinality'] = $record['cardinality'];
    $field['translatable'] = $record['translatable'];
    $field['deleted'] = $record['deleted'];

    $fields[$field[$key]] = $field;
  }
  return $fields;
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
