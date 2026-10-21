# system_theme_disable()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 318–341 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L318-L341)
- **Module/theme:** system

## Signature

```php
function system_theme_disable()
```

## Documentation

```text
Menu callback; Disables a theme.
```

## Code

```php
function system_theme_disable() {
  if (isset($_REQUEST['theme']) && isset($_REQUEST['token']) && drupal_valid_token($_REQUEST['token'], 'system-theme-operation-link')) {
    $theme = $_REQUEST['theme'];
    // Get current list of themes.
    $themes = list_themes();

    // Check if the specified theme is one recognized by the system.
    if (!empty($themes[$theme])) {
      if ($theme == variable_get('theme_default', 'bartik')) {
        // Don't disable the default theme.
        drupal_set_message(t('%theme is the default theme and cannot be disabled.', array('%theme' => $themes[$theme]->info['name'])), 'error');
      }
      else {
        theme_disable(array($theme));
        drupal_set_message(t('The %theme theme has been disabled.', array('%theme' => $themes[$theme]->info['name'])));
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
