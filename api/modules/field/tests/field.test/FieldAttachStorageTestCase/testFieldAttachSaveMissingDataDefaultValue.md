# FieldAttachStorageTestCase::testFieldAttachSaveMissingDataDefaultValue()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 467–494 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L467-L494)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachSaveMissingDataDefaultValue()
```

## Documentation

```text
Test insert with missing or NULL fields, with default value.
```

## Code

```php
  function testFieldAttachSaveMissingDataDefaultValue() {
    // Add a default value function.
    $this->instance['default_value_function'] = 'field_test_default_value';
    field_update_instance($this->instance);

    $entity_type = 'test_entity';
    $entity_init = field_test_create_stub_entity();
    $langcode = LANGUAGE_NONE;

    // Insert: Field is NULL.
    $entity = clone($entity_init);
    $entity->{$this->field_name}[$langcode] = NULL;
    field_attach_insert($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertTrue(empty($entity->{$this->field_name}[$langcode]), 'Insert: NULL field results in no value saved');

    // Insert: Field is missing.
    field_cache_clear();
    $entity = clone($entity_init);
    field_attach_insert($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $values = field_test_default_value($entity_type, $entity, $this->field, $this->instance);
    $this->assertEqual($entity->{$this->field_name}[$langcode], $values, 'Insert: missing field results in default value saved');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
