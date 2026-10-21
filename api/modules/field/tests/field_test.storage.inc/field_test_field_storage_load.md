# field_test_field_storage_load()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 83–114 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L83-L114)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_load()](../../field.api.php/hook_field_storage_load.md)

## Signature

```php
function field_test_field_storage_load($entity_type, $entities, $age, $fields, $options)
```

## Documentation

```text
Implements hook_field_storage_load().
```

## Code

```php
function field_test_field_storage_load($entity_type, $entities, $age, $fields, $options) {
  $data = _field_test_storage_data();

  $load_current = $age == FIELD_LOAD_CURRENT;

  foreach ($fields as $field_id => $ids) {
    $field = field_info_field_by_id($field_id);
    $field_name = $field['field_name'];
    $field_data = $data[$field['id']];
    $sub_table = $load_current ? 'current' : 'revisions';
    $delta_count = array();
    foreach ($field_data[$sub_table] as $row) {
      if ($row->type == $entity_type && (!$row->deleted || $options['deleted'])) {
        if (($load_current && in_array($row->entity_id, $ids)) || (!$load_current && in_array($row->revision_id, $ids))) {
          if (in_array($row->language, field_available_languages($entity_type, $field))) {
            if (!isset($delta_count[$row->entity_id][$row->language])) {
              $delta_count[$row->entity_id][$row->language] = 0;
            }
            if ($field['cardinality'] == FIELD_CARDINALITY_UNLIMITED || $delta_count[$row->entity_id][$row->language] < $field['cardinality']) {
              $item = array();
              foreach ($field['columns'] as $column => $attributes) {
                $item[$column] = $row->{$column};
              }
              $entities[$row->entity_id]->{$field_name}[$row->language][] = $item;
              $delta_count[$row->entity_id][$row->language]++;
            }
          }
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
