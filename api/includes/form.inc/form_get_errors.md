# form_get_errors()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1690–1695 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1690-L1695)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_get_errors()
```

## Documentation

```text
Returns an associative array of all errors if any.

@return array|null
  The form errors if any, NULL otherwise.
```

## Code

```php
function form_get_errors() {
  $form = form_set_error();
  if (!empty($form)) {
    return $form;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
