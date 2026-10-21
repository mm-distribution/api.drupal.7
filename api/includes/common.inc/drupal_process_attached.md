# drupal_process_attached()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4750–4813 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4750-L4813)

## Signature

```php
function drupal_process_attached($elements, $group = JS_DEFAULT, $dependency_check = FALSE, $every_page = NULL)
```

## Documentation

```text
Adds attachments to a render() structure.

Libraries, JavaScript, CSS and other types of custom structures are attached
to elements using the #attached property. The #attached property is an
associative array, where the keys are the attachment types and the values are
the attached data. For example:
@code
$build['#attached'] = array(
  'js' => array(drupal_get_path('module', 'taxonomy') . '/taxonomy.js'),
  'css' => array(drupal_get_path('module', 'taxonomy') . '/taxonomy.css'),
);
@endcode

'js', 'css', and 'library' are types that get special handling. For any
other kind of attached data, the array key must be the full name of the
callback function and each value an array of arguments. For example:
@code
$build['#attached']['drupal_add_http_header'] = array(
  array('Content-Type', 'application/rss+xml; charset=utf-8'),
);
@endcode

External 'js' and 'css' files can also be loaded. For example:
@code
$build['#attached']['js'] = array(
  'http://code.jquery.com/jquery-1.4.2.min.js' => array(
    'type' => 'external',
  ),
);
@endcode

@param $elements
  The structured array describing the data being rendered.
@param $group
  The default group of JavaScript and CSS being added. This is only applied
  to the stylesheets and JavaScript items that don't have an explicit group
  assigned to them.
@param $dependency_check
  When TRUE, will exit if a given library's dependencies are missing. When
  set to FALSE, will continue to add the libraries, even though one or more
  dependencies are missing. Defaults to FALSE.
@param $every_page
  Set to TRUE to indicate that the attachments are added to every page on the
  site. Only attachments with the every_page flag set to TRUE can participate
  in JavaScript/CSS aggregation.

@return
  FALSE if there were any missing library dependencies; TRUE if all library
  dependencies were met.

@see drupal_add_library()
@see drupal_add_js()
@see drupal_add_css()
@see drupal_render()
```

## Code

```php
function drupal_process_attached($elements, $group = JS_DEFAULT, $dependency_check = FALSE, $every_page = NULL) {
  // Add defaults to the special attached structures that should be processed differently.
  $elements['#attached'] += array(
    'library' => array(),
    'js' => array(),
    'css' => array(),
  );

  // Add the libraries first.
  $success = TRUE;
  foreach ($elements['#attached']['library'] as $library) {
    if (drupal_add_library($library[0], $library[1], $every_page) === FALSE) {
      $success = FALSE;
      // Exit if the dependency is missing.
      if ($dependency_check) {
        return $success;
      }
    }
  }
  unset($elements['#attached']['library']);

  // Add both the JavaScript and the CSS.
  // The parameters for drupal_add_js() and drupal_add_css() require special
  // handling.
  foreach (array('js', 'css') as $type) {
    foreach ($elements['#attached'][$type] as $data => $options) {
      // If the value is not an array, it's a filename and passed as first
      // (and only) argument.
      if (!is_array($options)) {
        $data = $options;
        $options = NULL;
      }
      // In some cases, the first parameter ($data) is an array. Arrays can't be
      // passed as keys in PHP, so we have to get $data from the value array.
      if (is_numeric($data)) {
        $data = $options['data'];
        unset($options['data']);
      }
      // Apply the default group if it isn't explicitly given.
      if (!isset($options['group'])) {
        $options['group'] = $group;
      }
      // Set the every_page flag if one was passed.
      if (isset($every_page)) {
        $options['every_page'] = $every_page;
      }
      call_user_func('drupal_add_' . $type, $data, $options);
    }
    unset($elements['#attached'][$type]);
  }

  // Add additional types of attachments specified in the render() structure.
  // Libraries, JavaScript and CSS have been added already, as they require
  // special handling.
  foreach ($elements['#attached'] as $callback => $options) {
    if (function_exists($callback)) {
      foreach ($elements['#attached'][$callback] as $args) {
        call_user_func_array($callback, $args);
      }
    }
  }

  return $success;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
