# form_type_textfield_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2612–2621 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2612-L2621)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_textfield_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a textfield form element.

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
function form_type_textfield_value($element, $input = FALSE) {
  if ($input !== FALSE && $input !== NULL) {
    // This should be a string, but allow other scalars since they might be
    // valid input in programmatic form submissions.
    if (!is_scalar($input)) {
      $input = '';
    }
    return str_replace(array("\r", "\n"), '', (string) $input);
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
