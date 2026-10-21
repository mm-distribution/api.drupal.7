# theme_get_suggestions()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2796–2841 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2796-L2841)

## Signature

```php
function theme_get_suggestions($args, $base, $delimiter = '__')
```

## Documentation

```text
Generate an array of suggestions from path arguments.

This is typically called for adding to the 'theme_hook_suggestions' or
'classes_array' variables from within preprocess functions, when wanting to
base the additional suggestions on the path of the current page.

@param $args
  An array of path arguments, such as from function arg().
@param $base
  A string identifying the base 'thing' from which more specific suggestions
  are derived. For example, 'page' or 'html'.
@param $delimiter
  The string used to delimit increasingly specific information. The default
  of '__' is appropriate for theme hook suggestions. '-' is appropriate for
  extra classes.

@return
  An array of suggestions, suitable for adding to
  $variables['theme_hook_suggestions'] within a preprocess function or to
  $variables['classes_array'] if the suggestions represent extra CSS classes.
```

## Code

```php
function theme_get_suggestions($args, $base, $delimiter = '__') {

  // Build a list of suggested theme hooks or body classes in order of
  // specificity. One suggestion is made for every element of the current path,
  // though numeric elements are not carried to subsequent suggestions. For
  // example, for $base='page', http://www.example.com/node/1/edit would result
  // in the following suggestions and body classes:
  //
  // page__node              page-node
  // page__node__%           page-node-%
  // page__node__1           page-node-1
  // page__node__edit        page-node-edit

  $suggestions = array();
  $prefix = $base;
  foreach ($args as $arg) {
    // Remove slashes or null per SA-CORE-2009-003 and change - (hyphen) to _
    // (underscore).
    //
    // When we discover templates in @see drupal_find_theme_templates,
    // hyphens (-) are converted to underscores (_) before the theme hook
    // is registered. We do this because the hyphens used for delimiters
    // in hook suggestions cannot be used in the function names of the
    // associated preprocess functions. Any page templates designed to be used
    // on paths that contain a hyphen are also registered with these hyphens
    // converted to underscores so here we must convert any hyphens in path
    // arguments to underscores here before fetching theme hook suggestions
    // to ensure the templates are appropriately recognized.
    $arg = str_replace(array("/", "\\", "\0", '-'), array('', '', '', '_'), $arg);
    // The percent acts as a wildcard for numeric arguments since
    // asterisks are not valid filename characters on many filesystems.
    if (is_numeric($arg)) {
      $suggestions[] = $prefix . $delimiter . '%';
    }
    $suggestions[] = $prefix . $delimiter . $arg;
    if (!is_numeric($arg)) {
      $prefix .= $delimiter . $arg;
    }
  }
  if (drupal_is_front_page()) {
    // Front templates should be based on root only, not prefixed arguments.
    $suggestions[] = $base . $delimiter . 'front';
  }

  return $suggestions;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
