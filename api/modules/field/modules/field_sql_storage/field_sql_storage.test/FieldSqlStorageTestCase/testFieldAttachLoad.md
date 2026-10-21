# FieldSqlStorageTestCase::testFieldAttachLoad()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 49–111 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L49-L111)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldAttachLoad()
```

## Documentation

```text
Uses the mysql tables and records to verify
field_load_revision works correctly.
```

## Code

```php
  function testFieldAttachLoad() {
    $entity_type = 'test_entity';
    $eid = 0;
    $langcode = LANGUAGE_NONE;

    $columns = array('entity_type', 'entity_id', 'revision_id', 'delta', 'language', $this->field_name . '_value');

    // Insert data for four revisions to the field revisions table
    $query = db_insert($this->revision_table)->fields($columns);
    for ($evid = 0; $evid < 4; ++$evid) {
      $values[$evid] = array();
      // Note: we insert one extra value ('<=' instead of '<').
      for ($delta = 0; $delta <= $this->field['cardinality']; $delta++) {
        $value = mt_rand(1, 127);
        $values[$evid][] = $value;
        $query->values(array($entity_type, $eid, $evid, $delta, $langcode, $value));
      }
    }
    $query->execute();

    // Insert data for the "most current revision" into the field table
    $query = db_insert($this->table)->fields($columns);
    foreach ($values[0] as $delta => $value) {
      $query->values(array($entity_type, $eid, 0, $delta, $langcode, $value));
    }
    $query->execute();

    // Load the "most current revision"
    $entity = field_test_create_stub_entity($eid, 0, $this->instance['bundle']);
    field_attach_load($entity_type, array($eid => $entity));
    foreach ($values[0] as $delta => $value) {
      if ($delta < $this->field['cardinality']) {
        $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['value'], $value, "Value $delta is loaded correctly for current revision");
      }
      else {
        $this->assertFalse(array_key_exists($delta, $entity->{$this->field_name}[$langcode]), "No extraneous value gets loaded for current revision.");
      }
    }

    // Load every revision
    for ($evid = 0; $evid < 4; ++$evid) {
      $entity = field_test_create_stub_entity($eid, $evid, $this->instance['bundle']);
      field_attach_load_revision($entity_type, array($eid => $entity));
      foreach ($values[$evid] as $delta => $value) {
        if ($delta < $this->field['cardinality']) {
          $this->assertEqual($entity->{$this->field_name}[$langcode][$delta]['value'], $value, "Value $delta for revision $evid is loaded correctly");
        }
        else {
          $this->assertFalse(array_key_exists($delta, $entity->{$this->field_name}[$langcode]), "No extraneous value gets loaded for revision $evid.");
        }
      }
    }

    // Add a translation in an unavailable language and verify it is not loaded.
    $eid = $evid = 1;
    $unavailable_language = 'xx';
    $entity = field_test_create_stub_entity($eid, $evid, $this->instance['bundle']);
    $values = array($entity_type, $eid, $evid, 0, $unavailable_language, mt_rand(1, 127));
    db_insert($this->table)->fields($columns)->values($values)->execute();
    db_insert($this->revision_table)->fields($columns)->values($values)->execute();
    field_attach_load($entity_type, array($eid => $entity));
    $this->assertFalse(array_key_exists($unavailable_language, $entity->{$this->field_name}), 'Field translation in an unavailable language ignored');
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
