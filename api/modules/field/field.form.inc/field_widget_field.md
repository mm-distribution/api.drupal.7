# field_widget_field()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 587–590 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L587-L590)
- **Module/theme:** field

## Signature

```php
function field_widget_field($element, $form_state)
```

## Documentation

```text
Retrieves the field definition for a widget's helper callbacks.

Widgets helper element callbacks (such as #process, #element_validate,
#value_callback, ...) should use field_widget_field() and
field_widget_instance() instead of field_info_field() and
field_info_instance() when they need to access field or instance properties.
See hook_field_widget_form() for more details.

@param $element
  The structured array for the widget.
@param $form_state
  The form state.

@return
  The $field definition array for the current widget.

@see field_widget_instance()
@see hook_field_widget_form()
```

## Code

```php
function field_widget_field($element, $form_state) {
  $field_state = field_form_get_state($element['#field_parents'], $element['#field_name'], $element['#language'], $form_state);
  return $field_state['field'];
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
