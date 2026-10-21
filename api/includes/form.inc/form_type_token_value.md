# form_type_token_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2636–2640 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2636-L2640)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_token_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for form's token value.

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
function form_type_token_value($element, $input = FALSE) {
  if ($input !== FALSE) {
    return (string) $input;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
