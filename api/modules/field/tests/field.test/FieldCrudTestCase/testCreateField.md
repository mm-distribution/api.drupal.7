# FieldCrudTestCase::testCreateField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2403–2517 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2403-L2517)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testCreateField()
```

## Documentation

```text
Test the creation of a field.
```

## Code

```php
  function testCreateField() {
    $field_definition = array(
      'field_name' => 'field_2',
      'type' => 'test_field',
    );
    field_test_memorize();
    $field_definition = field_create_field($field_definition);
    $mem = field_test_memorize();
    $this->assertIdentical($mem['field_test_field_create_field'][0][0], $field_definition, 'hook_field_create_field() called with correct arguments.');

    // Read the raw record from the {field_config_instance} table.
    $result = db_query('SELECT * FROM {field_config} WHERE field_name = :field_name', array(':field_name' => $field_definition['field_name']));
    $record = $result->fetchAssoc();
    $record['data'] = unserialize($record['data']);

    // Ensure that basic properties are preserved.
    $this->assertEqual($record['field_name'], $field_definition['field_name'], 'The field name is properly saved.');
    $this->assertEqual($record['type'], $field_definition['type'], 'The field type is properly saved.');

    // Ensure that cardinality defaults to 1.
    $this->assertEqual($record['cardinality'], 1, 'Cardinality defaults to 1.');

    // Ensure that default settings are present.
    $field_type = field_info_field_types($field_definition['type']);
    $this->assertIdentical($record['data']['settings'], $field_type['settings'], 'Default field settings have been written.');

    // Ensure that default storage was set.
    $this->assertEqual($record['storage_type'], variable_get('field_storage_default'), 'The field type is properly saved.');

    // Guarantee that the name is unique.
    try {
      field_create_field($field_definition);
      $this->fail(t('Cannot create two fields with the same name.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create two fields with the same name.'));
    }

    // Check that field type is required.
    try {
      $field_definition = array(
        'field_name' => 'field_1',
      );
      field_create_field($field_definition);
      $this->fail(t('Cannot create a field with no type.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create a field with no type.'));
    }

    // Check that field name is required.
    try {
      $field_definition = array(
        'type' => 'test_field'
      );
      field_create_field($field_definition);
      $this->fail(t('Cannot create an unnamed field.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create an unnamed field.'));
    }

    // Check that field name must start with a letter or _.
    try {
      $field_definition = array(
        'field_name' => '2field_2',
        'type' => 'test_field',
      );
      field_create_field($field_definition);
      $this->fail(t('Cannot create a field with a name starting with a digit.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create a field with a name starting with a digit.'));
    }

    // Check that field name must only contain lowercase alphanumeric or _.
    try {
      $field_definition = array(
        'field_name' => 'field#_3',
        'type' => 'test_field',
      );
      field_create_field($field_definition);
      $this->fail(t('Cannot create a field with a name containing an illegal character.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create a field with a name containing an illegal character.'));
    }

    // Check that field name cannot be longer than 32 characters long.
    try {
      $field_definition = array(
        'field_name' => '_12345678901234567890123456789012',
        'type' => 'test_field',
      );
      field_create_field($field_definition);
      $this->fail(t('Cannot create a field with a name longer than 32 characters.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create a field with a name longer than 32 characters.'));
    }

    // Check that field name can not be an entity key.
    // "ftvid" is known as an entity key from the "test_entity" type.
    try {
      $field_definition = array(
        'type' => 'test_field',
        'field_name' => 'ftvid',
      );
      $field = field_create_field($field_definition);
      $this->fail(t('Cannot create a field bearing the name of an entity key.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot create a field bearing the name of an entity key.'));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
