# FieldInfoTestCase::testFieldPrepare()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1389–1415 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1389-L1415)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldPrepare()
```

## Documentation

```text
Test that cached field definitions are ready for current runtime context.
```

## Code

```php
  function testFieldPrepare() {
    $field_definition = array(
      'field_name' => 'field',
      'type' => 'test_field',
    );
    field_create_field($field_definition);

    // Simulate a stored field definition missing a field setting (e.g. a
    // third-party module adding a new field setting has been enabled, and
    // existing fields do not know the setting yet).
    $data = db_query('SELECT data FROM {field_config} WHERE field_name = :field_name', array(':field_name' => $field_definition['field_name']))->fetchField();
    $data = unserialize($data);
    $data['settings'] = array();
    db_update('field_config')
      ->fields(array('data' => serialize($data)))
      ->condition('field_name', $field_definition['field_name'])
      ->execute();

    field_cache_clear();

    // Read the field back.
    $field = field_info_field($field_definition['field_name']);

    // Check that all expected settings are in place.
    $field_type = field_info_field_types($field_definition['type']);
    $this->assertIdentical($field['settings'], $field_type['settings'], 'All expected default field settings are present.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
