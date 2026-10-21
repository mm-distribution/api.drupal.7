# FieldBulkDeleteTestCase::testDeleteFieldInstance()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 3645–3687 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3645-L3687)
- **Class:** [FieldBulkDeleteTestCase](../FieldBulkDeleteTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testDeleteFieldInstance()
```

## Documentation

```text
Verify that deleting an instance leaves the field data items in
the database and that the appropriate Field API functions can
operate on the deleted data and instance.

This tests how EntityFieldQuery interacts with
field_delete_instance() and could be moved to FieldCrudTestCase,
but depends on this class's setUp().
```

## Code

```php
  function testDeleteFieldInstance() {
    $bundle = reset($this->bundles);
    $field = reset($this->fields);

    // There are 10 entities of this bundle.
    $query = new EntityFieldQuery();
    $found = $query
      ->fieldCondition($field)
      ->entityCondition('bundle', $bundle)
      ->execute();
    $this->assertEqual(count($found['test_entity']), 10, 'Correct number of entities found before deleting');

    // Delete the instance.
    $instance = field_info_instance($this->entity_type, $field['field_name'], $bundle);
    field_delete_instance($instance);

    // The instance still exists, deleted.
    $instances = field_read_instances(array('field_id' => $field['id'], 'deleted' => 1), array('include_deleted' => 1, 'include_inactive' => 1));
    $this->assertEqual(count($instances), 1, 'There is one deleted instance');
    $this->assertEqual($instances[0]['bundle'], $bundle, 'The deleted instance is for the correct bundle');

    // There are 0 entities of this bundle with non-deleted data.
    $query = new EntityFieldQuery();
    $found = $query
      ->fieldCondition($field)
      ->entityCondition('bundle', $bundle)
      ->execute();
    $this->assertTrue(!isset($found['test_entity']), 'No entities found after deleting');

    // There are 10 entities of this bundle when deleted fields are allowed, and
    // their values are correct.
    $query = new EntityFieldQuery();
    $found = $query
      ->fieldCondition($field)
      ->entityCondition('bundle', $bundle)
      ->deleted(TRUE)
      ->execute();
    field_attach_load($this->entity_type, $found[$this->entity_type], FIELD_LOAD_CURRENT, array('field_id' => $field['id'], 'deleted' => 1));
    $this->assertEqual(count($found['test_entity']), 10, 'Correct number of entities found after deleting');
    foreach ($found['test_entity'] as $id => $entity) {
      $this->assertEqual($this->entities[$id]->{$field['field_name']}, $entity->{$field['field_name']}, "Entity $id with deleted data loaded correctly");
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
