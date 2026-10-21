# form_options_flatten()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2688–2692 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2688-L2692)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_options_flatten($array)
```

## Documentation

```text
Allows PHP array processing of multiple select options with the same value.

Used for form select elements which need to validate HTML option groups
and multiple options which may return the same value. Associative PHP arrays
cannot handle these structures, since they share a common key.

@param $array
  The form options array to process.

@return
  An array with all hierarchical elements flattened to a single array.
```

## Code

```php
function form_options_flatten($array) {
  // Always reset static var when first entering the recursion.
  drupal_static_reset('_form_options_flatten');
  return _form_options_flatten($array);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
