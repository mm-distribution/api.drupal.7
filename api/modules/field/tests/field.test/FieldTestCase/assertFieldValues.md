# FieldTestCase::assertFieldValues()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 63–71 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L63-L71)
- **Class:** [FieldTestCase](../FieldTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function assertFieldValues($entity, $field_name, $langcode, $expected_values, $column = 'value')
```

## Documentation

```text
Assert that a field has the expected values in an entity.

This function only checks a single column in the field values.

@param $entity
  The entity to test.
@param $field_name
  The name of the field to test
@param $langcode
  The language code for the values.
@param $expected_values
  The array of expected values.
@param $column
  (Optional) the name of the column to check.
```

## Code

```php
  function assertFieldValues($entity, $field_name, $langcode, $expected_values, $column = 'value') {
    $e = clone $entity;
    field_attach_load('test_entity', array($e->ftid => $e));
    $values = isset($e->{$field_name}[$langcode]) ? $e->{$field_name}[$langcode] : array();
    $this->assertEqual(count($values), count($expected_values), 'Expected number of values were saved.');
    foreach ($expected_values as $key => $value) {
      $this->assertEqual($values[$key][$column], $value, format_string('Value @value was saved correctly.', array('@value' => $value)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
