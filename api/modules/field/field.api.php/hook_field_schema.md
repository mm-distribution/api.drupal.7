# hook_field_schema()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 241–279 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L241-L279)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_schema($field)
```

## Documentation

```text
Define the Field API schema for a field structure.

This is invoked when a field is created, in order to obtain the database
schema from the module that defines the field's type.

This hook must be defined in the module's .install file for it to be detected
during installation and upgrade.

@param $field
  A field structure.

@return
  An associative array with the following keys:
  - columns: An array of Schema API column specifications, keyed by column
    name. This specifies what comprises a value for a given field. For
    example, a value for a number field is simply 'value', while a value for
    a formatted text field is the combination of 'value' and 'format'. It is
    recommended to avoid having the column definitions depend on field
    settings when possible. No assumptions should be made on how storage
    engines internally use the original column name to structure their
    storage.
  - indexes: (optional) An array of Schema API indexes definitions. Only
    columns that appear in the 'columns' array are allowed. Those indexes
    will be used as default indexes. Callers of field_create_field() can
    specify additional indexes, or, at their own risk, modify the default
    indexes specified by the field-type module. Some storage engines might
    not support indexes.
  - foreign keys: (optional) An array of Schema API foreign keys
    definitions.
```

## Code

```php
function hook_field_schema($field) {
  if ($field['type'] == 'text_long') {
    $columns = array(
      'value' => array(
        'type' => 'text',
        'size' => 'big',
        'not null' => FALSE,
      ),
    );
  }
  else {
    $columns = array(
      'value' => array(
        'type' => 'varchar',
        'length' => $field['settings']['max_length'],
        'not null' => FALSE,
      ),
    );
  }
  $columns += array(
    'format' => array(
      'type' => 'varchar',
      'length' => 255,
      'not null' => FALSE,
    ),
  );
  return array(
    'columns' => $columns,
    'indexes' => array(
      'format' => array('format'),
    ),
    'foreign keys' => array(
      'format' => array(
        'table' => 'filter_format',
        'columns' => array('format' => 'format'),
      ),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_schema()".

- [field_test_field_schema()](../tests/field_test.install/field_test_field_schema.md) — `modules/field/tests/field_test.install`
- [file_field_schema()](../../file/file.install/file_field_schema.md) — `modules/file/file.install`
- [image_field_schema()](../../image/image.install/image_field_schema.md) — `modules/image/image.install`
- [list_field_schema()](../modules/list/list.install/list_field_schema.md) — `modules/field/modules/list/list.install`
- [number_field_schema()](../modules/number/number.install/number_field_schema.md) — `modules/field/modules/number/number.install`
- [taxonomy_field_schema()](../../taxonomy/taxonomy.install/taxonomy_field_schema.md) — `modules/taxonomy/taxonomy.install`
- [text_field_schema()](../modules/text/text.install/text_field_schema.md) — `modules/field/modules/text/text.install`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
