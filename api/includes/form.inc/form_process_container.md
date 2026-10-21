# form_process_container()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3419–3425 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3419-L3425)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_container($element, &$form_state)
```

## Documentation

```text
Processes a container element.

@param $element
  An associative array containing the properties and children of the
  container.
@param $form_state
  The $form_state array for the form this element belongs to.

@return
  The processed element.
```

## Code

```php
function form_process_container($element, &$form_state) {
  // Generate the ID of the element if it's not explicitly given.
  if (!isset($element['#id'])) {
    $element['#id'] = drupal_html_id(implode('-', $element['#parents']) . '-wrapper');
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
