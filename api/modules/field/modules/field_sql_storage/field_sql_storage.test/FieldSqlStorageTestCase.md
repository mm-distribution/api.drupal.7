# FieldSqlStorageTestCase

- **Type:** Class
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](_file.md), lines 14–682 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L14-L682)
- **Module/theme:** field_sql_storage

## Signature

```php
class FieldSqlStorageTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests field storage.
```

## Properties

### $field

```php
protected $field;
```

### $instance

```php
protected $instance;
```

### $field_name

```php
protected $field_name;
```

### $table

```php
protected $table;
```

### $revision_table

```php
protected $revision_table;
```

## Methods (derived index)

- [getInfo()](FieldSqlStorageTestCase/getInfo.md)
- [setUp()](FieldSqlStorageTestCase/setUp.md)
- [testFieldAttachLoad()](FieldSqlStorageTestCase/testFieldAttachLoad.md) — Uses the mysql tables and records to verify field_load_revision works correctly.
- [testFieldSqlSchemaForEntityWithStringIdentifier()](FieldSqlStorageTestCase/testFieldSqlSchemaForEntityWithStringIdentifier.md) — Tests adding a field with an entity ID type of string.
- [testFieldAttachInsertAndUpdate()](FieldSqlStorageTestCase/testFieldAttachInsertAndUpdate.md) — Reads mysql to verify correct data is written when using insert and update.
- [testFieldAttachSaveMissingData()](FieldSqlStorageTestCase/testFieldAttachSaveMissingData.md) — Tests insert and update with missing or NULL fields.
- [testFieldCompareDataModification()](FieldSqlStorageTestCase/testFieldCompareDataModification.md) — Tests the expected return values of _field_sql_storage_write_compare().
- [testUpdateFieldSchemaWithData()](FieldSqlStorageTestCase/testUpdateFieldSchemaWithData.md) — Test trying to update a field with data.
- [testFieldUpdateFailure()](FieldSqlStorageTestCase/testFieldUpdateFailure.md) — Test that failure to create fields is handled gracefully.
- [testFieldUpdateIndexesWithData()](FieldSqlStorageTestCase/testFieldUpdateIndexesWithData.md) — Test adding and removing indexes while data is present.
- [testFieldStorageDetails()](FieldSqlStorageTestCase/testFieldStorageDetails.md) — Test the storage details.
- [testFieldSqlStorageForeignKeys()](FieldSqlStorageTestCase/testFieldSqlStorageForeignKeys.md) — Test foreign key support.
- [testFieldSqlStorageMultipleConditionsSameColumn()](FieldSqlStorageTestCase/testFieldSqlStorageMultipleConditionsSameColumn.md) — Test handling multiple conditions on one column of a field.
- [testFieldSqlStorageMultipleConditionsDifferentColumns()](FieldSqlStorageTestCase/testFieldSqlStorageMultipleConditionsDifferentColumns.md) — Test handling multiple conditions on multiple columns of one field.
- [testFieldSqlStorageMultipleConditionsDifferentColumnsMultipleLanguages()](FieldSqlStorageTestCase/testFieldSqlStorageMultipleConditionsDifferentColumnsMultipleLanguages.md) — Test handling multiple conditions on multiple columns of one field for multiple languages.

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
