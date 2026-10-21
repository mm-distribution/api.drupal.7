# field_test_field_storage_write()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 119–184 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L119-L184)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_write()](../../field.api.php/hook_field_storage_write.md)

## Signature

```php
function field_test_field_storage_write($entity_type, $entity, $op, $fields)
```

## Documentation

```text
Implements hook_field_storage_write().
```

## Code

```php
function field_test_field_storage_write($entity_type, $entity, $op, $fields) {
  $data = _field_test_storage_data();

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  foreach ($fields as $field_id) {
    $field = field_info_field_by_id($field_id);
    $field_name = $field['field_name'];
    $field_data = &$data[$field_id];

    $all_languages = field_available_languages($entity_type, $field);
    $field_languages = array_intersect($all_languages, array_keys((array) $entity->$field_name));

    // Delete and insert, rather than update, in case a value was added.
    if ($op == FIELD_STORAGE_UPDATE) {
      // Delete languages present in the incoming $entity->$field_name.
      // Delete all languages if $entity->$field_name is empty.
      $languages = !empty($entity->$field_name) ? $field_languages : $all_languages;
      if ($languages) {
        foreach ($field_data['current'] as $key => $row) {
          if ($row->type == $entity_type && $row->entity_id == $id && in_array($row->language, $languages)) {
            unset($field_data['current'][$key]);
          }
        }
        if (isset($vid)) {
          foreach ($field_data['revisions'] as $key => $row) {
            if ($row->type == $entity_type && $row->revision_id == $vid) {
              unset($field_data['revisions'][$key]);
            }
          }
        }
      }
    }

    foreach ($field_languages as $langcode) {
      $items = (array) $entity->{$field_name}[$langcode];
      $delta_count = 0;
      foreach ($items as $delta => $item) {
        $row = (object) array(
          'field_id' => $field_id,
          'type' => $entity_type,
          'entity_id' => $id,
          'revision_id' => $vid,
          'bundle' => $bundle,
          'delta' => $delta,
          'deleted' => FALSE,
          'language' => $langcode,
        );
        foreach ($field['columns'] as $column => $attributes) {
          $row->{$column} = isset($item[$column]) ? $item[$column] : NULL;
        }

        $field_data['current'][] = $row;
        if (isset($vid)) {
          $field_data['revisions'][] = $row;
        }

        if ($field['cardinality'] != FIELD_CARDINALITY_UNLIMITED && ++$delta_count == $field['cardinality']) {
          break;
        }
      }
    }
  }

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
