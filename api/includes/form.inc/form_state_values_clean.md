# form_state_values_clean()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2264–2299 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2264-L2299)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_state_values_clean(&$form_state)
```

## Documentation

```text
Removes internal Form API elements and buttons from submitted form values.

This function can be used when a module wants to store all submitted form
values, for example, by serializing them into a single database column. In
such cases, all internal Form API values and all form button elements should
not be contained, and this function allows to remove them before the module
proceeds to storage. Next to button elements, the following internal values
are removed:
- form_id
- form_token
- form_build_id
- op

@param $form_state
  A keyed array containing the current state of the form, including
  submitted form values; altered by reference.
```

## Code

```php
function form_state_values_clean(&$form_state) {
  // Remove internal Form API values.
  unset($form_state['values']['form_id'], $form_state['values']['form_token'], $form_state['values']['form_build_id'], $form_state['values']['op']);

  // Remove button values.
  // form_builder() collects all button elements in a form. We remove the button
  // value separately for each button element.
  foreach ($form_state['buttons'] as $button) {
    // Remove this button's value from the submitted form values by finding
    // the value corresponding to this button.
    // We iterate over the #parents of this button and move a reference to
    // each parent in $form_state['values']. For example, if #parents is:
    //   array('foo', 'bar', 'baz')
    // then the corresponding $form_state['values'] part will look like this:
    // array(
    //   'foo' => array(
    //     'bar' => array(
    //       'baz' => 'button_value',
    //     ),
    //   ),
    // )
    // We start by (re)moving 'baz' to $last_parent, so we are able unset it
    // at the end of the iteration. Initially, $values will contain a
    // reference to $form_state['values'], but in the iteration we move the
    // reference to $form_state['values']['foo'], and finally to
    // $form_state['values']['foo']['bar'], which is the level where we can
    // unset 'baz' (that is stored in $last_parent).
    $parents = $button['#parents'];
    $last_parent = array_pop($parents);
    $key_exists = NULL;
    $values = &drupal_array_get_nested_value($form_state['values'], $parents, $key_exists);
    if ($key_exists && is_array($values)) {
      unset($values[$last_parent]);
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
