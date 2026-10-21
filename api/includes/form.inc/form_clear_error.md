# form_clear_error()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1680–1682 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1680-L1682)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_clear_error()
```

## Documentation

```text
Clears all errors against all form elements made by form_set_error().
```

## Code

```php
function form_clear_error() {
  drupal_static_reset('form_set_error');
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
