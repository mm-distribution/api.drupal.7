# drupal_get_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 123–132 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L123-L132)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_get_form($form_id)
```

## Documentation

```text
Returns a renderable form array for a given form ID.

This function should be used instead of drupal_build_form() when $form_state
is not needed (i.e., when initially rendering the form) and is often
used as a menu callback.

@param $form_id
  The unique string identifying the desired form. If a function with that
  name exists, it is called to build the form array. Modules that need to
  generate the same form (or very similar forms) using different $form_ids
  can implement hook_forms(), which maps different $form_id values to the
  proper form constructor function. Examples may be found in node_forms(),
  and search_forms(). hook_forms() can also be used to define forms in
  classes.
@param ...
  Any additional arguments are passed on to the functions called by
  drupal_get_form(), including the unique form constructor function. For
  example, the node_edit form requires that a node object is passed in here
  when it is called. These are available to implementations of
  hook_form_alter() and hook_form_FORM_ID_alter() as the array
  $form_state['build_info']['args'].

@return
  The form array.

@see drupal_build_form()
```

## Code

```php
function drupal_get_form($form_id) {
  $form_state = array();

  $args = func_get_args();
  // Remove $form_id from the arguments.
  array_shift($args);
  $form_state['build_info']['args'] = $args;

  return drupal_build_form($form_id, $form_state);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
