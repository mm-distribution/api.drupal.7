# hook_forms()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1829–1861 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1829-L1861)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_forms($form_id, $args)
```

## Documentation

```text
Map form_ids to form builder functions.

By default, when drupal_get_form() is called, the system will look for a
function with the same name as the form ID, and use that function to build
the form. If no such function is found, Drupal calls this hook. Modules
implementing this hook can then provide their own instructions for mapping
form IDs to constructor functions. As a result, you can easily map multiple
form IDs to a single form constructor (referred to as a 'base' form).

Using a base form can help to avoid code duplication, by allowing many
similar forms to use the same code base. Another benefit is that it becomes
much easier for other modules to apply a general change to the group of
forms; hook_form_BASE_FORM_ID_alter() can be used to easily alter multiple
forms at once by directly targeting the shared base form.

Two example use cases where base forms may be useful are given below.

First, you can use this hook to tell the form system to use a different
function to build certain forms in your module; this is often used to define
a form "factory" function that is used to build several similar forms. In
this case, your hook implementation will likely ignore all of the input
arguments. See node_forms() for an example of this. Note, node_forms() is the
hook_forms() implementation; the base form itself is defined in node_form().

Second, you could use this hook to define how to build a form with a
dynamically-generated form ID. In this case, you would need to verify that
the $form_id input matched your module's format for dynamically-generated
form IDs, and if so, act appropriately.

Third, forms defined in classes can be defined this way.

@param $form_id
  The unique string identifying the desired form.
@param $args
  An array containing the original arguments provided to drupal_get_form()
  or drupal_form_submit(). These are always passed to the form builder and
  do not have to be specified manually in 'callback arguments'.

@return
  An associative array whose keys define form_ids and whose values are an
  associative array defining the following keys:
  - callback: The callable returning the form array. If it is the name of
    the form builder function then this will be used for the base
    form ID, for example, to target a base form using
    hook_form_BASE_FORM_ID_alter(). Otherwise use the base_form_id key to
    define the base form ID.
  - callback arguments: (optional) Additional arguments to pass to the
    function defined in 'callback', which are prepended to $args.
  - base_form_id: The base form ID can be specified explicitly. This is
    required when callback is not the name of a function.
  - wrapper_callback: (optional) Any callable to invoke before the form
    builder defined in 'callback' is invoked. This wrapper callback may
    prepopulate the $form array with form elements, which will then be
    already contained in the $form that is passed on to the form builder
    defined in 'callback'. For example, a wrapper callback could setup
    wizard-like form buttons that are the same for a variety of forms that
    belong to the wizard, which all share the same wrapper callback.
```

## Code

```php
function hook_forms($form_id, $args) {
  // Simply reroute the (non-existing) $form_id 'mymodule_first_form' to
  // 'mymodule_main_form'.
  $forms['mymodule_first_form'] = array(
    'callback' => 'mymodule_main_form',
  );

  // Reroute the $form_id and prepend an additional argument that gets passed to
  // the 'mymodule_main_form' form builder function.
  $forms['mymodule_second_form'] = array(
    'callback' => 'mymodule_main_form',
    'callback arguments' => array('some parameter'),
  );

  // Reroute the $form_id, but invoke the form builder function
  // 'mymodule_main_form_wrapper' first, so we can prepopulate the $form array
  // that is passed to the actual form builder 'mymodule_main_form'.
  $forms['mymodule_wrapped_form'] = array(
    'callback' => 'mymodule_main_form',
    'wrapper_callback' => 'mymodule_main_form_wrapper',
  );

  // Build a form with a static class callback.
  $forms['mymodule_class_generated_form'] = array(
    // This will call: MyClass::generateMainForm().
    'callback' => array('MyClass', 'generateMainForm'),
    // The base_form_id is required when the callback is a static function in
    // a class. This can also be used to keep newer code backwards compatible.
    'base_form_id' => 'mymodule_main_form',
  );

  return $forms;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_forms()".

- [comment_forms()](../../comment/comment.module/comment_forms.md) — `modules/comment/comment.module`
- [dashboard_forms()](../../dashboard/dashboard.module/dashboard_forms.md) — `modules/dashboard/dashboard.module`
- [node_forms()](../../node/node.module/node_forms.md) — `modules/node/node.module`
- [search_forms()](../../search/search.module/search_forms.md) — `modules/search/search.module`
- [trigger_forms()](../../trigger/trigger.module/trigger_forms.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
