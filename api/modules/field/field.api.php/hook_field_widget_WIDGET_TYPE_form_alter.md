# hook_field_widget_WIDGET_TYPE_form_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 982–987 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L982-L987)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_WIDGET_TYPE_form_alter(&$element, &$form_state, $context)
```

## Documentation

```text
Alter widget forms for a specific widget provided by another module.

Modules can implement hook_field_widget_WIDGET_TYPE_form_alter() to modify a
specific widget form, rather than using hook_field_widget_form_alter() and
checking the widget type.

@param $element
  The field widget form element as constructed by hook_field_widget_form().
@param $form_state
  An associative array containing the current state of the form.
@param $context
  An associative array containing the following key-value pairs, matching the
  arguments received by hook_field_widget_form():
  - "form": The form structure where widgets are being attached to. This
    might be a full form structure, or a sub-element of a larger form.
  - "field": The field structure.
  - "instance": The field instance structure.
  - "langcode": The language associated with $items.
  - "items": Array of default values for this field.
  - "delta": The order of this item in the array of subelements (0, 1, 2,
    etc).

@see hook_field_widget_form()
@see hook_field_widget_form_alter()
```

## Code

```php
function hook_field_widget_WIDGET_TYPE_form_alter(&$element, &$form_state, $context) {
  // Code here will only act on widgets of type WIDGET_TYPE.  For example,
  // hook_field_widget_mymodule_autocomplete_form_alter() will only act on
  // widgets of type 'mymodule_autocomplete'.
  $element['#autocomplete_path'] = 'mymodule/autocomplete_path';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_WIDGET_TYPE_form_alter()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
