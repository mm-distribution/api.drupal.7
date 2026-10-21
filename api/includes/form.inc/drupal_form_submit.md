# drupal_form_submit()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 723–750 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L723-L750)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_form_submit($form_id, &$form_state)
```

## Documentation

```text
Retrieves, populates, and processes a form.

This function allows you to supply values for form elements and submit a
form for processing. Compare to drupal_get_form(), which also builds and
processes a form, but does not allow you to supply values.

There is no return value, but you can check to see if there are errors
by calling form_get_errors().

@param $form_id
  The unique string identifying the desired form. If a function
  with that name exists, it is called to build the form array.
  Modules that need to generate the same form (or very similar forms)
  using different $form_ids can implement hook_forms(), which maps
  different $form_id values to the proper form constructor function. Examples
  may be found in node_forms() and search_forms().
@param $form_state
  A keyed array containing the current state of the form. Most important is
  the $form_state['values'] collection, a tree of data used to simulate the
  incoming $_POST information from a user's form submission. If a key is not
  filled in $form_state['values'], then the default value of the respective
  element is used. To submit an unchecked checkbox or other control that
  browsers submit by not having a $_POST entry, include the key, but set the
  value to NULL.
@param ...
  Any additional arguments are passed on to the functions called by
  drupal_form_submit(), including the unique form constructor function.
  For example, the node_edit form requires that a node object be passed
  in here when it is called. Arguments that need to be passed by reference
  should not be included here, but rather placed directly in the $form_state
  build info array so that the reference can be preserved. For example, a
  form builder function with the following signature:
  @code
  function mymodule_form($form, &$form_state, &$object) {
  }
  @endcode
  would be called via drupal_form_submit() as follows:
  @code
  $form_state['values'] = $my_form_values;
  $form_state['build_info']['args'] = array(&$object);
  drupal_form_submit('mymodule_form', $form_state);
  @endcode
For example:
@code
// register a new user
$form_state = array();
$form_state['values']['name'] = 'robo-user';
$form_state['values']['mail'] = 'robouser@example.com';
$form_state['values']['pass']['pass1'] = 'password';
$form_state['values']['pass']['pass2'] = 'password';
$form_state['values']['op'] = t('Create new account');
drupal_form_submit('user_register_form', $form_state);
@endcode
```

## Code

```php
function drupal_form_submit($form_id, &$form_state) {
  if (!isset($form_state['build_info']['args'])) {
    $args = func_get_args();
    array_shift($args);
    array_shift($args);
    $form_state['build_info']['args'] = $args;
  }
  // Merge in default values.
  $form_state += form_state_defaults();

  // Populate $form_state['input'] with the submitted values before retrieving
  // the form, to be consistent with what drupal_build_form() does for
  // non-programmatic submissions (form builder functions may expect it to be
  // there).
  $form_state['input'] = $form_state['values'];

  $form_state['programmed'] = TRUE;
  $form = drupal_retrieve_form($form_id, $form_state);
  // Programmed forms are always submitted.
  $form_state['submitted'] = TRUE;

  // Reset form validation.
  $form_state['must_validate'] = TRUE;
  form_clear_error();

  drupal_prepare_form($form_id, $form, $form_state);
  drupal_process_form($form_id, $form, $form_state);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
