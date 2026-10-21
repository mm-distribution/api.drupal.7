# FieldAttachStorageTestCase::testFieldAttachSaveLoad()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 160–215 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L160-L215)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachSaveLoad()
```

## Documentation

```text
Check field values insert, update and load.

Works independently of the underlying field storage backend. Inserts or
updates random field data and then loads and verifies the data.
```

## Code

```php
  function testFieldAttachSaveLoad() {
    // Configure the instance so that we test hook_field_load() (see
    // field_test_field_load() in field_test.module).
    $this->instance['settings']['test_hook_field_load'] = TRUE;
    field_update_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    $entity_type = 'test_entity';
    $values = array();

    // TODO : test empty values filtering and "compression" (store consecutive deltas).

    // Preparation: create three revisions and store them in $revision array.
    for ($revision_id = 0; $revision_id < 3; $revision_id++) {
      $revision[$revision_id] = field_test_create_stub_entity(0, $revision_id, $this->instance['bundle']);
      // Note: we try to insert one extra value.
      $values[$revision_id] = $this->_generateTestFieldValues($this->field['cardinality'] + 1);
      $current_revision = $revision_id;
      // If this is the first revision do an insert.
      if (!$revision_id) {
        $revision[$revision_id]->{$this->field_name}[$langcode] = $values[$revision_id];
        field_attach_insert($entity_type, $revision[$revision_id]);
      }
      else {
        // Otherwise do an update.
        $revision[$revision_id]->{$this->field_name}[$langcode] = $values[$revision_id];
        field_attach_update($entity_type, $revision[$revision_id]);
      }
    }

    // Confirm current revision loads the correct data.
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    field_attach_load($entity_type, array(0 => $entity));
    // Number of values per field loaded equals the field cardinality.
    $this->assertEqual(count($entity->{$this->field_name}[$langcode]), $this->field['cardinality'], 'Current revision: expected number of values');
    for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
      // The field value loaded matches the one inserted or updated.
      $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['value'] , $values[$current_revision][$delta]['value'], format_string('Current revision: expected value %delta was found.', array('%delta' => $delta)));
      // The value added in hook_field_load() is found.
      $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['additional_key'], 'additional_value', format_string('Current revision: extra information for value %delta was found', array('%delta' => $delta)));
    }

    // Confirm each revision loads the correct data.
    foreach (array_keys($revision) as $revision_id) {
      $entity = field_test_create_stub_entity(0, $revision_id, $this->instance['bundle']);
      field_attach_load_revision($entity_type, array(0 => $entity));
      // Number of values per field loaded equals the field cardinality.
      $this->assertEqual(count($entity->{$this->field_name}[$langcode]), $this->field['cardinality'], format_string('Revision %revision_id: expected number of values.', array('%revision_id' => $revision_id)));
      for ($delta = 0; $delta < $this->field['cardinality']; $delta++) {
        // The field value loaded matches the one inserted or updated.
        $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['value'], $values[$revision_id][$delta]['value'], format_string('Revision %revision_id: expected value %delta was found.', array('%revision_id' => $revision_id, '%delta' => $delta)));
        // The value added in hook_field_load() is found.
        $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['additional_key'], 'additional_value', format_string('Revision %revision_id: extra information for value %delta was found', array('%revision_id' => $revision_id, '%delta' => $delta)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
