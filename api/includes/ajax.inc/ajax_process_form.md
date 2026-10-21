# ajax_process_form()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 644–650 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L644-L650)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_process_form($element, &$form_state)
```

## Documentation

```text
Form element processing handler for the #ajax form property.

@param $element
  An associative array containing the properties of the element.

@return
  The processed element.

@see ajax_pre_render_element()
```

## Code

```php
function ajax_process_form($element, &$form_state) {
  $element = ajax_pre_render_element($element);
  if (!empty($element['#ajax_processed'])) {
    $form_state['cache'] = TRUE;
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
