# field_update_7001()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 411–437 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L411-L437)
- **Module/theme:** field
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function field_update_7001()
```

## Documentation

```text
Fix fields definitions created during the d6 to d7 upgrade path.
```

## Code

```php
function field_update_7001() {
  $fields = _update_7000_field_read_fields();
  foreach ($fields as $field) {
    // _update_7000_field_create_field() was broken in d7 RC2, and the fields
    // created during a d6 to d7 upgrade do not correcly store the 'index'
    // entry. See http://drupal.org/node/996160.

    module_load_install($field['module']);
    $schema = (array) module_invoke($field['module'], 'field_schema', $field);
    $schema += array('indexes' => array());
    // 'indexes' can be both hardcoded in the field type, and specified in the
    // incoming $field definition.
    $field['indexes'] += $schema['indexes'];

    // Place the updated entries in the existing serialized 'data' column.
    $data = db_query("SELECT data FROM {field_config} WHERE id = :id", array(':id' => $field['id']))->fetchField();
    $data = unserialize($data);
    $data['columns'] = $field['columns'];
    $data['indexes'] = $field['indexes'];

    // Save the new data.
    $query = db_update('field_config')
      ->condition('id', $field['id'])
      ->fields(array('data' => serialize($data)))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
