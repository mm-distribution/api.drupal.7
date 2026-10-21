# FieldCrudTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2390–2393 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2390-L2393)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // field_update_field() tests use number.module
    parent::setUp('field_test', 'number');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
