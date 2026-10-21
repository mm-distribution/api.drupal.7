# FieldAttachStorageTestCase::testFieldAttachCreateRenameBundle()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 614–650 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L614-L650)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldAttachCreateRenameBundle()
```

## Documentation

```text
Test field_attach_create_bundle() and field_attach_rename_bundle().
```

## Code

```php
  function testFieldAttachCreateRenameBundle() {
    // Create a new bundle. This has to be initiated by the module so that its
    // hook_entity_info() is consistent.
    $new_bundle = 'test_bundle_' . drupal_strtolower($this->randomName());
    field_test_create_bundle($new_bundle);

    // Add an instance to that bundle.
    $this->instance['bundle'] = $new_bundle;
    field_create_instance($this->instance);

    // Save an entity with data in the field.
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;
    $values = $this->_generateTestFieldValues($this->field['cardinality']);
    $entity->{$this->field_name}[$langcode] = $values;
    $entity_type = 'test_entity';
    field_attach_insert($entity_type, $entity);

    // Verify the field data is present on load.
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    field_attach_load($entity_type, array(0 => $entity));
    $this->assertEqual(count($entity->{$this->field_name}[$langcode]), $this->field['cardinality'], "Data is retrieved for the new bundle");

    // Rename the bundle. This has to be initiated by the module so that its
    // hook_entity_info() is consistent.
    $new_bundle = 'test_bundle_' . drupal_strtolower($this->randomName());
    field_test_rename_bundle($this->instance['bundle'], $new_bundle);

    // Check that the instance definition has been updated.
    $this->instance = field_info_instance($entity_type, $this->field_name, $new_bundle);
    $this->assertIdentical($this->instance['bundle'], $new_bundle, "Bundle name has been updated in the instance.");

    // Verify the field data is present on load.
    $entity = field_test_create_stub_entity(0, 0, $new_bundle);
    field_attach_load($entity_type, array(0 => $entity));
    $this->assertEqual(count($entity->{$this->field_name}[$langcode]), $this->field['cardinality'], "Bundle name has been updated in the field storage");
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
