# field_test_field_schema()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.install`](_file.md), lines 119–162 · [local source](../../../../../source/modules/field/tests/field_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install#L119-L162)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_schema()](../../field.api.php/hook_field_schema.md)

## Signature

```php
function field_test_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function field_test_field_schema($field) {
  if ($field['type'] == 'test_field') {
    return array(
      'columns' => array(
        'value' => array(
          'type' => 'int',
          'size' => 'medium',
          'not null' => FALSE,
        ),
      ),
      'indexes' => array(
        'value' => array('value'),
      ),
    );
  }
  else {
    $foreign_keys = array();
    // The 'foreign keys' key is not always used in tests.
    if (!empty($field['settings']['foreign_key_name'])) {
      $foreign_keys['foreign keys'] = array(
      // This is a dummy foreign key definition, references a table that
      // doesn't exist, but that's not a problem.
      $field['settings']['foreign_key_name'] => array(
        'table' => $field['settings']['foreign_key_name'],
        'columns' => array($field['settings']['foreign_key_name'] => 'id'),
        ),
      );
    }
    return array(
      'columns' => array(
        'shape' => array(
          'type' => 'varchar',
          'length' => 32,
          'not null' => FALSE,
        ),
        'color' => array(
          'type' => 'varchar',
          'length' => 32,
          'not null' => FALSE,
        ),
      ),
    ) + $foreign_keys;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.install](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
