# theme_enable()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 1604–1621 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L1604-L1621)

## Signature

```php
function theme_enable($theme_list)
```

## Documentation

```text
Enables a given list of themes.

@param $theme_list
  An array of theme names.
```

## Code

```php
function theme_enable($theme_list) {
  drupal_clear_css_cache();

  foreach ($theme_list as $key) {
    db_update('system')
      ->fields(array('status' => 1))
      ->condition('type', 'theme')
      ->condition('name', $key)
      ->execute();
  }

  list_themes(TRUE);
  menu_rebuild();
  drupal_theme_rebuild();

  // Invoke hook_themes_enabled() after the themes have been enabled.
  module_invoke_all('themes_enabled', $theme_list);
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
