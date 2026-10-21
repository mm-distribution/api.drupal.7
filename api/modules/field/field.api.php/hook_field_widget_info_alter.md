# hook_field_widget_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 831–839 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L831-L839)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_info_alter(&$info)
```

## Documentation

```text
Perform alterations on Field API widget types.

@param $info
  Array of informations on widget types exposed by hook_field_widget_info()
  implementations.
```

## Code

```php
function hook_field_widget_info_alter(&$info) {
  // Add a setting to a widget type.
  $info['text_textfield']['settings'] += array(
    'mymodule_additional_setting' => 'default value',
  );

  // Let a new field type re-use an existing widget.
  $info['options_select']['field types'][] = 'my_field_type';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_info_alter()".

- [list_field_widget_info_alter()](../modules/list/list.module/list_field_widget_info_alter.md) — `modules/field/modules/list/list.module`
- [taxonomy_field_widget_info_alter()](../../taxonomy/taxonomy.module/taxonomy_field_widget_info_alter.md) — `modules/taxonomy/taxonomy.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
