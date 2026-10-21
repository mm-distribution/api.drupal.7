# system_theme_enable()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 296–313 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L296-L313)
- **Module/theme:** system

## Signature

```php
function system_theme_enable()
```

## Documentation

```text
Menu callback; Enables a theme.
```

## Code

```php
function system_theme_enable() {
  if (isset($_REQUEST['theme']) && isset($_REQUEST['token']) && drupal_valid_token($_REQUEST['token'], 'system-theme-operation-link')) {
    $theme = $_REQUEST['theme'];
    // Get current list of themes.
    $themes = list_themes();

    // Check if the specified theme is one recognized by the system.
    if (!empty($themes[$theme])) {
      theme_enable(array($theme));
      drupal_set_message(t('The %theme theme has been enabled.', array('%theme' => $themes[$theme]->info['name'])));
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
