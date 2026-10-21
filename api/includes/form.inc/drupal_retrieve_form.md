# drupal_retrieve_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 766–848 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L766-L848)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_retrieve_form($form_id, &$form_state)
```

## Documentation

```text
Retrieves the structured array that defines a given form.

@param $form_id
  The unique string identifying the desired form. If a function
  with that name exists, it is called to build the form array.
  Modules that need to generate the same form (or very similar forms)
  using different $form_ids can implement hook_forms(), which maps
  different $form_id values to the proper form constructor function.
@param $form_state
  A keyed array containing the current state of the form, including the
  additional arguments to drupal_get_form() or drupal_form_submit() in the
  'args' component of the array.
```

## Code

```php
function drupal_retrieve_form($form_id, &$form_state) {
  $forms = &drupal_static(__FUNCTION__);

  // Record the $form_id.
  $form_state['build_info']['form_id'] = $form_id;

  // Record the filepath of the include file containing the original form, so
  // the form builder callbacks can be loaded when the form is being rebuilt
  // from cache on a different path (such as 'system/ajax'). See
  // form_get_cache(). Don't do this in maintenance mode as Drupal may not be
  // fully bootstrapped (i.e. during installation) in which case
  // menu_get_item() is not available.
  if (!isset($form_state['build_info']['files']['menu']) && !defined('MAINTENANCE_MODE')) {
    $item = menu_get_item();
    if (!empty($item['include_file'])) {
      // Do not use form_load_include() here, as the file is already loaded.
      // Anyway, form_get_cache() is able to handle filepaths too.
      $form_state['build_info']['files']['menu'] = $item['include_file'];
    }
  }

  // We save two copies of the incoming arguments: one for modules to use
  // when mapping form ids to constructor functions, and another to pass to
  // the constructor function itself.
  $args = $form_state['build_info']['args'];

  // We first check to see if there's a function named after the $form_id.
  // If there is, we simply pass the arguments on to it to get the form.
  if (!function_exists($form_id)) {
    // In cases where many form_ids need to share a central constructor function,
    // such as the node editing form, modules can implement hook_forms(). It
    // maps one or more form_ids to the correct constructor functions.
    //
    // We cache the results of that hook to save time, but that only works
    // for modules that know all their form_ids in advance. (A module that
    // adds a small 'rate this comment' form to each comment in a list
    // would need a unique form_id for each one, for example.)
    //
    // So, we call the hook if $forms isn't yet populated, OR if it doesn't
    // yet have an entry for the requested form_id.
    if (!isset($forms) || !isset($forms[$form_id])) {
      $forms = module_invoke_all('forms', $form_id, $args);
    }
    $form_definition = $forms[$form_id];
    if (isset($form_definition['callback arguments'])) {
      $args = array_merge($form_definition['callback arguments'], $args);
    }
    if (isset($form_definition['callback'])) {
      $callback = $form_definition['callback'];
      $form_state['build_info']['base_form_id'] = isset($form_definition['base_form_id']) ? $form_definition['base_form_id'] : $callback;
    }
    // In case $form_state['wrapper_callback'] is not defined already, we also
    // allow hook_forms() to define one.
    if (!isset($form_state['wrapper_callback']) && isset($form_definition['wrapper_callback'])) {
      $form_state['wrapper_callback'] = $form_definition['wrapper_callback'];
    }
  }

  $form = array();
  // We need to pass $form_state by reference in order for forms to modify it,
  // since call_user_func_array() requires that referenced variables are passed
  // explicitly.
  $args = array_merge(array($form, &$form_state), $args);

  // When the passed $form_state (not using drupal_get_form()) defines a
  // 'wrapper_callback', then it requests to invoke a separate (wrapping) form
  // builder function to pre-populate the $form array with form elements, which
  // the actual form builder function ($callback) expects. This allows for
  // pre-populating a form with common elements for certain forms, such as
  // back/next/save buttons in multi-step form wizards. See drupal_build_form().
  if (isset($form_state['wrapper_callback']) && is_callable($form_state['wrapper_callback'])) {
    $form = call_user_func_array($form_state['wrapper_callback'], $args);
    // Put the prepopulated $form into $args.
    $args[0] = $form;
  }

  // If $callback was returned by a hook_forms() implementation, call it.
  // Otherwise, call the function named after the form id.
  $form = call_user_func_array(isset($callback) ? $callback : $form_id, $args);
  $form['#form_id'] = $form_id;

  return $form;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
