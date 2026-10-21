# FieldBulkDeleteTestCase

- **Type:** Class
- **File:** [`modules/field/tests/field.test`](_file.md), lines 3506–3831 · [local source](../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3506-L3831)
- **Module/theme:** field_test_schema_alter

## Signature

```php
class FieldBulkDeleteTestCase extends FieldTestCase
```

## Documentation

```text
Unit test class for field bulk delete and batch purge functionality.
```

## Properties

### $field

```php
protected $field;
```

### $fields

```php
protected $fields;
```

### $instances

```php
protected $instances;
```

### $entities

```php
protected $entities;
```

### $entities_by_bundles

```php
protected $entities_by_bundles;
```

### $bundles

```php
protected $bundles;
```

### $entity_type

```php
protected $entity_type;
```

## Methods (derived index)

- [getInfo()](FieldBulkDeleteTestCase/getInfo.md)
- [_generateStubEntities()](FieldBulkDeleteTestCase/_generateStubEntities.md) — Convenience function for Field API tests.
- [checkHooksInvocations()](FieldBulkDeleteTestCase/checkHooksInvocations.md) — Tests that the expected hooks have been invoked on the expected entities.
- [setUp()](FieldBulkDeleteTestCase/setUp.md)
- [testDeleteFieldInstance()](FieldBulkDeleteTestCase/testDeleteFieldInstance.md) — Verify that deleting an instance leaves the field data items in the database and that the appropriate Field API functions can operate on the deleted data and instance.
- [testPurgeInstance()](FieldBulkDeleteTestCase/testPurgeInstance.md) — Verify that field data items and instances are purged when an instance is deleted.
- [testPurgeField()](FieldBulkDeleteTestCase/testPurgeField.md) — Verify that fields are preserved and purged correctly as multiple instances are deleted and purged.

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
