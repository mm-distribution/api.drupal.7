# FieldAttachTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 84–98 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L84-L98)
- **Class:** [FieldAttachTestCase](../FieldAttachTestCase.md)
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
    // Since this is a base class for many test cases, support the same
    // flexibility that DrupalWebTestCase::setUp() has for the modules to be
    // passed in as either an array or a variable number of string arguments.
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    if (!in_array('field_test', $modules)) {
      $modules[] = 'field_test';
    }
    parent::setUp($modules);

    $this->createFieldWithInstance();
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
