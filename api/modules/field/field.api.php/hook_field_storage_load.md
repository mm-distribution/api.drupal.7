# hook_field_storage_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1813–1859 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1813-L1859)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_load($entity_type, $entities, $age, $fields, $options)
```

## Documentation

```text
Load field data for a set of entities.

This hook is invoked from field_attach_load() to ask the field storage
module to load field data.

Modules implementing this hook should load field values and add them to
objects in $entities. Fields with no values should be added as empty
arrays.

@param $entity_type
  The type of entity, such as 'node' or 'user'.
@param $entities
  The array of entity objects to add fields to, keyed by entity ID.
@param $age
  FIELD_LOAD_CURRENT to load the most recent revision for all fields, or
  FIELD_LOAD_REVISION to load the version indicated by each entity.
@param $fields
  An array listing the fields to be loaded. The keys of the array are field
  IDs, and the values of the array are the entity IDs (or revision IDs,
  depending on the $age parameter) to add each field to.
@param $options
  An associative array of additional options, with the following keys:
  - deleted: If TRUE, deleted fields should be loaded as well as
    non-deleted fields. If unset or FALSE, only non-deleted fields should be
    loaded.
```

## Code

```php
function hook_field_storage_load($entity_type, $entities, $age, $fields, $options) {
  $load_current = $age == FIELD_LOAD_CURRENT;

  foreach ($fields as $field_id => $ids) {
    // By the time this hook runs, the relevant field definitions have been
    // populated and cached in FieldInfo, so calling field_info_field_by_id()
    // on each field individually is more efficient than loading all fields in
    // memory upfront with field_info_field_by_ids().
    $field = field_info_field_by_id($field_id);
    $field_name = $field['field_name'];
    $table = $load_current ? _field_sql_storage_tablename($field) : _field_sql_storage_revision_tablename($field);

    $query = db_select($table, 't')
      ->fields('t')
      ->condition('entity_type', $entity_type)
      ->condition($load_current ? 'entity_id' : 'revision_id', $ids, 'IN')
      ->condition('language', field_available_languages($entity_type, $field), 'IN')
      ->orderBy('delta');

    if (empty($options['deleted'])) {
      $query->condition('deleted', 0);
    }

    $results = $query->execute();

    $delta_count = array();
    foreach ($results as $row) {
      if (!isset($delta_count[$row->entity_id][$row->language])) {
        $delta_count[$row->entity_id][$row->language] = 0;
      }

      if ($field['cardinality'] == FIELD_CARDINALITY_UNLIMITED || $delta_count[$row->entity_id][$row->language] < $field['cardinality']) {
        $item = array();
        // For each column declared by the field, populate the item
        // from the prefixed database column.
        foreach ($field['columns'] as $column => $attributes) {
          $column_name = _field_sql_storage_columnname($field_name, $column);
          $item[$column] = $row->$column_name;
        }

        // Add the item to the field values for the entity.
        $entities[$row->entity_id]->{$field_name}[$row->language][] = $item;
        $delta_count[$row->entity_id][$row->language]++;
      }
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_load()".

- [field_sql_storage_field_storage_load()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_load.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_load()](../tests/field_test.storage.inc/field_test_field_storage_load.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
