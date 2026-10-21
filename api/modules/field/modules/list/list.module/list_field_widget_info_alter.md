# list_field_widget_info_alter()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 423–433 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L423-L433)
- **Module/theme:** list
- **Implements:** [hook_field_widget_info_alter()](../../../field.api.php/hook_field_widget_info_alter.md)

## Signature

```php
function list_field_widget_info_alter(&$info)
```

## Documentation

```text
Implements hook_field_widget_info_alter().

The List module does not implement widgets of its own, but reuses the
widgets defined in options.module.

@see list_options_list()
```

## Code

```php
function list_field_widget_info_alter(&$info) {
  $widgets = array(
    'options_select' => array('list_integer', 'list_float', 'list_text'),
    'options_buttons' => array('list_integer', 'list_float', 'list_text', 'list_boolean'),
    'options_onoff' => array('list_boolean'),
  );

  foreach ($widgets as $widget => $field_types) {
    $info[$widget]['field types'] = array_merge($info[$widget]['field types'], $field_types);
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
