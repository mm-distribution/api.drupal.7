# form_type_radios_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2480–2504 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2480-L2504)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_radios_value(&$element, $input = FALSE)
```

## Documentation

```text
Form value callback: Determines the value for a #type radios form element.

@param $element
  The form element whose value is being populated.
@param $input
  (optional) The incoming input to populate the form element. If FALSE, the
  element's default value is returned. Defaults to FALSE.

@return
  The data that will appear in $form_state['values'] for this element, or
  nothing to use the default.
```

## Code

```php
function form_type_radios_value(&$element, $input = FALSE) {
  if ($input !== FALSE) {
    // When there's user input (including NULL), return it as the value.
    // However, if NULL is submitted, _form_builder_handle_input_element() will
    // apply the default value, and we want that validated against #options
    // unless it's empty. (An empty #default_value, such as NULL or FALSE, can
    // be used to indicate that no radio button is selected by default.)
    if (!isset($input) && !empty($element['#default_value'])) {
      $element['#needs_validation'] = TRUE;
    }
    return $input;
  }
  else {
    // For default value handling, simply return #default_value. Additionally,
    // for a NULL default value, set #has_garbage_value to prevent
    // _form_builder_handle_input_element() converting the NULL to an empty
    // string, so that code can distinguish between nothing selected and the
    // selection of a radio button whose value is an empty string.
    $value = isset($element['#default_value']) ? $element['#default_value'] : NULL;
    if (!isset($value)) {
      $element['#has_garbage_value'] = TRUE;
    }
    return $value;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
