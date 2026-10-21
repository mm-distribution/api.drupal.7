# FieldInfoTestCase::testFieldInfoCache()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1595–1615 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1595-L1615)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldInfoCache()
```

## Documentation

```text
Tests that the field info cache can be built correctly.
```

## Code

```php
  function testFieldInfoCache() {
    // Create a test field and ensure it's in the array returned by
    // field_info_fields().
    $field_name = drupal_strtolower($this->randomName());
    $field = array(
      'field_name' => $field_name,
      'type' => 'test_field',
    );
    field_create_field($field);
    $fields = field_info_fields();
    $this->assertTrue(isset($fields[$field_name]), 'The test field is initially found in the array returned by field_info_fields().');

    // Now rebuild the field info cache, and set a variable which will cause
    // the cache to be cleared while it's being rebuilt; see
    // field_test_entity_info(). Ensure the test field is still in the returned
    // array.
    field_info_cache_clear();
    variable_set('field_test_clear_info_cache_in_hook_entity_info', TRUE);
    $fields = field_info_fields();
    $this->assertTrue(isset($fields[$field_name]), 'The test field is found in the array returned by field_info_fields() even if its cache is cleared while being rebuilt.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
