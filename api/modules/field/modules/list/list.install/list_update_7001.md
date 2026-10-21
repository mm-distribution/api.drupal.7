# list_update_7001()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.install`](_file.md), lines 51–89 · [local source](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install#L51-L89)
- **Module/theme:** list

## Signature

```php
function list_update_7001()
```

## Documentation

```text
Rename the list field types and change 'allowed_values' format.
```

## Code

```php
function list_update_7001() {
  $fields = _update_7000_field_read_fields(array('module' => 'list'));
  foreach ($fields as $field) {
    $update = array();

    // Translate the old string format into the new array format.
    $allowed_values = $field['settings']['allowed_values'];
    if (is_string($allowed_values)) {
      $position_keys = ($field['type'] == 'list');
      $allowed_values = _list_update_7001_extract_allowed_values($allowed_values, $position_keys);

      // Additionally, float keys need to be disambiguated ('.5' is '0.5').
      if ($field['type'] == 'list_number' && !empty($allowed_values)) {
        $keys = array_map('_list_update_7001_float_string_cast', array_keys($allowed_values));
        $allowed_values = array_combine($keys, array_values($allowed_values));
      }

      // Place the new setting in the existing serialized 'data' column.
      $data = db_query("SELECT data FROM {field_config} WHERE id = :id", array(':id' => $field['id']))->fetchField();
      $data = unserialize($data);
      $data['settings']['allowed_values'] = $allowed_values;
      $update['data'] = serialize($data);
    }

    // Rename field types.
    $types = array('list' => 'list_integer', 'list_number' => 'list_float');
    if (isset($types[$field['type']])) {
      $update['type'] = $types[$field['type']];
    }

    // Save the new data.
    if ($update) {
      $query = db_update('field_config')
        ->condition('id', $field['id'])
        ->fields($update)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · Licensed GPL-2.0-or-later (see LICENSE)._
