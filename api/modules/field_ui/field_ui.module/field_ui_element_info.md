# field_ui_element_info()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 316–324 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L316-L324)
- **Module/theme:** field_ui
- **Implements:** [hook_element_info()](../../system/system.api.php/hook_element_info.md)

## Signature

```php
function field_ui_element_info()
```

## Documentation

```text
Implements hook_element_info().
```

## Code

```php
function field_ui_element_info() {
  return array(
    'field_ui_table' => array(
      '#theme' => 'field_ui_table',
      '#pre_render' => array('field_ui_table_pre_render'),
      '#regions' => array('' => array()),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
