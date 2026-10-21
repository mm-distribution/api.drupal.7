# color_palette_color_value()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 313–328 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L313-L328)
- **Module/theme:** color

## Signature

```php
function color_palette_color_value($element, $input = FALSE, $form_state = array())
```

## Documentation

```text
Determines the value for a palette color field.

@param $element
  The form element whose value is being populated.
@param $input
  The incoming input to populate the form element. If this is FALSE,
  the element's default value should be returned.
@param $form_state
  A keyed array containing the current state of the form.

@return
  The data that will appear in the $form_state['values'] collection for this
  element. Return nothing to use the default.
```

## Code

```php
function color_palette_color_value($element, $input = FALSE, $form_state = array()) {
  // If we suspect a possible cross-site request forgery attack, only accept
  // hexadecimal CSS color strings from user input, to avoid problems when this
  // value is used in the JavaScript preview.
  if ($input !== FALSE) {
    // Start with the provided value for this textfield, and validate that if
    // necessary, falling back on the default value.
    $value = form_type_textfield_value($element, $input, $form_state);
    if (!$value || !isset($form_state['complete form']['#token']) || color_valid_hexadecimal_string($value) || drupal_valid_token($form_state['values']['form_token'], $form_state['complete form']['#token'])) {
      return $value;
    }
    else {
      return $element['#default_value'];
    }
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
