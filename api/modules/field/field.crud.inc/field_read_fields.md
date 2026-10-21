# field_read_fields()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 356–417 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L356-L417)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_read_fields($params = array(), $include_additional = array())
```

## Documentation

```text
Reads in fields that match an array of conditions.

@param array $params
  An array of conditions to match against. Keys are columns from the
  'field_config' table, values are conditions to match. Additionally,
  conditions on the 'entity_type' and 'bundle' columns from the
  'field_config_instance' table are supported (select fields having an
  instance on a given bundle).
@param array $include_additional
  The default behavior of this function is to not return fields that
  are inactive or have been deleted. Setting
  $include_additional['include_inactive'] or
  $include_additional['include_deleted'] to TRUE will override this
  behavior.
@return
  An array of fields matching $params. If
  $include_additional['include_deleted'] is TRUE, the array is keyed
  by field id, otherwise it is keyed by field name.
```

## Code

```php
function field_read_fields($params = array(), $include_additional = array()) {
  $query = db_select('field_config', 'fc', array('fetch' => PDO::FETCH_ASSOC));
  $query->fields('fc');

  // Turn the conditions into a query.
  foreach ($params as $key => $value) {
    // Allow filtering on the 'entity_type' and 'bundle' columns of the
    // field_config_instance table.
    if ($key == 'entity_type' || $key == 'bundle') {
      if (empty($fci_join)) {
        $fci_join = $query->join('field_config_instance', 'fci', 'fc.id = fci.field_id');
      }
      $key = 'fci.' . $key;
    }
    else {
      $key = 'fc.' . $key;
    }

    $query->condition($key, $value);
  }

  if (!isset($include_additional['include_inactive']) || !$include_additional['include_inactive']) {
    $query
      ->condition('fc.active', 1)
      ->condition('fc.storage_active', 1);
  }
  $include_deleted = (isset($include_additional['include_deleted']) && $include_additional['include_deleted']);
  if (!$include_deleted) {
    $query->condition('fc.deleted', 0);
  }

  $fields = array();
  $results = $query->execute();
  foreach ($results as $record) {
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

    module_invoke_all('field_read_field', $field);

    // Populate storage information.
    $schema = field_retrieve_schema($field);
    $field['columns'] = $schema['columns'];

    $field_name = $field['field_name'];
    if ($include_deleted) {
      $field_name = $field['id'];
    }
    $fields[$field_name] = $field;
  }
  return $fields;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
