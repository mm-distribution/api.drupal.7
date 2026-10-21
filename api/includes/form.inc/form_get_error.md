# form_get_error()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1703–1713 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1703-L1713)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_get_error($element)
```

## Documentation

```text
Returns the error message filed against the given form element.

Form errors higher up in the form structure override deeper errors as well as
errors on the element itself.
```

## Code

```php
function form_get_error($element) {
  $form = form_set_error();
  $parents = array();
  foreach ($element['#parents'] as $parent) {
    $parents[] = $parent;
    $key = implode('][', $parents);
    if (isset($form[$key])) {
      return $form[$key];
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
