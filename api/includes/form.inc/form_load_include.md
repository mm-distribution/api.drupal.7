# form_load_include()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 650–666 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L650-L666)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_load_include(&$form_state, $type, $module, $name = NULL)
```

## Documentation

```text
Ensures an include file is loaded whenever the form is processed.

Example:
@code
  // Load node.admin.inc from Node module.
  form_load_include($form_state, 'inc', 'node', 'node.admin');
@endcode

Use this function instead of module_load_include() from inside a form
constructor or any form processing logic as it ensures that the include file
is loaded whenever the form is processed. In contrast to using
module_load_include() directly, form_load_include() makes sure the include
file is correctly loaded also if the form is cached.

@param $form_state
  The current state of the form.
@param $type
  The include file's type (file extension).
@param $module
  The module to which the include file belongs.
@param $name
  (optional) The base file name (without the $type extension). If omitted,
  $module is used; i.e., resulting in "$module.$type" by default.

@return
  The filepath of the loaded include file, or FALSE if the include file was
  not found or has been loaded already.

@see module_load_include()
```

## Code

```php
function form_load_include(&$form_state, $type, $module, $name = NULL) {
  if (!isset($name)) {
    $name = $module;
  }
  if (!isset($form_state['build_info']['files']["$module:$name.$type"])) {
    // Only add successfully included files to the form state.
    if ($result = module_load_include($type, $module, $name)) {
      $form_state['build_info']['files']["$module:$name.$type"] = array(
        'type' => $type,
        'module' => $module,
        'name' => $name,
      );
      return $result;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
