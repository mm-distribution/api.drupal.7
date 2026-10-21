# weight_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3183–3190 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3183-L3190)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function weight_value(&$form)
```

## Documentation

```text
Sets the value for a weight element, with zero as a default.
```

## Code

```php
function weight_value(&$form) {
  if (isset($form['#default_value'])) {
    $form['#value'] = $form['#default_value'];
  }
  else {
    $form['#value'] = 0;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
