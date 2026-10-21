# _form_options_flatten()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2699–2715 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2699-L2715)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_options_flatten($array)
```

## Documentation

```text
Iterates over an array and returns a flat array with duplicate keys removed.

This function also handles cases where objects are passed as array values.
```

## Code

```php
function _form_options_flatten($array) {
  $return = &drupal_static(__FUNCTION__);

  foreach ($array as $key => $value) {
    if (is_object($value)) {
      _form_options_flatten($value->option);
    }
    elseif (is_array($value)) {
      _form_options_flatten($value);
    }
    else {
      $return[$key] = 1;
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
