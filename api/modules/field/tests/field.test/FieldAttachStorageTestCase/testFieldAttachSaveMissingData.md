# FieldAttachStorageTestCase::testFieldAttachSaveMissingData()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 389–462 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L389-L462)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachSaveMissingData()
```

## Documentation

```text
Tests insert and update with missing or NULL fields.
```

## Code

```php
  function testFieldAttachSaveMissingData() {
    $entity_type = 'test_entity';
    $entity_init = field_test_create_stub_entity();
    $langcode = LANGUAGE_NONE;

    // Insert: Field is missing.
    $entity = clone($entity_init);
    field_attach_insert($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertTrue(empty($entity->{$this->field_name}), 'Insert: missing field results in no value saved');

    // Insert: Field is NULL.
    field_cache_clear();
    $entity = clone($entity_init);
    $entity->{$this->field_name} = NULL;
    field_attach_insert($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertTrue(empty($entity->{$this->field_name}), 'Insert: NULL field results in no value saved');

    // Add some real data.
    field_cache_clear();
    $entity = clone($entity_init);
    $values = $this->_generateTestFieldValues(1);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_insert($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertEqual($entity->{$this->field_name}[$langcode], $values, 'Field data saved');

    // Update: Field is missing. Data should survive.
    field_cache_clear();
    $entity = clone($entity_init);
    field_attach_update($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertEqual($entity->{$this->field_name}[$langcode], $values, 'Update: missing field leaves existing values in place');

    // Update: Field is NULL. Data should be wiped.
    field_cache_clear();
    $entity = clone($entity_init);
    $entity->{$this->field_name} = NULL;
    field_attach_update($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertTrue(empty($entity->{$this->field_name}), 'Update: NULL field removes existing values');

    // Re-add some data.
    field_cache_clear();
    $entity = clone($entity_init);
    $values = $this->_generateTestFieldValues(1);
    $entity->{$this->field_name}[$langcode] = $values;
    field_attach_update($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertEqual($entity->{$this->field_name}[$langcode], $values, 'Field data saved');

    // Update: Field is empty array. Data should be wiped.
    field_cache_clear();
    $entity = clone($entity_init);
    $entity->{$this->field_name} = array();
    field_attach_update($entity_type, $entity);

    $entity = clone($entity_init);
    field_attach_load($entity_type, array($entity->ftid => $entity));
    $this->assertTrue(empty($entity->{$this->field_name}), 'Update: empty array removes existing values');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
