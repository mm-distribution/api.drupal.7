# system_themes_page()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 136–250 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L136-L250)
- **Module/theme:** system

## Signature

```php
function system_themes_page()
```

## Documentation

```text
Menu callback; displays a listing of all themes.
```

## Code

```php
function system_themes_page() {
  // Get current list of themes.
  $themes = system_rebuild_theme_data();
  uasort($themes, 'system_sort_modules_by_info_name');

  $theme_default = variable_get('theme_default', 'bartik');
  $theme_groups  = array();

  foreach ($themes as &$theme) {
    if (!empty($theme->info['hidden'])) {
      continue;
    }
    $admin_theme_options[$theme->name] = $theme->info['name'];
    $theme->is_default = ($theme->name == $theme_default);

    // Identify theme screenshot.
    $theme->screenshot = NULL;
    // Create a list which includes the current theme and all its base themes.
    if (isset($themes[$theme->name]->base_themes)) {
      $theme_keys = array_keys($themes[$theme->name]->base_themes);
      $theme_keys[] = $theme->name;
    }
    else {
      $theme_keys = array($theme->name);
    }
    // Look for a screenshot in the current theme or in its closest ancestor.
    foreach (array_reverse($theme_keys) as $theme_key) {
      if (isset($themes[$theme_key]) && file_exists($themes[$theme_key]->info['screenshot'])) {
        $theme->screenshot = array(
          'path' => $themes[$theme_key]->info['screenshot'],
          'alt' => t('Screenshot for !theme theme', array('!theme' => $theme->info['name'])),
          'title' => t('Screenshot for !theme theme', array('!theme' => $theme->info['name'])),
          'attributes' => array('class' => array('screenshot')),
        );
        break;
      }
    }

    if (empty($theme->status)) {
     // Ensure this theme is compatible with this version of core.
     // Require the 'content' region to make sure the main page
     // content has a common place in all themes.
      $theme->incompatible_core = !isset($theme->info['core']) || ($theme->info['core'] != DRUPAL_CORE_COMPATIBILITY) || (!isset($theme->info['regions']['content']));
      $theme->incompatible_php = version_compare(phpversion(), $theme->info['php']) < 0;
    }
    $query['token'] = drupal_get_token('system-theme-operation-link');
    $theme->operations = array();
    if (!empty($theme->status) || !$theme->incompatible_core && !$theme->incompatible_php) {
      // Create the operations links.
      $query['theme'] = $theme->name;
      if (drupal_theme_access($theme)) {
        $theme->operations[] = array(
          'title' => t('Settings'),
          'href' => 'admin/appearance/settings/' . $theme->name,
          'attributes' => array('title' => t('Settings for !theme theme', array('!theme' => $theme->info['name']))),
        );
      }
      if (!empty($theme->status)) {
        if (!$theme->is_default) {
          $theme->operations[] = array(
            'title' => t('Disable'),
            'href' => 'admin/appearance/disable',
            'query' => $query,
            'attributes' => array('title' => t('Disable !theme theme', array('!theme' => $theme->info['name']))),
          );
          $theme->operations[] = array(
            'title' => t('Set default'),
            'href' => 'admin/appearance/default',
            'query' => $query,
            'attributes' => array('title' => t('Set !theme as default theme', array('!theme' => $theme->info['name']))),
          );
        }
      }
      else {
        $theme->operations[] = array(
          'title' => t('Enable'),
          'href' => 'admin/appearance/enable',
          'query' => $query,
          'attributes' => array('title' => t('Enable !theme theme', array('!theme' => $theme->info['name']))),
        );
        $theme->operations[] = array(
          'title' => t('Enable and set default'),
          'href' => 'admin/appearance/default',
          'query' => $query,
          'attributes' => array('title' => t('Enable !theme as default theme', array('!theme' => $theme->info['name']))),
        );
      }
    }

    // Add notes to default and administration theme.
    $theme->notes = array();
    $theme->classes = array();
    if ($theme->is_default) {
      $theme->classes[] = 'theme-default';
      $theme->notes[] = t('default theme');
    }

    // Sort enabled and disabled themes into their own groups.
    $theme_groups[$theme->status ? 'enabled' : 'disabled'][] = $theme;
  }

  // There are two possible theme groups.
  $theme_group_titles = array(
    'enabled' => format_plural(count($theme_groups['enabled']), 'Enabled theme', 'Enabled themes'),
  );
  if (!empty($theme_groups['disabled'])) {
    $theme_group_titles['disabled'] = format_plural(count($theme_groups['disabled']), 'Disabled theme', 'Disabled themes');
  }

  uasort($theme_groups['enabled'], 'system_sort_themes');
  drupal_alter('system_themes_page', $theme_groups);

  $admin_form = drupal_get_form('system_themes_admin_form', $admin_theme_options);
  return theme('system_themes_page', array('theme_groups' => $theme_groups, 'theme_group_titles' => $theme_group_titles)) . drupal_render($admin_form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
