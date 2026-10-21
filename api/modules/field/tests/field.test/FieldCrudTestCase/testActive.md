# FieldCrudTestCase::testActive()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2816–2835 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2816-L2835)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testActive()
```

## Documentation

```text
Test that fields are properly marked active or inactive.
```

## Code

```php
  function testActive() {
    $field_definition = array(
      'field_name' => 'field_1',
      'type' => 'test_field',
      // For this test, we need a storage backend provided by a different
      // module than field_test.module.
      'storage' => array(
        'type' => 'field_sql_storage',
      ),
    );
    field_create_field($field_definition);

    // Test disabling and enabling:
    // - the field type module,
    // - the storage module,
    // - both.
    $this->_testActiveHelper($field_definition, array('field_test'));
    $this->_testActiveHelper($field_definition, array('field_sql_storage'));
    $this->_testActiveHelper($field_definition, array('field_test', 'field_sql_storage'));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
