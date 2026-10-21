# drupal_theme_initialize()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 70–113 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L70-L113)

## Signature

```php
function drupal_theme_initialize()
```

## Documentation

```text
Initializes the theme system by loading the theme.
```

## Code

```php
function drupal_theme_initialize() {
  global $theme, $user, $theme_key;

  // If $theme is already set, assume the others are set, too, and do nothing
  if (isset($theme)) {
    return;
  }

  drupal_bootstrap(DRUPAL_BOOTSTRAP_DATABASE);
  $themes = list_themes();

  // Only select the user selected theme if it is available in the
  // list of themes that can be accessed.
  $theme = !empty($user->theme) && drupal_theme_access($user->theme) ? $user->theme : variable_get('theme_default', 'bartik');

  // Allow modules to override the theme. Validation has already been performed
  // inside menu_get_custom_theme(), so we do not need to check it again here.
  $custom_theme = menu_get_custom_theme();
  $theme = !empty($custom_theme) ? $custom_theme : $theme;

  // Store the identifier for retrieving theme settings with.
  $theme_key = $theme;

  // Find all our ancestor themes and put them in an array.
  $base_theme = array();
  $ancestor = $theme;
  while ($ancestor && isset($themes[$ancestor]->base_theme)) {
    $ancestor = $themes[$ancestor]->base_theme;
    $base_theme[] = $themes[$ancestor];
  }
  _drupal_theme_initialize($themes[$theme], array_reverse($base_theme));

  // Themes can have alter functions, so reset the drupal_alter() cache.
  drupal_static_reset('drupal_alter');

  // Provide the page with information about the theme that's used, so that a
  // later Ajax request can be rendered using the same theme.
  // @see ajax_base_page_theme()
  $setting['ajaxPageState'] = array(
    'theme' => $theme_key,
    'theme_token' => drupal_get_token($theme_key),
  );
  drupal_add_js($setting, 'setting');
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
