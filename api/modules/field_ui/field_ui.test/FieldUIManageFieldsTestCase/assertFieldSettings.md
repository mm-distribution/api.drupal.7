# FieldUIManageFieldsTestCase::assertFieldSettings()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 276–287 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L276-L287)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function assertFieldSettings($bundle, $field_name, $string = 'dummy test string', $entity_type = 'node')
```

## Documentation

```text
Asserts field settings are as expected.

@param $bundle
  The bundle name for the instance.
@param $field_name
  The field name for the instance.
@param $string
  The settings text.
@param $entity_type
  The entity type for the instance.
```

## Code

```php
  function assertFieldSettings($bundle, $field_name, $string = 'dummy test string', $entity_type = 'node') {
    // Reset the fields info.
    field_info_cache_clear();
    // Assert field settings.
    $field = field_info_field($field_name);
    $this->assertTrue($field['settings']['test_field_setting'] == $string, 'Field settings were found.');

    // Assert instance and widget settings.
    $instance = field_info_instance($entity_type, $field_name, $bundle);
    $this->assertTrue($instance['settings']['test_instance_setting'] == $string, 'Field instance settings were found.');
    $this->assertTrue($instance['widget']['settings']['test_widget_setting'] == $string, 'Field widget settings were found.');
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
