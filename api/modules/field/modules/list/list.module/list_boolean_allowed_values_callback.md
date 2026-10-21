# list_boolean_allowed_values_callback()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 203–207 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L203-L207)
- **Module/theme:** list

## Signature

```php
function list_boolean_allowed_values_callback($element, $input, $form_state)
```

## Documentation

```text
Form element #value_callback: assembles the allowed values for 'boolean' fields.
```

## Code

```php
function list_boolean_allowed_values_callback($element, $input, $form_state) {
  $on = drupal_array_get_nested_value($form_state['input'], $element['#on_parents']);
  $off = drupal_array_get_nested_value($form_state['input'], $element['#off_parents']);
  return array($off, $on);
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
