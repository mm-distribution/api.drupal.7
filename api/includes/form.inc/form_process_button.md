# form_process_button()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3395–3405 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3395-L3405)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_button($element, &$form_state)
```

## Documentation

```text
Processes a form button element.

@param $element
  An associative array containing the properties and children of the
  form button.
@param $form_state
  The $form_state array for the form this element belongs to.

@return
  The processed element.
```

## Code

```php
function form_process_button($element, &$form_state) {
  // We normally want to add drupal.form-single-submit so that the double submit
  // protection can be added to the site, however, with the addition of
  // javascript_always_use_jquery, this would make most pages with a login
  // block or a search form have jquery always added, changing what people who
  // set the javascript_always_use_jquery variable to FALSE would have expected.
  if (variable_get('javascript_always_use_jquery', TRUE) && variable_get('javascript_use_double_submit_protection', TRUE)) {
    $element['#attached']['library'][] = array('system', 'drupal.form-single-submit');
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
