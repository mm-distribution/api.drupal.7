# drupal_load_stylesheet()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3841–3875 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3841-L3875)

## Signature

```php
function drupal_load_stylesheet($file, $optimize = NULL, $reset_basepath = TRUE)
```

## Documentation

```text
Loads the stylesheet and resolves all @import commands.

Loads a stylesheet and replaces @import commands with the contents of the
imported file. Use this instead of file_get_contents when processing
stylesheets.

The returned contents are compressed removing white space and comments only
when CSS aggregation is enabled. This optimization will not apply for
color.module enabled themes with CSS aggregation turned off.

@param $file
  Name of the stylesheet to be processed.
@param $optimize
  Defines if CSS contents should be compressed or not.
@param $reset_basepath
  Used internally to facilitate recursive resolution of @import commands.

@return
  Contents of the stylesheet, including any resolved @import commands.
```

## Code

```php
function drupal_load_stylesheet($file, $optimize = NULL, $reset_basepath = TRUE) {
  // These statics are not cache variables, so we don't use drupal_static().
  static $_optimize, $basepath;
  if ($reset_basepath) {
    $basepath = '';
  }
  // Store the value of $optimize for preg_replace_callback with nested
  // @import loops.
  if (isset($optimize)) {
    $_optimize = $optimize;
  }

  // Stylesheets are relative one to each other. Start by adding a base path
  // prefix provided by the parent stylesheet (if necessary).
  if ($basepath && !file_uri_scheme($file)) {
    $file = $basepath . '/' . $file;
  }
  // Store the parent base path to restore it later.
  $parent_base_path = $basepath;
  // Set the current base path to process possible child imports.
  $basepath = dirname($file);

  // Load the CSS stylesheet. We suppress errors because themes may specify
  // stylesheets in their .info file that don't exist in the theme's path,
  // but are merely there to disable certain module CSS files.
  $content = '';
  if ($contents = @file_get_contents($file)) {
    // Return the processed stylesheet.
    $content = drupal_load_stylesheet_content($contents, $_optimize);
  }

  // Restore the parent base path as the file and its childen are processed.
  $basepath = $parent_base_path;
  return $content;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
