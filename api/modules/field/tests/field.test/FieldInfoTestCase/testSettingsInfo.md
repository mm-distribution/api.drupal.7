# FieldInfoTestCase::testSettingsInfo()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1570–1590 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1570-L1590)
- **Class:** [FieldInfoTestCase](../FieldInfoTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testSettingsInfo()
```

## Documentation

```text
Test that the field_info settings convenience functions work.
```

## Code

```php
  function testSettingsInfo() {
    $info = field_test_field_info();
    // We need to account for the existence of user_field_info_alter().
    foreach (array_keys($info) as $name) {
      $info[$name]['instance_settings']['user_register_form'] = FALSE;
    }
    foreach ($info as $type => $data) {
      $this->assertIdentical(field_info_field_settings($type), $data['settings'], format_string("field_info_field_settings returns %type's field settings", array('%type' => $type)));
      $this->assertIdentical(field_info_instance_settings($type), $data['instance_settings'], format_string("field_info_field_settings returns %type's field instance settings", array('%type' => $type)));
    }

    $info = field_test_field_widget_info();
    foreach ($info as $type => $data) {
      $this->assertIdentical(field_info_widget_settings($type), $data['settings'], format_string("field_info_widget_settings returns %type's widget settings", array('%type' => $type)));
    }

    $info = field_test_field_formatter_info();
    foreach ($info as $type => $data) {
      $this->assertIdentical(field_info_formatter_settings($type), $data['settings'], format_string("field_info_formatter_settings returns %type's formatter settings", array('%type' => $type)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
