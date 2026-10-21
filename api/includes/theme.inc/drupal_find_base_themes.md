# drupal_find_base_themes()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 843–867 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L843-L867)

## Signature

```php
function drupal_find_base_themes($themes, $key, $used_keys = array())
```

## Documentation

```text
Find all the base themes for the specified theme.

Themes can inherit templates and function implementations from earlier themes.

@param $themes
  An array of available themes.
@param $key
  The name of the theme whose base we are looking for.
@param $used_keys
  A recursion parameter preventing endless loops.
@return
  Returns an array of all of the theme's ancestors; the first element's value
  will be NULL if an error occurred.
```

## Code

```php
function drupal_find_base_themes($themes, $key, $used_keys = array()) {
  $base_key = $themes[$key]->info['base theme'];
  // Does the base theme exist?
  if (!isset($themes[$base_key])) {
    return array($base_key => NULL);
  }

  $current_base_theme = array($base_key => $themes[$base_key]->info['name']);

  // Is the base theme itself a child of another theme?
  if (isset($themes[$base_key]->info['base theme'])) {
    // Do we already know the base themes of this theme?
    if (isset($themes[$base_key]->base_themes)) {
      return $themes[$base_key]->base_themes + $current_base_theme;
    }
    // Prevent loops.
    if (!empty($used_keys[$base_key])) {
      return array($base_key => NULL);
    }
    $used_keys[$base_key] = TRUE;
    return drupal_find_base_themes($themes, $base_key, $used_keys) + $current_base_theme;
  }
  // If we get here, then this is our parent theme.
  return $current_base_theme;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
