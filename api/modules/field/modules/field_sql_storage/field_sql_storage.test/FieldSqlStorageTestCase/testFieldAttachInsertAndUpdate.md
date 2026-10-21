# FieldSqlStorageTestCase::testFieldAttachInsertAndUpdate()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 140–216 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L140-L216)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldAttachInsertAndUpdate()
```

## Documentation

```text
Reads mysql to verify correct data is
written when using insert and update.
```

## Code

```php
  function testFieldAttachInsertAndUpdate() {
    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;

    // Test insert.
    $values = array();
    // Note: we try to insert one extra value ('<=' instead of '<').
    // TODO : test empty values filtering and "compression" (store consecutive deltas).
    for ($delta = 0; $delta <= $this->field['cardinality']; $delta++) {
      $values[$delta]['value'] = mt_rand(1, 127);
    }
    $entity->{$this->field_name}[$langcode] = $rev_values[0] = $values;
    field_attach_insert($entity_type, $entity);

    $rows = db_select($this->table, 't')->fields('t')->execute()->fetchAllAssoc('delta', PDO::FETCH_ASSOC);
    foreach ($values as $delta => $value) {
      if ($delta < $this->field['cardinality']) {
        $this->assertEqual($rows[$delta][$this->field_name . '_value'], $value['value'], format_string("Value %delta is inserted correctly", array('%delta' => $delta)));
      }
      else {
        $this->assertFalse(array_key_exists($delta, $rows), "No extraneous value gets inserted.");
      }
    }

    // Test update.
    $entity = field_test_create_stub_entity(0, 1, $this->instance['bundle']);
    $values = array();
    // Note: we try to update one extra value ('<=' instead of '<').
    for ($delta = 0; $delta <= $this->field['cardinality']; $delta++) {
      $values[$delta]['value'] = mt_rand(1, 127);
    }
    $entity->{$this->field_name}[$langcode] = $rev_values[1] = $values;
    field_attach_update($entity_type, $entity);
    $rows = db_select($this->table, 't')->fields('t')->execute()->fetchAllAssoc('delta', PDO::FETCH_ASSOC);
    foreach ($values as $delta => $value) {
      if ($delta < $this->field['cardinality']) {
        $this->assertEqual($rows[$delta][$this->field_name . '_value'], $value['value'], format_string("Value %delta is updated correctly", array('%delta' => $delta)));
      }
      else {
        $this->assertFalse(array_key_exists($delta, $rows), "No extraneous value gets updated.");
      }
    }

    // Check that data for both revisions are in the revision table.
    // We make sure each value is stored correctly, then unset it.
    // When an entire revision's values are unset (remembering that we
    // put one extra value in $values per revision), unset the entire
    // revision. Then, if $rev_values is empty at the end, all
    // revision data was found.
    $results = db_select($this->revision_table, 't')->fields('t')->execute();
    foreach ($results as $row) {
      $this->assertEqual($row->{$this->field_name . '_value'}, $rev_values[$row->revision_id][$row->delta]['value'], "Value {$row->delta} for revision {$row->revision_id} stored correctly");
      unset($rev_values[$row->revision_id][$row->delta]);
      if (count($rev_values[$row->revision_id]) == 1) {
        unset($rev_values[$row->revision_id]);
      }
    }
    $this->assertTrue(empty($rev_values), "All values for all revisions are stored in revision table {$this->revision_table}");

    // Check that update leaves the field data untouched if
    // $entity->{$field_name} is absent.
    unset($entity->{$this->field_name});
    field_attach_update($entity_type, $entity);
    $rows = db_select($this->table, 't')->fields('t')->execute()->fetchAllAssoc('delta', PDO::FETCH_ASSOC);
    foreach ($values as $delta => $value) {
      if ($delta < $this->field['cardinality']) {
        $this->assertEqual($rows[$delta][$this->field_name . '_value'], $value['value'], format_string("Update with no field_name entry leaves value %delta untouched", array('%delta' => $delta)));
      }
    }

    // Check that update with an empty $entity->$field_name empties the field.
    $entity->{$this->field_name} = NULL;
    field_attach_update($entity_type, $entity);
    $rows = db_select($this->table, 't')->fields('t')->execute()->fetchAllAssoc('delta', PDO::FETCH_ASSOC);
    $this->assertEqual(count($rows), 0, "Update with an empty field_name entry empties the field.");
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
