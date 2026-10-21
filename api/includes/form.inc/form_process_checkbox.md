# form_process_checkbox()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3303–3325 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3303-L3325)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_checkbox($element, $form_state)
```

## Documentation

```text
Sets the #checked property of a checkbox element.
```

## Code

```php
function form_process_checkbox($element, $form_state) {
  $value = $element['#value'];
  $return_value = $element['#return_value'];
  // On form submission, the #value of an available and enabled checked
  // checkbox is #return_value, and the #value of an available and enabled
  // unchecked checkbox is integer 0. On not submitted forms, and for
  // checkboxes with #access=FALSE or #disabled=TRUE, the #value is
  // #default_value (integer 0 if #default_value is NULL). Most of the time,
  // a string comparison of #value and #return_value is sufficient for
  // determining the "checked" state, but a value of TRUE always means checked
  // (even if #return_value is 'foo'), and a value of FALSE or integer 0 always
  // means unchecked (even if #return_value is '' or '0').
  if ($value === TRUE || $value === FALSE || $value === 0) {
    $element['#checked'] = (bool) $value;
  }
  else {
    // Compare as strings, so that 15 is not considered equal to '15foo', but 1
    // is considered equal to '1'. This cast does not imply that either #value
    // or #return_value is expected to be a string.
    $element['#checked'] = ((string) $value === (string) $return_value);
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
