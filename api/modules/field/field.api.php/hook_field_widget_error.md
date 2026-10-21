# hook_field_widget_error()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1040–1042 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1040-L1042)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Flag a field-level validation error.

@param $element
  An array containing the form element for the widget. The error needs to be
  flagged on the right sub-element, according to the widget's internal
  structure.
@param $error
  An associative array with the following key-value pairs, as returned by
  hook_field_validate():
  - error: the error code. Complex widgets might need to report different
    errors to different form elements inside the widget.
  - message: the human readable message to be displayed.
@param $form
  The form structure where field elements are attached to. This might be a
  full form structure, or a sub-element of a larger form.
@param $form_state
  An associative array containing the current state of the form.
```

## Code

```php
function hook_field_widget_error($element, $error, $form, &$form_state) {
  form_error($element, $error['message']);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_error()".

- [field_test_field_widget_error()](../tests/field_test.field.inc/field_test_field_widget_error.md) — `modules/field/tests/field_test.field.inc`
- [number_field_widget_error()](../modules/number/number.module/number_field_widget_error.md) — `modules/field/modules/number/number.module`
- [options_field_widget_error()](../modules/options/options.module/options_field_widget_error.md) — `modules/field/modules/options/options.module`
- [taxonomy_field_widget_error()](../../taxonomy/taxonomy.module/taxonomy_field_widget_error.md) — `modules/taxonomy/taxonomy.module`
- [text_field_widget_error()](../modules/text/text.module/text_field_widget_error.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
