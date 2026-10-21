# _color_html_alter()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 85–109 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L85-L109)
- **Module/theme:** color

## Signature

```php
function _color_html_alter(&$vars)
```

## Documentation

```text
Replaces style sheets with color-altered style sheets.

A theme that supports the color module should call this function from its
THEME_process_html() function, so that the correct style sheets are
included when html.tpl.php is rendered.

@see theme()
```

## Code

```php
function _color_html_alter(&$vars) {
  global $theme_key;
  $themes = list_themes();

  // Override stylesheets.
  $color_paths = variable_get('color_' . $theme_key . '_stylesheets', array());
  if (!empty($color_paths)) {

    foreach ($themes[$theme_key]->stylesheets['all'] as $base_filename => $old_path) {
      // Loop over the path array with recolored CSS files to find matching
      // paths which could replace the non-recolored paths.
      foreach ($color_paths as $color_path) {
        // Color module currently requires unique file names to be used,
        // which allows us to compare different file paths.
        if (drupal_basename($old_path) == drupal_basename($color_path)) {
          // Replace the path to the new css file.
          // This keeps the order of the stylesheets intact.
          $vars['css'][$old_path]['data'] = $color_path;
        }
      }
    }

    $vars['styles'] = drupal_get_css($vars['css']);
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
