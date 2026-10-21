# FieldCrudTestCase::testReadField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2548–2558 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2548-L2558)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testReadField()
```

## Documentation

```text
Test reading back a field definition.
```

## Code

```php
  function testReadField() {
    $field_definition = array(
      'field_name' => 'field_1',
      'type' => 'test_field',
    );
    field_create_field($field_definition);

    // Read the field back.
    $field = field_read_field($field_definition['field_name']);
    $this->assertTrue($field_definition < $field, 'The field was properly read.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
