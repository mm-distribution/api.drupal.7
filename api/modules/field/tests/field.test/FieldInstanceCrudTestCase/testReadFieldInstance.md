# FieldInstanceCrudTestCase::testReadFieldInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3040–3046 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3040-L3046)
- **Class:** [FieldInstanceCrudTestCase](../FieldInstanceCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testReadFieldInstance()
```

## Documentation

```text
Test reading back an instance definition.
```

## Code

```php
  function testReadFieldInstance() {
    field_create_instance($this->instance_definition);

    // Read the instance back.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertTrue($this->instance_definition < $instance, 'The field was properly read.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
