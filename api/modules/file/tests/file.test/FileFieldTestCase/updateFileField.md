# FileFieldTestCase::updateFileField()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 113–119 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L113-L119)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function updateFileField($name, $type_name, $instance_settings = array(), $widget_settings = array())
```

## Documentation

```text
Updates an existing file field with new settings.
```

## Code

```php
  function updateFileField($name, $type_name, $instance_settings = array(), $widget_settings = array()) {
    $instance = field_info_instance('node', $name, $type_name);
    $instance['settings'] = array_merge($instance['settings'], $instance_settings);
    $instance['widget']['settings'] = array_merge($instance['widget']['settings'], $widget_settings);

    field_update_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
