# form_set_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2671–2673 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2671-L2673)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_set_value($element, $value, &$form_state)
```

## Documentation

```text
Changes submitted form values during form validation.

Use this function to change the submitted value of a form element in a form
validation function, so that the changed value persists in $form_state
through the remaining validation and submission handlers. It does not change
the value in $element['#value'], only in $form_state['values'], which is
where submitted values are always stored.

Note that form validation functions are specified in the '#validate'
component of the form array (the value of $form['#validate'] is an array of
validation function names). If the form does not originate in your module,
you can implement hook_form_FORM_ID_alter() to add a validation function
to $form['#validate'].

@param $element
  The form element that should have its value updated; in most cases you can
  just pass in the element from the $form array, although the only component
  that is actually used is '#parents'. If constructing yourself, set
  $element['#parents'] to be an array giving the path through the form
  array's keys to the element whose value you want to update. For instance,
  if you want to update the value of $form['elem1']['elem2'], which should be
  stored in $form_state['values']['elem1']['elem2'], you would set
  $element['#parents'] = array('elem1','elem2').
@param $value
  The new value for the form element.
@param $form_state
  Form state array where the value change should be recorded.
```

## Code

```php
function form_set_value($element, $value, &$form_state) {
  drupal_array_set_nested_value($form_state['values'], $element['#parents'], $value, TRUE);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
