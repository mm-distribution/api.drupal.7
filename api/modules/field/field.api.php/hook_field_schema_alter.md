# hook_field_schema_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 291–305 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L291-L305)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_schema_alter(&$schema, $field)
```

## Documentation

```text
Allow modules to alter the schema for a field.

@param array $schema
  The schema definition as returned by hook_field_schema().
@param array $field
  The field definition.

@see field_retrieve_schema()
```

## Code

```php
function hook_field_schema_alter(&$schema, $field) {
  if ($field['type'] == 'image') {
    // Alter the length of a field.
    $schema['columns']['alt']['length'] = 2048;
    // Add an additional column of data.
    $schema['columns']['additional_column'] = array(
      'description' => "Additional column added to image field table.",
      'type' => 'varchar',
      'length' => 128,
      'not null' => FALSE,
    );
    // Add an additional index.
    $schema['indexes']['fid_additional_column'] = array('fid', 'additional_column');
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_schema_alter()".

- [field_test_schema_alter_field_schema_alter()](../tests/field_test_schema_alter.install/field_test_schema_alter_field_schema_alter.md) — `modules/field/tests/field_test_schema_alter.install`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
