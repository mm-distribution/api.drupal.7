# form_type_password_confirm_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2519–2535 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2519-L2535)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_password_confirm_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a password_confirm form element.

@param $element
  The form element whose value is being populated.
@param $input
  The incoming input to populate the form element. If this is FALSE,
  the element's default value should be returned.

@return
  The data that will appear in $form_state['values'] for this element, or
  nothing to use the default.
```

## Code

```php
function form_type_password_confirm_value($element, $input = FALSE) {
  if ($input === FALSE) {
    $element += array('#default_value' => array());
    return $element['#default_value'] + array('pass1' => '', 'pass2' => '');
  }
  $value = array('pass1' => '', 'pass2' => '');
  // Throw out all invalid array keys; we only allow pass1 and pass2.
  foreach ($value as $allowed_key => $default) {
    // These should be strings, but allow other scalars since they might be
    // valid input in programmatic form submissions. Any nested array values
    // are ignored.
    if (isset($input[$allowed_key]) && is_scalar($input[$allowed_key])) {
      $value[$allowed_key] = (string) $input[$allowed_key];
    }
  }
  return $value;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
