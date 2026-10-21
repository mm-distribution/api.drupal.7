# color_scheme_form_submit()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 363–491 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L363-L491)
- **Module/theme:** color

## Signature

```php
function color_scheme_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for color_scheme_form().

@see color_scheme_form_validate()
```

## Code

```php
function color_scheme_form_submit($form, &$form_state) {
  // Get theme coloring info.
  if (!isset($form_state['values']['info'])) {
    return;
  }
  $theme = $form_state['values']['theme'];
  $info = $form_state['values']['info'];

  // Resolve palette.
  $palette = $form_state['values']['palette'];
  if ($form_state['values']['scheme'] != '') {
    foreach ($palette as $key => $color) {
      if (isset($info['schemes'][$form_state['values']['scheme']]['colors'][$key])) {
        $palette[$key] = $info['schemes'][$form_state['values']['scheme']]['colors'][$key];
      }
    }
    $palette += $info['schemes']['default']['colors'];
  }

  // Make sure enough memory is available, if PHP's memory limit is compiled in.
  if (function_exists('memory_get_usage')) {
    // Fetch source image dimensions.
    $source = drupal_get_path('theme', $theme) . '/' . $info['base_image'];
    list($width, $height) = getimagesize($source);

    // We need at least a copy of the source and a target buffer of the same
    // size (both at 32bpp).
    $required = $width * $height * 8;
    // We intend to prevent color scheme changes if there isn't enough memory
    // available.  memory_get_usage(TRUE) returns a more accurate number than
    // memory_get_usage(), therefore we won't inadvertently reject a color
    // scheme change based on a faulty memory calculation.
    $usage = memory_get_usage(TRUE);
    $memory_limit = ini_get('memory_limit');
    $size = parse_size($memory_limit);
    if (!drupal_check_memory_limit($usage + $required, $memory_limit)) {
      drupal_set_message(t('There is not enough memory available to PHP to change this theme\'s color scheme. You need at least %size more. Check the <a href="@url">PHP documentation</a> for more information.', array('%size' => format_size($usage + $required - $size), '@url' => 'http://www.php.net/manual/ini.core.php#ini.sect.resource-limits')), 'error');
      return;
    }
  }

  // Delete old files.
  foreach (variable_get('color_' . $theme . '_files', array()) as $file) {
    @drupal_unlink($file);
  }
  if (isset($file) && $file = dirname($file)) {
    @drupal_rmdir($file);
  }

  // Don't render the default colorscheme, use the standard theme instead.
  if (implode(',', color_get_palette($theme, TRUE)) == implode(',', $palette)) {
    variable_del('color_' . $theme . '_palette');
    variable_del('color_' . $theme . '_stylesheets');
    variable_del('color_' . $theme . '_logo');
    variable_del('color_' . $theme . '_files');
    variable_del('color_' . $theme . '_screenshot');
    return;
  }

  // Prepare target locations for generated files.
  $id = $theme . '-' . substr(hash('sha256', serialize($palette) . microtime()), 0, 8);
  $paths['color'] = 'public://color';
  $paths['target'] = $paths['color'] . '/' . $id;
  foreach ($paths as $path) {
    file_prepare_directory($path, FILE_CREATE_DIRECTORY);
  }
  $paths['target'] = $paths['target'] . '/';
  $paths['id'] = $id;
  $paths['source'] = drupal_get_path('theme', $theme) . '/';
  $paths['files'] = $paths['map'] = array();

  // Save palette and logo location.
  variable_set('color_' . $theme . '_palette', $palette);
  variable_set('color_' . $theme . '_logo', $paths['target'] . 'logo.png');

  // Copy over neutral images.
  foreach ($info['copy'] as $file) {
    $base = drupal_basename($file);
    $source = $paths['source'] . $file;
    $filepath = file_unmanaged_copy($source, $paths['target'] . $base);
    $paths['map'][$file] = $base;
    $paths['files'][] = $filepath;
  }

  // Render new images, if image has been provided.
  if ($info['base_image']) {
    _color_render_images($theme, $info, $paths, $palette);
  }

  // Rewrite theme stylesheets.
  $css = array();
  foreach ($info['css'] as $stylesheet) {
    // Build a temporary array with LTR and RTL files.
    $files = array();
    if (file_exists($paths['source'] . $stylesheet)) {
      $files[] = $stylesheet;

      $rtl_file = str_replace('.css', '-rtl.css', $stylesheet);
      if (file_exists($paths['source'] . $rtl_file)) {
        $files[] = $rtl_file;
      }
    }

    foreach ($files as $file) {
      // Aggregate @imports recursively for each configured top level CSS file
      // without optimization. Aggregation and optimization will be
      // handled by drupal_build_css_cache() only.
      $style = drupal_load_stylesheet($paths['source'] . $file, FALSE);

      // Return the path to where this CSS file originated from, stripping
      // off the name of the file at the end of the path.
      $base = base_path() . dirname($paths['source'] . $file) . '/';
      _drupal_build_css_path(NULL, $base);

      // Prefix all paths within this CSS file, ignoring absolute paths.
      $style = preg_replace_callback('/url\([\'"]?(?![a-z]+:|\/+)([^\'")]+)[\'"]?\)/i', '_drupal_build_css_path', $style);

      // Rewrite stylesheet with new colors.
      $style = _color_rewrite_stylesheet($theme, $info, $paths, $palette, $style);
      $base_file = drupal_basename($file);
      $css[] = $paths['target'] . $base_file;
      _color_save_stylesheet($paths['target'] . $base_file, $style, $paths);
    }
  }

  // Maintain list of files.
  variable_set('color_' . $theme . '_stylesheets', $css);
  variable_set('color_' . $theme . '_files', $paths['files']);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
