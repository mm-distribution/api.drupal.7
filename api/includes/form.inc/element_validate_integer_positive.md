# element_validate_integer_positive()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4449–4454 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4449-L4454)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function element_validate_integer_positive($element, &$form_state)
```

## Documentation

```text
Form element validation handler for integer elements that must be positive.
```

## Code

```php
function element_validate_integer_positive($element, &$form_state) {
  $value = $element['#value'];
  if ($value !== '' && (!is_numeric($value) || intval($value) != $value || $value <= 0)) {
    form_error($element, t('%name must be a positive integer.', array('%name' => $element['#title'])));
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
