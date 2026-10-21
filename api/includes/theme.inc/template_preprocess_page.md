# template_preprocess_page()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2677–2720 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2677-L2720)

## Signature

```php
function template_preprocess_page(&$variables)
```

## Documentation

```text
Preprocess variables for page.tpl.php

Most themes utilize their own copy of page.tpl.php. The default is located
inside "modules/system/page.tpl.php". Look in there for the full list of
variables.

Uses the arg() function to generate a series of page template suggestions
based on the current path.

Any changes to variables in this preprocessor should also be changed inside
template_preprocess_maintenance_page() to keep all of them consistent.

@see drupal_render_page()
@see template_process_page()
@see page.tpl.php
```

## Code

```php
function template_preprocess_page(&$variables) {
  // Move some variables to the top level for themer convenience and template cleanliness.
  $variables['show_messages'] = $variables['page']['#show_messages'];

  foreach (system_region_list($GLOBALS['theme'], REGIONS_ALL, FALSE) as $region_key) {
    if (!isset($variables['page'][$region_key])) {
      $variables['page'][$region_key] = array();
    }
    if ($region_content = drupal_get_region_content($region_key)) {
      $variables['page'][$region_key][]['#markup'] = $region_content;
    }
  }

  // Set up layout variable.
  $variables['layout'] = 'none';
  if (!empty($variables['page']['sidebar_first'])) {
    $variables['layout'] = 'first';
  }
  if (!empty($variables['page']['sidebar_second'])) {
    $variables['layout'] = ($variables['layout'] == 'first') ? 'both' : 'second';
  }

  $variables['base_path']         = base_path();
  $variables['front_page']        = url();
  $variables['feed_icons']        = drupal_get_feeds();
  $variables['language']          = $GLOBALS['language'];
  $variables['language']->dir     = $GLOBALS['language']->direction ? 'rtl' : 'ltr';
  $variables['logo']              = theme_get_setting('logo');
  $variables['main_menu']         = theme_get_setting('toggle_main_menu') ? menu_main_menu() : array();
  $variables['secondary_menu']    = theme_get_setting('toggle_secondary_menu') ? menu_secondary_menu() : array();
  $variables['action_links']      = menu_local_actions();
  $variables['site_name']         = (theme_get_setting('toggle_name') ? filter_xss_admin(variable_get('site_name', 'Drupal')) : '');
  $variables['site_slogan']       = (theme_get_setting('toggle_slogan') ? filter_xss_admin(variable_get('site_slogan', '')) : '');
  $variables['tabs']              = menu_local_tabs();

  if ($node = menu_get_object()) {
    $variables['node'] = $node;
  }

  // Populate the page template suggestions.
  if ($suggestions = theme_get_suggestions(arg(), 'page')) {
    $variables['theme_hook_suggestions'] = $suggestions;
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
