# FieldTestCase

- **Type:** Class
- **File:** [`modules/field/tests/field.test`](_file.md), lines 11–72 · [local source](../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L11-L72)
- **Module/theme:** field_test_schema_alter

## Signature

```php
class FieldTestCase extends DrupalWebTestCase
```

## Documentation

```text
Parent class for Field API tests.
```

## Properties

### $default_storage

```php
var $default_storage = 'field_sql_storage';
```

## Methods (derived index)

- [setUp()](FieldTestCase/setUp.md) — Set the default field storage backend for fields created during tests.
- [_generateTestFieldValues()](FieldTestCase/_generateTestFieldValues.md) — Generate random values for a field_test field.
- [assertFieldValues()](FieldTestCase/assertFieldValues.md) — Assert that a field has the expected values in an entity.

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
