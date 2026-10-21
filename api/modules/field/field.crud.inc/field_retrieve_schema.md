# field_retrieve_schema()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 31–41 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L31-L41)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_retrieve_schema($field)
```

## Documentation

```text
Retrieves the schema for a field.

@param array $field
  The field array to get the schema definition against.
@return array
  The field schema definition array.
```

## Code

```php
function field_retrieve_schema($field) {
  // Make sure the installation API is available.
  include_once DRUPAL_ROOT . '/includes/install.inc';
  module_load_all_includes('install');
  $schema = (array) module_invoke($field['module'], 'field_schema', $field);
  $schema += array('columns' => array(), 'indexes' => array(), 'foreign keys' => array());
  // Give other modules a chance to alter this definition.
  // @see hook_field_schema_alter()
  drupal_alter('field_schema', $schema, $field);
  return $schema;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
