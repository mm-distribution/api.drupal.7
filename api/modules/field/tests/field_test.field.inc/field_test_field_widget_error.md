# field_test_field_widget_error()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 227–240 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L227-L240)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_error()](../../field.api.php/hook_field_widget_error.md)

## Signature

```php
function field_test_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_widget_error().
```

## Code

```php
function field_test_field_widget_error($element, $error, $form, &$form_state) {
  // @todo No easy way to differenciate widget types, we should receive it as a
  // parameter.
  if (isset($element['value'])) {
    // Widget is test_field_widget.
    $error_element = $element['value'];
  }
  else {
    // Widget is test_field_widget_multiple.
    $error_element = $element;
  }

  form_error($error_element, $error['message']);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
