# password_confirm_validate()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3046–3066 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3046-L3066)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function password_confirm_validate($element, &$element_state)
```

## Documentation

```text
Validates a password_confirm element.
```

## Code

```php
function password_confirm_validate($element, &$element_state) {
  $pass1 = trim($element['pass1']['#value']);
  $pass2 = trim($element['pass2']['#value']);
  if (strlen($pass1) > 0 || strlen($pass2) > 0) {
    if (strcmp($pass1, $pass2)) {
      form_error($element, t('The specified passwords do not match.'));
    }
  }
  elseif ($element['#required'] && !empty($element_state['input'])) {
    form_error($element, t('Password field is required.'));
  }

  // Password field must be converted from a two-element array into a single
  // string regardless of validation results.
  form_set_value($element['pass1'], NULL, $element_state);
  form_set_value($element['pass2'], NULL, $element_state);
  form_set_value($element, $pass1, $element_state);

  return $element;

}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
