# FieldSqlStorageTestCase::testFieldAttachSaveMissingData()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 221–311 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L221-L311)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldAttachSaveMissingData()
```

## Documentation

```text
Tests insert and update with missing or NULL fields.
```

## Code

```php
  function testFieldAttachSaveMissingData() {
    $entity_type = 'test_entity';
    $entity = field_test_create_stub_entity(0, 0, $this->instance['bundle']);
    $langcode = LANGUAGE_NONE;

    // Insert: Field is missing
    field_attach_insert($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 0, 'Missing field results in no inserts');

    // Insert: Field is NULL
    $entity->{$this->field_name} = NULL;
    field_attach_insert($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 0, 'NULL field results in no inserts');

    // Add some real data
    $entity->{$this->field_name}[$langcode] = array(0 => array('value' => 1));
    field_attach_insert($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 1, 'Field data saved');

    // Update: Field is missing. Data should survive.
    unset($entity->{$this->field_name});
    field_attach_update($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 1, 'Missing field leaves data in table');

    // Update: Field is NULL. Data should be wiped.
    $entity->{$this->field_name} = NULL;
    field_attach_update($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 0, 'NULL field leaves no data in table');

    // Add a translation in an unavailable language.
    $unavailable_language = 'xx';
    db_insert($this->table)
      ->fields(array('entity_type', 'bundle', 'deleted', 'entity_id', 'revision_id', 'delta', 'language'))
      ->values(array($entity_type, $this->instance['bundle'], 0, 0, 0, 0, $unavailable_language))
      ->execute();
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 1, 'Field translation in an unavailable language saved.');

    // Again add some real data.
    $entity->{$this->field_name}[$langcode] = array(0 => array('value' => 1));
    field_attach_insert($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 2, 'Field data saved.');

    // Update: Field translation is missing but field is not empty. Translation
    // data should survive.
    $entity->{$this->field_name}[$unavailable_language] = array(mt_rand(1, 127));
    unset($entity->{$this->field_name}[$langcode]);
    field_attach_update($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 2, 'Missing field translation leaves data in table.');

    // Update: Field translation is NULL but field is not empty. Translation
    // data should be wiped.
    $entity->{$this->field_name}[$langcode] = NULL;
    field_attach_update($entity_type, $entity);
    $count = db_select($this->table)
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($count, 1, 'NULL field translation is wiped.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
