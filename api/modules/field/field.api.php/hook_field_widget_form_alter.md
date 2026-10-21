# hook_field_widget_form_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 948–954 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L948-L954)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_form_alter(&$element, &$form_state, $context)
```

## Documentation

```text
Alter forms for field widgets provided by other modules.

@param $element
  The field widget form element as constructed by hook_field_widget_form().
@param $form_state
  An associative array containing the current state of the form.
@param $context
  An associative array containing the following key-value pairs, matching the
  arguments received by hook_field_widget_form():
  - form: The form structure to which widgets are being attached. This may be
    a full form structure, or a sub-element of a larger form.
  - field: The field structure.
  - instance: The field instance structure.
  - langcode: The language associated with $items.
  - items: Array of default values for this field.
  - delta: The order of this item in the array of subelements (0, 1, 2, etc).

@see hook_field_widget_form()
@see hook_field_widget_WIDGET_TYPE_form_alter()
```

## Code

```php
function hook_field_widget_form_alter(&$element, &$form_state, $context) {
  // Add a css class to widget form elements for all fields of type mytype.
  if ($context['field']['type'] == 'mytype') {
    // Be sure not to overwrite existing attributes.
    $element['#attributes']['class'][] = 'myclass';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_form_alter()".

- [field_test_field_widget_form_alter()](../tests/field_test.module/field_test_field_widget_form_alter.md) — `modules/field/tests/field_test.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
