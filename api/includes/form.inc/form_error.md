# form_error()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1718–1720 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1718-L1720)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_error(&$element, $message = '')
```

## Documentation

```text
Flags an element as having an error.
```

## Code

```php
function form_error(&$element, $message = '') {
  form_set_error(implode('][', $element['#parents']), $message);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
