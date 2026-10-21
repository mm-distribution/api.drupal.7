# drupal_get_css()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3230–3280 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3230-L3280)

## Signature

```php
function drupal_get_css($css = NULL, $skip_alter = FALSE)
```

## Documentation

```text
Returns a themed representation of all stylesheets to attach to the page.

It loads the CSS in order, with 'module' first, then 'theme' afterwards.
This ensures proper cascading of styles so themes can easily override
module styles through CSS selectors.

Themes may replace module-defined CSS files by adding a stylesheet with the
same filename. For example, themes/bartik/system-menus.css would replace
modules/system/system-menus.css. This allows themes to override complete
CSS files, rather than specific selectors, when necessary.

If the original CSS file is being overridden by a theme, the theme is
responsible for supplying an accompanying RTL CSS file to replace the
module's.

@param $css
  (optional) An array of CSS files. If no array is provided, the default
  stylesheets array is used instead.
@param $skip_alter
  (optional) If set to TRUE, this function skips calling drupal_alter() on
  $css, useful when the calling function passes a $css array that has already
  been altered.

@return
  A string of XHTML CSS tags.

@see drupal_add_css()
```

## Code

```php
function drupal_get_css($css = NULL, $skip_alter = FALSE) {
  if (!isset($css)) {
    $css = drupal_add_css();
  }

  // Allow modules and themes to alter the CSS items.
  if (!$skip_alter) {
    drupal_alter('css', $css);
  }

  // Sort CSS items, so that they appear in the correct order.
  uasort($css, 'drupal_sort_css_js');

  // Provide the page with information about the individual CSS files used,
  // information not otherwise available when CSS aggregation is enabled. The
  // setting is attached later in this function, but is set here, so that CSS
  // files removed below are still considered "used" and prevented from being
  // added in a later AJAX request.
  // Skip if no files were added to the page or jQuery.extend() will overwrite
  // the Drupal.settings.ajaxPageState.css object with an empty array.
  if (!empty($css)) {
    // Cast the array to an object to be on the safe side even if not empty.
    $setting['ajaxPageState']['css'] = (object) array_fill_keys(array_keys($css), 1);
  }

  // Remove the overridden CSS files. Later CSS files override former ones.
  $previous_item = array();
  foreach ($css as $key => $item) {
    if ($item['type'] == 'file') {
      // If defined, force a unique basename for this file.
      $basename = isset($item['basename']) ? $item['basename'] : drupal_basename($item['data']);
      if (isset($previous_item[$basename])) {
        // Remove the previous item that shared the same base name.
        unset($css[$previous_item[$basename]]);
      }
      $previous_item[$basename] = $key;
    }
  }

  // Render the HTML needed to load the CSS.
  $styles = array(
    '#type' => 'styles',
    '#items' => $css,
  );

  if (!empty($setting)) {
    $styles['#attached']['js'][] = array('type' => 'setting', 'data' => $setting);
  }

  return drupal_render($styles);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
