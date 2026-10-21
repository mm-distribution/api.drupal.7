# element_validate_integer()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4439–4444 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4439-L4444)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function element_validate_integer($element, &$form_state)
```

## Documentation

```text
Form element validation handler for integer elements.
```

## Code

```php
function element_validate_integer($element, &$form_state) {
  $value = $element['#value'];
  if ($value !== '' && (!is_numeric($value) || intval($value) != $value)) {
    form_error($element, t('%name must be an integer.', array('%name' => $element['#title'])));
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
