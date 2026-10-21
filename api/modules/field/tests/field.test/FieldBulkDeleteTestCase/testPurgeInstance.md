# FieldBulkDeleteTestCase::testPurgeInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3693–3753 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3693-L3753)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testPurgeInstance()
```

## Documentation

```text
Verify that field data items and instances are purged when an
instance is deleted.
```

## Code

```php
  function testPurgeInstance() {
    // Start recording hook invocations.
    field_test_memorize();

    $bundle = reset($this->bundles);
    $field = reset($this->fields);

    // Delete the instance.
    $instance = field_info_instance($this->entity_type, $field['field_name'], $bundle);
    field_delete_instance($instance);

    // No field hooks were called.
    $mem = field_test_memorize();
    $this->assertEqual(count($mem), 0, 'No field hooks were called');

    $batch_size = 2;
    for ($count = 8; $count >= 0; $count -= $batch_size) {
      // Purge two entities.
      field_purge_batch($batch_size);

      // There are $count deleted entities left.
      $query = new EntityFieldQuery();
      $found = $query
        ->fieldCondition($field)
        ->entityCondition('bundle', $bundle)
        ->deleted(TRUE)
        ->execute();
      $this->assertEqual($count ? count($found['test_entity']) : count($found), $count, 'Correct number of entities found after purging 2');
    }

    // Check hooks invocations.
    // - hook_field_load() (multiple hook) should have been called on all
    // entities by pairs of two.
    // - hook_field_delete() should have been called once for each entity in the
    // bundle.
    $actual_hooks = field_test_memorize();
    $hooks = array();
    $stubs = $this->_generateStubEntities($this->entity_type, $this->entities_by_bundles[$bundle], $field['field_name']);
    foreach (array_chunk($stubs, $batch_size, TRUE) as $chunk) {
      $hooks['field_test_field_load'][] = $chunk;
    }
    foreach ($stubs as $stub) {
      $hooks['field_test_field_delete'][] = $stub;
    }
    $this->checkHooksInvocations($hooks, $actual_hooks);

    // The instance still exists, deleted.
    $instances = field_read_instances(array('field_id' => $field['id'], 'deleted' => 1), array('include_deleted' => 1, 'include_inactive' => 1));
    $this->assertEqual(count($instances), 1, 'There is one deleted instance');

    // Purge the instance.
    field_purge_batch($batch_size);

    // The instance is gone.
    $instances = field_read_instances(array('field_id' => $field['id'], 'deleted' => 1), array('include_deleted' => 1, 'include_inactive' => 1));
    $this->assertEqual(count($instances), 0, 'The instance is gone');

    // The field still exists, not deleted, because it has a second instance.
    $fields = field_read_fields(array('id' => $field['id']), array('include_deleted' => 1, 'include_inactive' => 1));
    $this->assertTrue(isset($fields[$field['id']]), 'The field exists and is not deleted');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
