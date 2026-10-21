# drupal_add_library()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4972–4993 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4972-L4993)

## Signature

```php
function drupal_add_library($module, $name, $every_page = NULL)
```

## Documentation

```text
Adds multiple JavaScript or CSS files at the same time.

A library defines a set of JavaScript and/or CSS files, optionally using
settings, and optionally requiring another library. For example, a library
can be a jQuery plugin, a JavaScript framework, or a CSS framework. This
function allows modules to load a library defined/shipped by itself or a
depending module, without having to add all files of the library separately.
Each library is only loaded once.

@param $module
  The name of the module that registered the library.
@param $name
  The name of the library to add.
@param $every_page
  Set to TRUE if this library is added to every page on the site. Only items
  with the every_page flag set to TRUE can participate in aggregation.

@return
  TRUE if the library was successfully added; FALSE if the library or one of
  its dependencies could not be added.

@see drupal_get_library()
@see hook_library()
@see hook_library_alter()
```

## Code

```php
function drupal_add_library($module, $name, $every_page = NULL) {
  $added = &drupal_static(__FUNCTION__, array());

  // Only process the library if it exists and it was not added already.
  if (!isset($added[$module][$name])) {
    if ($library = drupal_get_library($module, $name)) {
      // Add all components within the library.
      $elements['#attached'] = array(
        'library' => $library['dependencies'],
        'js' => $library['js'],
        'css' => $library['css'],
      );
      $added[$module][$name] = drupal_process_attached($elements, JS_LIBRARY, TRUE, $every_page);
    }
    else {
      // Requested library does not exist.
      $added[$module][$name] = FALSE;
    }
  }

  return $added[$module][$name];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
