# template_preprocess()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2475–2507 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2475-L2507)

## Signature

```php
function template_preprocess(&$variables, $hook)
```

## Documentation

```text
Adds a default set of helper variables for variable processors and templates.

This function is called for theme hooks implemented as templates only, not
for theme hooks implemented as functions. This preprocess function is the
first in the sequence of preprocessing and processing functions that is
called when preparing variables for a template. See theme() for more details
about the full sequence.

@see theme()
@see template_process()
```

## Code

```php
function template_preprocess(&$variables, $hook) {
  global $user;
  static $count = array();

  // Track run count for each hook to provide zebra striping. See
  // "template_preprocess_block()" which provides the same feature specific to
  // blocks.
  $count[$hook] = isset($count[$hook]) && is_int($count[$hook]) ? $count[$hook] : 1;
  $variables['zebra'] = ($count[$hook] % 2) ? 'odd' : 'even';
  $variables['id'] = $count[$hook]++;

  // Tell all templates where they are located.
  $variables['directory'] = path_to_theme();

  // Initialize html class attribute for the current hook.
  $variables['classes_array'] = array(drupal_html_class($hook));

  // Merge in variables that don't depend on hook and don't change during a
  // single page request.
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['default_variables'] = &drupal_static(__FUNCTION__);
  }
  $default_variables = &$drupal_static_fast['default_variables'];
  // Global $user object shouldn't change during a page request once rendering
  // has started, but if there's an edge case where it does, re-fetch the
  // variables appropriate for the new user.
  if (!isset($default_variables) || ($user !== $default_variables['user'])) {
    $default_variables = _template_preprocess_default_variables();
  }
  $variables += $default_variables;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
