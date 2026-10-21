# FieldCrudTestCase::_testActiveHelper()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2848–2874 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2848-L2874)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function _testActiveHelper($field_definition, $modules)
```

## Documentation

```text
Helper function for testActive().

Test dependency between a field and a set of modules.

@param $field_definition
  A field definition.
@param $modules
  An aray of module names. The field will be tested to be inactive as long
  as any of those modules is disabled.
```

## Code

```php
  function _testActiveHelper($field_definition, $modules) {
    $field_name = $field_definition['field_name'];

    // Read the field.
    $field = field_read_field($field_name);
    $this->assertTrue($field_definition <= $field, 'The field was properly read.');

    module_disable($modules, FALSE);

    $fields = field_read_fields(array('field_name' => $field_name), array('include_inactive' => TRUE));
    $this->assertTrue(isset($fields[$field_name]) && $field_definition < $field, 'The field is properly read when explicitly fetching inactive fields.');

    // Re-enable modules one by one, and check that the field is still inactive
    // while some modules remain disabled.
    while ($modules) {
      $field = field_read_field($field_name);
      $this->assertTrue(empty($field), format_string('%modules disabled. The field is marked inactive.', array('%modules' => implode(', ', $modules))));

      $module = array_shift($modules);
      module_enable(array($module), FALSE);
    }

    // Check that the field is active again after all modules have been
    // enabled.
    $field = field_read_field($field_name);
    $this->assertTrue($field_definition <= $field, 'The field was was marked active.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
