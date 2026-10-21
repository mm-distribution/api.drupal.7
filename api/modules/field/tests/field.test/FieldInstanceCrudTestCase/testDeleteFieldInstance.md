# FieldInstanceCrudTestCase::testDeleteFieldInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3109–3143 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3109-L3143)
- **Class:** [FieldInstanceCrudTestCase](../FieldInstanceCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testDeleteFieldInstance()
```

## Documentation

```text
Test the deletion of a field instance.
```

## Code

```php
  function testDeleteFieldInstance() {
    // TODO: Test deletion of the data stored in the field also.
    // Need to check that data for a 'deleted' field / instance doesn't get loaded
    // Need to check data marked deleted is cleaned on cron (not implemented yet...)

    // Create two instances for the same field so we can test that only one
    // is deleted.
    field_create_instance($this->instance_definition);
    $this->another_instance_definition = $this->instance_definition;
    $this->another_instance_definition['bundle'] .= '_another_bundle';
    $instance = field_create_instance($this->another_instance_definition);

    // Test that the first instance is not deleted, and then delete it.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($instance) && empty($instance['deleted']), 'A new field instance is not marked for deletion.');
    field_delete_instance($instance);

    // Make sure the instance is marked as deleted when the instance is
    // specifically loaded.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($instance['deleted']), 'A deleted field instance is marked for deletion.');

    // Try to load the instance normally and make sure it does not show up.
    $instance = field_read_instance('test_entity', $this->instance_definition['field_name'], $this->instance_definition['bundle']);
    $this->assertTrue(empty($instance), 'A deleted field instance is not loaded by default.');

    // Make sure the other field instance is not deleted.
    $another_instance = field_read_instance('test_entity', $this->another_instance_definition['field_name'], $this->another_instance_definition['bundle']);
    $this->assertTrue(!empty($another_instance) && empty($another_instance['deleted']), 'A non-deleted field instance is not marked for deletion.');

    // Make sure the field is deleted when its last instance is deleted.
    field_delete_instance($another_instance);
    $field = field_read_field($another_instance['field_name'], array('include_deleted' => TRUE));
    $this->assertTrue(!empty($field['deleted']), 'A deleted field is marked for deletion after all its instances have been marked for deletion.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
