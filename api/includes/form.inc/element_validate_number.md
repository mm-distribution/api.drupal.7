# element_validate_number()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4459–4464 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4459-L4464)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function element_validate_number($element, &$form_state)
```

## Documentation

```text
Form element validation handler for number elements.
```

## Code

```php
function element_validate_number($element, &$form_state) {
  $value = $element['#value'];
  if ($value != '' && !is_numeric($value)) {
    form_error($element, t('%name must be a number.', array('%name' => $element['#title'])));
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
