# system_theme_default()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 346–387 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L346-L387)
- **Module/theme:** system

## Signature

```php
function system_theme_default()
```

## Documentation

```text
Menu callback; Set the default theme.
```

## Code

```php
function system_theme_default() {
  if (isset($_REQUEST['theme']) && isset($_REQUEST['token']) && drupal_valid_token($_REQUEST['token'], 'system-theme-operation-link')) {
    $theme = $_REQUEST['theme'];
    // Get current list of themes.
    $themes = list_themes();

    // Check if the specified theme is one recognized by the system.
    if (!empty($themes[$theme])) {
      // Enable the theme if it is currently disabled.
      if (empty($themes[$theme]->status)) {
       theme_enable(array($theme));
      }
      // Set the default theme.
      variable_set('theme_default', $theme);

      // Rebuild the menu. This duplicates the menu_rebuild() in theme_enable().
      // However, modules must know the current default theme in order to use
      // this information in hook_menu() or hook_menu_alter() implementations,
      // and doing the variable_set() before the theme_enable() could result
      // in a race condition where the theme is default but not enabled.
      menu_rebuild();

      // The status message depends on whether an admin theme is currently in use:
      // a value of 0 means the admin theme is set to be the default theme.
      $admin_theme = variable_get('admin_theme', 0);
      if ($admin_theme != 0 && $admin_theme != $theme) {
        drupal_set_message(t('Please note that the administration theme is still set to the %admin_theme theme; consequently, the theme on this page remains unchanged. All non-administrative sections of the site, however, will show the selected %selected_theme theme by default.', array(
          '%admin_theme' => $themes[$admin_theme]->info['name'],
          '%selected_theme' => $themes[$theme]->info['name'],
        )));
      }
      else {
        drupal_set_message(t('%theme is now the default theme.', array('%theme' => $themes[$theme]->info['name'])));
      }
    }
    else {
      drupal_set_message(t('The %theme theme was not found.', array('%theme' => $theme)), 'error');
    }
    drupal_goto('admin/appearance');
  }
  return MENU_ACCESS_DENIED;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
