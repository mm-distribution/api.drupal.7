# theme_disable()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1629–1654 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1629-L1654)

## Signature

```php
function theme_disable($theme_list)
```

## Documentation

```text
Disables a given list of themes.

@param $theme_list
  An array of theme names.
```

## Code

```php
function theme_disable($theme_list) {
  // Don't disable the default theme.
  if ($pos = array_search(variable_get('theme_default', 'bartik'), $theme_list) !== FALSE) {
    unset($theme_list[$pos]);
    if (empty($theme_list)) {
      return;
    }
  }

  drupal_clear_css_cache();

  foreach ($theme_list as $key) {
    db_update('system')
      ->fields(array('status' => 0))
      ->condition('type', 'theme')
      ->condition('name', $key)
      ->execute();
  }

  list_themes(TRUE);
  menu_rebuild();
  drupal_theme_rebuild();

  // Invoke hook_themes_disabled after the themes have been disabled.
  module_invoke_all('themes_disabled', $theme_list);
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
