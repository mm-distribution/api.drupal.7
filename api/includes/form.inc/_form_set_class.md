# _form_set_class()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4418–4434 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4418-L4434)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_set_class(&$element, $class = array())
```

## Documentation

```text
Sets a form element's class attribute.

Adds 'required' and 'error' classes as needed.

@param $element
  The form element.
@param $name
  Array of new class names to be added.
```

## Code

```php
function _form_set_class(&$element, $class = array()) {
  if (!empty($class)) {
    if (!isset($element['#attributes']['class'])) {
      $element['#attributes']['class'] = array();
    }
    $element['#attributes']['class'] = array_merge($element['#attributes']['class'], $class);
  }
  // This function is invoked from form element theme functions, but the
  // rendered form element may not necessarily have been processed by
  // form_builder().
  if (!empty($element['#required'])) {
    $element['#attributes']['class'][] = 'required';
  }
  if (isset($element['#parents']) && form_get_error($element) !== NULL && !empty($element['#validated'])) {
    $element['#attributes']['class'][] = 'error';
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
