# FieldSqlStorageTestCase::testFieldCompareDataModification()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 316–374 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L316-L374)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
public function testFieldCompareDataModification()
```

## Documentation

```text
Tests the expected return values of _field_sql_storage_write_compare().
```

## Code

```php
  public function testFieldCompareDataModification() {
    $langcode = LANGUAGE_NONE;
    $field_info = field_info_field($this->field_name);

    // Make sure we have 2 sample field values that are unique.
    $value1 = 0;
    $value2 = 0;
    while ($value1 == $value2) {
      $value1 = mt_rand();
      $value2 = (string) mt_rand();
    }

    // Create the 2 entities to compare.
    $entity = field_test_create_stub_entity();
    $entity->{$this->field_name}[$langcode][]['value'] = $value1;
    $entity1 = clone $entity;
    $entity2 = clone $entity;

    // Make sure that it correctly compares identical entities.
    $this->assert(!_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'The entities are identical.');

    // Compare to an empty object.
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, new stdClass()), 'The entity is not the same as an empty object.');

    // Change one of the values.
    $entity2->{$this->field_name}[$langcode][0]['value'] = $value2;
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'The values are not the same.');

    // Reset $entity2.
    $entity2 = clone $entity;

    // Duplicate the value on one of the entities.
    $entity1->{$this->field_name}[$langcode][]['value'] = $value1;
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'The fields do not have the same number of values.');

    // Add a second value to both entities.
    $entity2->{$this->field_name}[$langcode][]['value'] = $value2;
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'The values are not the same.');

    // Replace the array containing the value with the actual value.
    $entity2->{$this->field_name}[$langcode] = $entity2->{$this->field_name}[$langcode][0];
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'The array to hold field values is replaced by the value.');

    // Null one value.
    $entity2->{$this->field_name}[$langcode] = NULL;
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'One field is NULL and the other is not.');

    // Null both values.
    $entity1->{$this->field_name}[$langcode] = NULL;
    $this->assert(!_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'Both fields are NULL.');

    // Unset one of the fields.
    unset($entity2->{$this->field_name});
    $this->assert(_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'One field structure is unset.');

    // Unset both of the fields.
    unset($entity1->{$this->field_name});
    $this->assert(!_field_sql_storage_write_compare($field_info, $entity1, $entity2), 'Both field structures are unset.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
