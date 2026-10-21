# FieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 17–28 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L17-L28)
- **Class:** [FieldTestCase](../FieldTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function setUp()
```

## Documentation

```text
Set the default field storage backend for fields created during tests.
```

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
    parent::setUp($modules);
    // Set default storage backend.
    variable_set('field_storage_default', $this->default_storage);
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
