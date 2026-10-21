# FieldCrudTestCase

- **Type:** Class
- **File:** [`modules/field/tests/field.test`](_file.md), lines 2376–2875 · [local source](../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2376-L2875)
- **Module/theme:** field_test_schema_alter

## Signature

```php
class FieldCrudTestCase extends FieldTestCase
```

## Documentation

_No docblock in source._

## Properties

### $field

```php
protected $field;
```

### $another_field

```php
protected $another_field;
```

### $instance_definition

```php
protected $instance_definition;
```

### $another_instance_definition

```php
protected $another_instance_definition;
```

## Methods (derived index)

- [getInfo()](FieldCrudTestCase/getInfo.md)
- [setUp()](FieldCrudTestCase/setUp.md)
- [testCreateField()](FieldCrudTestCase/testCreateField.md) — Test the creation of a field.
- [testCreateFieldFail()](FieldCrudTestCase/testCreateFieldFail.md) — Test failure to create a field.
- [testReadField()](FieldCrudTestCase/testReadField.md) — Test reading back a field definition.
- [testReadFields()](FieldCrudTestCase/testReadFields.md) — Tests reading field definitions.
- [testFieldIndexes()](FieldCrudTestCase/testFieldIndexes.md) — Test creation of indexes on data column.
- [testDeleteField()](FieldCrudTestCase/testDeleteField.md) — Test the deletion of a field.
- [testUpdateNonExistentField()](FieldCrudTestCase/testUpdateNonExistentField.md)
- [testUpdateFieldType()](FieldCrudTestCase/testUpdateFieldType.md)
- [testUpdateField()](FieldCrudTestCase/testUpdateField.md) — Test updating a field.
- [testUpdateFieldForbid()](FieldCrudTestCase/testUpdateFieldForbid.md) — Test field type modules forbidding an update.
- [testActive()](FieldCrudTestCase/testActive.md) — Test that fields are properly marked active or inactive.
- [_testActiveHelper()](FieldCrudTestCase/_testActiveHelper.md) — Helper function for testActive().

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
