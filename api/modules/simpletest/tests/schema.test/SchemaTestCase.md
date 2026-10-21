# SchemaTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/schema.test`](_file.md), lines 11–440 · [local source](../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L11-L440)
- **Module/theme:** batch_test

## Signature

```php
class SchemaTestCase extends DrupalWebTestCase
```

## Documentation

```text
Unit tests for the Schema API.
```

## Properties

### $counter

```php
var $counter;
```

```text
A global counter for table and field creation.
```

## Methods (derived index)

- [getInfo()](SchemaTestCase/getInfo.md)
- [testSchema()](SchemaTestCase/testSchema.md)
- [tryInsert()](SchemaTestCase/tryInsert.md)
- [checkSchemaComment()](SchemaTestCase/checkSchemaComment.md) — Checks that a table or column comment matches a given description.
- [testUnsignedColumns()](SchemaTestCase/testUnsignedColumns.md) — Tests creating unsigned columns and data integrity thereof.
- [tryUnsignedInsert()](SchemaTestCase/tryUnsignedInsert.md) — Tries to insert a negative value into columns defined as unsigned.
- [testSchemaAddField()](SchemaTestCase/testSchemaAddField.md) — Test adding columns to an existing table.
- [assertFieldAdditionRemoval()](SchemaTestCase/assertFieldAdditionRemoval.md) — Assert that a given field can be added and removed from a table.
- [assertFieldCharacteristics()](SchemaTestCase/assertFieldCharacteristics.md) — Assert that a newly added field has the correct characteristics.
- [testFindTables()](SchemaTestCase/testFindTables.md) — Tests the findTables() method.

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
