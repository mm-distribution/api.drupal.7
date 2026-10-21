# form_process_actions()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3378–3381 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3378-L3381)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_actions($element, &$form_state)
```

## Documentation

```text
Processes a form actions container element.

@param $element
  An associative array containing the properties and children of the
  form actions container.
@param $form_state
  The $form_state array for the form this element belongs to.

@return
  The processed element.
```

## Code

```php
function form_process_actions($element, &$form_state) {
  $element['#attributes']['class'][] = 'form-actions';
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
