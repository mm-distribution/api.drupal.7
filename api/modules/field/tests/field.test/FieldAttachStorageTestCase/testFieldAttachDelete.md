# FieldAttachStorageTestCase::testFieldAttachDelete()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 559–609 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L559-L609)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachDelete()
```

## Documentation

```text
Test field_attach_delete().
```

## Code

```php
  function testFieldAttachDelete() {
    $entity_type = 'test_entity';
    $langcode = LANGUAGE_NONE;
    $rev[0] = field_test_create_stub_entity(0, 0, $this->instance['bundle']);

    // Create revision 0
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $rev[0]->{$this->field_name}[$langcode] = $values;
    field_attach_insert($entity_type, $rev[0]);

    // Create revision 1
    $rev[1] = field_test_create_stub_entity(0, 1, $this->instance['bundle']);
    $rev[1]->{$this->field_name}[$langcode] = $values;
    field_attach_update($entity_type, $rev[1]);

    // Create revision 2
    $rev[2] = field_test_create_stub_entity(0, 2, $this->instance['bundle']);
    $rev[2]->{$this->field_name}[$langcode] = $values;
    field_attach_update($entity_type, $rev[2]);

    // Confirm each revision loads
    foreach (array_keys($rev) as $vid) {
      $read = field_test_create_stub_entity(0, $vid, $this->instance['bundle']);
      field_attach_load_revision($entity_type, array(0 => $read));
      $this->assertEqual(count($read->{$this->field_name}[$langcode]), $this->field['cardinality'], "The test entity revision $vid has {$this->field['cardinality']} values.");
    }

    // Delete revision 1, confirm the other two still load.
    field_attach_delete_revision($entity_type, $rev[1]);
    foreach (array(0, 2) as $vid) {
      $read = field_test_create_stub_entity(0, $vid, $this->instance['bundle']);
      field_attach_load_revision($entity_type, array(0 => $read));
      $this->assertEqual(count($read->{$this->field_name}[$langcode]), $this->field['cardinality'], "The test entity revision $vid has {$this->field['cardinality']} values.");
    }

    // Confirm the current revision still loads
    $read = field_test_create_stub_entity(0, 2, $this->instance['bundle']);
    field_attach_load($entity_type, array(0 => $read));
    $this->assertEqual(count($read->{$this->field_name}[$langcode]), $this->field['cardinality'], "The test entity current revision has {$this->field['cardinality']} values.");

    // Delete all field data, confirm nothing loads
    field_attach_delete($entity_type, $rev[2]);
    foreach (array(0, 1, 2) as $vid) {
      $read = field_test_create_stub_entity(0, $vid, $this->instance['bundle']);
      field_attach_load_revision($entity_type, array(0 => $read));
      $this->assertIdentical($read->{$this->field_name}, array(), "The test entity revision $vid is deleted.");
    }
    $read = field_test_create_stub_entity(0, 2, $this->instance['bundle']);
    field_attach_load($entity_type, array(0 => $read));
    $this->assertIdentical($read->{$this->field_name}, array(), 'The test entity current revision is deleted.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
