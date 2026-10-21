# FieldBulkDeleteTestCase::testPurgeField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3759–3830 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3759-L3830)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testPurgeField()
```

## Documentation

```text
Verify that fields are preserved and purged correctly as multiple
instances are deleted and purged.
```

## Code

```php
  function testPurgeField() {
    // Start recording hook invocations.
    field_test_memorize();

    $field = reset($this->fields);

    // Delete the first instance.
    $bundle = reset($this->bundles);
    $instance = field_info_instance($this->entity_type, $field['field_name'], $bundle);
    field_delete_instance($instance);

    // Assert that hook_field_delete() was not called yet.
    $mem = field_test_memorize();
    $this->assertEqual(count($mem), 0, 'No field hooks were called.');

    // Purge the data.
    field_purge_batch(10);

    // Check hooks invocations.
    // - hook_field_load() (multiple hook) should have been called once, for all
    // entities in the bundle.
    // - hook_field_delete() should have been called once for each entity in the
    // bundle.
    $actual_hooks = field_test_memorize();
    $hooks = array();
    $stubs = $this->_generateStubEntities($this->entity_type, $this->entities_by_bundles[$bundle], $field['field_name']);
    $hooks['field_test_field_load'][] = $stubs;
    foreach ($stubs as $stub) {
      $hooks['field_test_field_delete'][] = $stub;
    }
    $this->checkHooksInvocations($hooks, $actual_hooks);

    // Purge again to purge the instance.
    field_purge_batch(0);

    // The field still exists, not deleted.
    $fields = field_read_fields(array('id' => $field['id']), array('include_deleted' => 1));
    $this->assertTrue(isset($fields[$field['id']]) && !$fields[$field['id']]['deleted'], 'The field exists and is not deleted');

    // Delete the second instance.
    $bundle = next($this->bundles);
    $instance = field_info_instance($this->entity_type, $field['field_name'], $bundle);
    field_delete_instance($instance);

    // Assert that hook_field_delete() was not called yet.
    $mem = field_test_memorize();
    $this->assertEqual(count($mem), 0, 'No field hooks were called.');

    // Purge the data.
    field_purge_batch(10);

    // Check hooks invocations (same as above, for the 2nd bundle).
    $actual_hooks = field_test_memorize();
    $hooks = array();
    $stubs = $this->_generateStubEntities($this->entity_type, $this->entities_by_bundles[$bundle], $field['field_name']);
    $hooks['field_test_field_load'][] = $stubs;
    foreach ($stubs as $stub) {
      $hooks['field_test_field_delete'][] = $stub;
    }
    $this->checkHooksInvocations($hooks, $actual_hooks);

    // The field still exists, deleted.
    $fields = field_read_fields(array('id' => $field['id']), array('include_deleted' => 1));
    $this->assertTrue(isset($fields[$field['id']]) && $fields[$field['id']]['deleted'], 'The field exists and is deleted');

    // Purge again to purge the instance and the field.
    field_purge_batch(0);

    // The field is gone.
    $fields = field_read_fields(array('id' => $field['id']), array('include_deleted' => 1, 'include_inactive' => 1));
    $this->assertEqual(count($fields), 0, 'The field is purged.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
