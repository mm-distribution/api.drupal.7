# drupal_alter()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 1059–1174 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L1059-L1174)

## Signature

```php
function drupal_alter($type, &$data, &$context1 = NULL, &$context2 = NULL, &$context3 = NULL)
```

## Documentation

```text
Passes alterable variables to specific hook_TYPE_alter() implementations.

This dispatch function hands off the passed-in variables to type-specific
hook_TYPE_alter() implementations in modules. It ensures a consistent
interface for all altering operations.

A maximum of 2 alterable arguments is supported (a third is supported for
legacy reasons, but should not be used in new code). In case more arguments
need to be passed and alterable, modules provide additional variables
assigned by reference in the last $context argument:
@code
  $context = array(
    'alterable' => &$alterable,
    'unalterable' => $unalterable,
    'foo' => 'bar',
  );
  drupal_alter('mymodule_data', $alterable1, $alterable2, $context);
@endcode

Note that objects are always passed by reference in PHP5. If it is absolutely
required that no implementation alters a passed object in $context, then an
object needs to be cloned:
@code
  $context = array(
    'unalterable_object' => clone $object,
  );
  drupal_alter('mymodule_data', $data, $context);
@endcode

@param $type
  A string describing the type of the alterable $data. 'form', 'links',
  'node_content', and so on are several examples. Alternatively can be an
  array, in which case hook_TYPE_alter() is invoked for each value in the
  array, ordered first by module, and then for each module, in the order of
  values in $type. For example, when Form API is using drupal_alter() to
  execute both hook_form_alter() and hook_form_FORM_ID_alter()
  implementations, it passes array('form', 'form_' . $form_id) for $type.
@param $data
  The variable that will be passed to hook_TYPE_alter() implementations to be
  altered. The type of this variable depends on the value of the $type
  argument. For example, when altering a 'form', $data will be a structured
  array. When altering a 'profile', $data will be an object.
@param $context1
  (optional) An additional variable that is passed by reference.
@param $context2
  (optional) An additional variable that is passed by reference. If more
  context needs to be provided to implementations, then this should be an
  associative array as described above.
@param $context3
  (optional) An additional variable that is passed by reference. This
  parameter is deprecated and will not exist in Drupal 8; consequently, it
  should not be used for new Drupal 7 code either. It is here only for
  backwards compatibility with older code that passed additional arguments
  to drupal_alter().
```

## Code

```php
function drupal_alter($type, &$data, &$context1 = NULL, &$context2 = NULL, &$context3 = NULL) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['functions'] = &drupal_static(__FUNCTION__);
  }
  $functions = &$drupal_static_fast['functions'];

  // Most of the time, $type is passed as a string, so for performance,
  // normalize it to that. When passed as an array, usually the first item in
  // the array is a generic type, and additional items in the array are more
  // specific variants of it, as in the case of array('form', 'form_FORM_ID').
  if (is_array($type)) {
    $cid = implode(',', $type);
    $extra_types = $type;
    $type = array_shift($extra_types);
    // Allow if statements in this function to use the faster isset() rather
    // than !empty() both when $type is passed as a string, or as an array with
    // one item.
    if (empty($extra_types)) {
      unset($extra_types);
    }
  }
  else {
    $cid = $type;
  }

  // Some alter hooks are invoked many times per page request, so statically
  // cache the list of functions to call, and on subsequent calls, iterate
  // through them quickly.
  if (!isset($functions[$cid])) {
    $functions[$cid] = array();
    $hook = $type . '_alter';
    $modules = module_implements($hook);
    if (!isset($extra_types)) {
      // For the more common case of a single hook, we do not need to call
      // function_exists(), since module_implements() returns only modules with
      // implementations.
      foreach ($modules as $module) {
        $functions[$cid][] = $module . '_' . $hook;
      }
    }
    else {
      // For multiple hooks, we need $modules to contain every module that
      // implements at least one of them.
      $extra_modules = array();
      foreach ($extra_types as $extra_type) {
        $extra_modules = array_merge($extra_modules, module_implements($extra_type . '_alter'));
      }
      // If any modules implement one of the extra hooks that do not implement
      // the primary hook, we need to add them to the $modules array in their
      // appropriate order. module_implements() can only return ordered
      // implementations of a single hook. To get the ordered implementations
      // of multiple hooks, we mimic the module_implements() logic of first
      // ordering by module_list(), and then calling
      // drupal_alter('module_implements').
      if (array_diff($extra_modules, $modules)) {
        // Merge the arrays and order by module_list().
        $modules = array_intersect(module_list(), array_merge($modules, $extra_modules));
        // Since module_implements() already took care of loading the necessary
        // include files, we can safely pass FALSE for the array values.
        $implementations = array_fill_keys($modules, FALSE);
        // Let modules adjust the order solely based on the primary hook. This
        // ensures the same module order regardless of whether this if block
        // runs. Calling drupal_alter() recursively in this way does not result
        // in an infinite loop, because this call is for a single $type, so we
        // won't end up in this code block again.
        drupal_alter('module_implements', $implementations, $hook);
        $modules = array_keys($implementations);
      }
      foreach ($modules as $module) {
        // Since $modules is a merged array, for any given module, we do not
        // know whether it has any particular implementation, so we need a
        // function_exists().
        $function = $module . '_' . $hook;
        if (function_exists($function)) {
          $functions[$cid][] = $function;
        }
        foreach ($extra_types as $extra_type) {
          $function = $module . '_' . $extra_type . '_alter';
          if (function_exists($function)) {
            $functions[$cid][] = $function;
          }
        }
      }
    }
    // Allow the theme to alter variables after the theme system has been
    // initialized.
    global $theme, $base_theme_info;
    if (isset($theme)) {
      $theme_keys = array();
      foreach ($base_theme_info as $base) {
        $theme_keys[] = $base->name;
      }
      $theme_keys[] = $theme;
      foreach ($theme_keys as $theme_key) {
        $function = $theme_key . '_' . $hook;
        if (function_exists($function)) {
          $functions[$cid][] = $function;
        }
        if (isset($extra_types)) {
          foreach ($extra_types as $extra_type) {
            $function = $theme_key . '_' . $extra_type . '_alter';
            if (function_exists($function)) {
              $functions[$cid][] = $function;
            }
          }
        }
      }
    }
  }

  foreach ($functions[$cid] as $function) {
    $function($data, $context1, $context2, $context3);
  }
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
