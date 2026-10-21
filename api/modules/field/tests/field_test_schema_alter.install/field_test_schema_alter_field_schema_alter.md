# field_test_schema_alter_field_schema_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test_schema_alter.install`](_file.md), lines 11–23 · [local source](../../../../../source/modules/field/tests/field_test_schema_alter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test_schema_alter.install#L11-L23)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_schema_alter()](../../field.api.php/hook_field_schema_alter.md)

## Signature

```php
function field_test_schema_alter_field_schema_alter(&$schema, $field)
```

## Documentation

```text
Implements hook_field_schema_alter().
```

## Code

```php
function field_test_schema_alter_field_schema_alter(&$schema, $field) {
  if ($field['type'] == 'test_field') {
    // Alter the field type.
    $schema['columns']['value']['type'] = 'float';
    // Add an additional column of data.
    $schema['columns']['additional_column'] = array(
      'description' => "Additional column added to image field table.",
      'type' => 'varchar',
      'length' => 128,
      'not null' => FALSE,
    );
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test_schema_alter.install](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test_schema_alter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
