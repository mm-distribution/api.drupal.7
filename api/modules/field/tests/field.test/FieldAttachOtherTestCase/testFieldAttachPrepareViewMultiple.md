# FieldAttachOtherTestCase::testFieldAttachPrepareViewMultiple()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 892–936 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L892-L936)
- **Class:** [FieldAttachOtherTestCase](../FieldAttachOtherTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachPrepareViewMultiple()
```

## Documentation

```text
Tests the 'multiple entity' behavior of field_attach_prepare_view().
```

## Code

```php
  function testFieldAttachPrepareViewMultiple() {
    $entity_type = 'test_entity';
    $langcode = LANGUAGE_NONE;

    // Set the instance to be hidden.
    $this->instance['display']['full']['type'] = 'hidden';
    field_update_instance($this->instance);

    // Set up a second instance on another bundle, with a formatter that uses
    // hook_field_formatter_prepare_view().
    field_test_create_bundle('test_bundle_2');
    $formatter_setting = $this->randomName();
    $this->instance2 = $this->instance;
    $this->instance2['bundle'] = 'test_bundle_2';
    $this->instance2['display']['full'] = array(
      'type' => 'field_test_with_prepare_view',
      'settings' => array(
        'test_formatter_setting_additional' => $formatter_setting,
      )
    );
    field_create_instance($this->instance2);

    // Create one entity in each bundle.
    $entity1_init = field_test_create_stub_entity(1, 1, 'test_bundle');
    $values1 = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity1_init->{$this->field_name}[$langcode] = $values1;

    $entity2_init = field_test_create_stub_entity(2, 2, 'test_bundle_2');
    $values2 = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity2_init->{$this->field_name}[$langcode] = $values2;

    // Run prepare_view, and check that the entities come out as expected.
    $entity1 = clone($entity1_init);
    $entity2 = clone($entity2_init);
    field_attach_prepare_view($entity_type, array($entity1->ftid => $entity1, $entity2->ftid => $entity2), 'full');
    $this->assertFalse(isset($entity1->{$this->field_name}[$langcode][0]['additional_formatter_value']), 'Entity 1 did not run through the prepare_view hook.');
    $this->assertTrue(isset($entity2->{$this->field_name}[$langcode][0]['additional_formatter_value']), 'Entity 2 ran through the prepare_view hook.');

    // Same thing, reversed order.
    $entity1 = clone($entity1_init);
    $entity2 = clone($entity2_init);
    field_attach_prepare_view($entity_type, array($entity2->ftid => $entity2, $entity1->ftid => $entity1), 'full');
    $this->assertFalse(isset($entity1->{$this->field_name}[$langcode][0]['additional_formatter_value']), 'Entity 1 did not run through the prepare_view hook.');
    $this->assertTrue(isset($entity2->{$this->field_name}[$langcode][0]['additional_formatter_value']), 'Entity 2 ran through the prepare_view hook.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
