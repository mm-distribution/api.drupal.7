# drupal_add_css()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3137–3199 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3137-L3199)

## Signature

```php
function drupal_add_css($data = NULL, $options = NULL)
```

## Documentation

```text
Adds a cascading stylesheet to the stylesheet queue.

Calling drupal_static_reset('drupal_add_css') will clear all cascading
stylesheets added so far.

If CSS aggregation/compression is enabled, all cascading style sheets added
with $options['preprocess'] set to TRUE will be merged into one aggregate
file and compressed by removing all extraneous white space.
Preprocessed inline stylesheets will not be aggregated into this single file;
instead, they are just compressed upon output on the page. Externally hosted
stylesheets are never aggregated or compressed.

The reason for aggregating the files is outlined quite thoroughly here:
http://www.die.net/musings/page_load_time/ "Load fewer external objects. Due
to request overhead, one bigger file just loads faster than two smaller ones
half its size."

$options['preprocess'] should be only set to TRUE when a file is required for
all typical visitors and most pages of a site. It is critical that all
preprocessed files are added unconditionally on every page, even if the
files do not happen to be needed on a page. This is normally done by calling
drupal_add_css() in a hook_init() implementation.

Non-preprocessed files should only be added to the page when they are
actually needed.

@param $data
  (optional) The stylesheet data to be added, depending on what is passed
  through to the $options['type'] parameter:
  - 'file': The path to the CSS file relative to the base_path(), or a
    stream wrapper URI. For example: "modules/devel/devel.css" or
    "public://generated_css/stylesheet_1.css". Note that Modules should
    always prefix the names of their CSS files with the module name; for
    example, system-menus.css rather than simply menus.css. Themes can
    override module-supplied CSS files based on their filenames, and this
    prefixing helps prevent confusing name collisions for theme developers.
    See drupal_get_css() where the overrides are performed. Also, if the
    direction of the current language is right-to-left (Hebrew, Arabic,
    etc.), the function will also look for an RTL CSS file and append it to
    the list. The name of this file should have an '-rtl.css' suffix. For
    example, a CSS file called 'mymodule-name.css' will have a
    'mymodule-name-rtl.css' file added to the list, if exists in the same
    directory. This CSS file should contain overrides for properties which
    should be reversed or otherwise different in a right-to-left display.
  - 'inline': A string of CSS that should be placed in the given scope. Note
    that it is better practice to use 'file' stylesheets, rather than
    'inline', as the CSS would then be aggregated and cached.
  - 'external': The absolute path to an external CSS file that is not hosted
    on the local server. These files will not be aggregated if CSS
    aggregation is enabled.
@param $options
  (optional) A string defining the 'type' of CSS that is being added in the
  $data parameter ('file', 'inline', or 'external'), or an array which can
  have any or all of the following keys:
  - 'type': The type of stylesheet being added. Available options are 'file',
    'inline' or 'external'. Defaults to 'file'.
  - 'basename': Force a basename for the file being added. Modules are
    expected to use stylesheets with unique filenames, but integration of
    external libraries may make this impossible. The basename of
    'modules/node/node.css' is 'node.css'. If the external library "node.js"
    ships with a 'node.css', then a different, unique basename would be
    'node.js.css'.
  - 'group': A number identifying the group in which to add the stylesheet.
    Available constants are:
    - CSS_SYSTEM: Any system-layer CSS.
    - CSS_DEFAULT: (default) Any module-layer CSS.
    - CSS_THEME: Any theme-layer CSS.
    The group number serves as a weight: the markup for loading a stylesheet
    within a lower weight group is output to the page before the markup for
    loading a stylesheet within a higher weight group, so CSS within higher
    weight groups take precendence over CSS within lower weight groups.
  - 'every_page': For optimal front-end performance when aggregation is
    enabled, this should be set to TRUE if the stylesheet is present on every
    page of the website for users for whom it is present at all. This
    defaults to FALSE. It is set to TRUE for stylesheets added via module and
    theme .info files. Modules that add stylesheets within hook_init()
    implementations, or from other code that ensures that the stylesheet is
    added to all website pages, should also set this flag to TRUE. All
    stylesheets within the same group that have the 'every_page' flag set to
    TRUE and do not have 'preprocess' set to FALSE are aggregated together
    into a single aggregate file, and that aggregate file can be reused
    across a user's entire site visit, leading to faster navigation between
    pages. However, stylesheets that are only needed on pages less frequently
    visited, can be added by code that only runs for those particular pages,
    and that code should not set the 'every_page' flag. This minimizes the
    size of the aggregate file that the user needs to download when first
    visiting the website. Stylesheets without the 'every_page' flag are
    aggregated into a separate aggregate file. This other aggregate file is
    likely to change from page to page, and each new aggregate file needs to
    be downloaded when first encountered, so it should be kept relatively
    small by ensuring that most commonly needed stylesheets are added to
    every page.
  - 'weight': The weight of the stylesheet specifies the order in which the
    CSS will appear relative to other stylesheets with the same group and
    'every_page' flag. The exact ordering of stylesheets is as follows:
    - First by group.
    - Then by the 'every_page' flag, with TRUE coming before FALSE.
    - Then by weight.
    - Then by the order in which the CSS was added. For example, all else
      being the same, a stylesheet added by a call to drupal_add_css() that
      happened later in the page request gets added to the page after one for
      which drupal_add_css() happened earlier in the page request.
  - 'media': The media type for the stylesheet, e.g., all, print, screen.
    Defaults to 'all'.
  - 'preprocess': If TRUE and CSS aggregation/compression is enabled, the
    styles will be aggregated and compressed. Defaults to TRUE.
  - 'browsers': An array containing information specifying which browsers
    should load the CSS item. See drupal_pre_render_conditional_comments()
    for details.

@return
  An array of queued cascading stylesheets.

@see drupal_get_css()
```

## Code

```php
function drupal_add_css($data = NULL, $options = NULL) {
  $css = &drupal_static(__FUNCTION__, array());
  $count = &drupal_static(__FUNCTION__ . '_count', 0);

  // If the $css variable has been reset with drupal_static_reset(), there is
  // no longer any CSS being tracked, so set the counter back to 0 also.
  if (count($css) === 0) {
    $count = 0;
  }

  // Construct the options, taking the defaults into consideration.
  if (isset($options)) {
    if (!is_array($options)) {
      $options = array('type' => $options);
    }
  }
  else {
    $options = array();
  }

  // Create an array of CSS files for each media type first, since each type needs to be served
  // to the browser differently.
  if (isset($data)) {
    $options += array(
      'type' => 'file',
      'group' => CSS_DEFAULT,
      'weight' => 0,
      'every_page' => FALSE,
      'media' => 'all',
      'preprocess' => TRUE,
      'data' => $data,
      'browsers' => array(),
    );
    $options['browsers'] += array(
      'IE' => TRUE,
      '!IE' => TRUE,
    );

    // Files with a query string cannot be preprocessed.
    if ($options['type'] === 'file' && $options['preprocess'] && strpos($options['data'], '?') !== FALSE) {
      $options['preprocess'] = FALSE;
    }

    // Always add a tiny value to the weight, to conserve the insertion order.
    $options['weight'] += $count / 1000;
    $count++;

    // Add the data to the CSS array depending on the type.
    switch ($options['type']) {
      case 'inline':
        // For inline stylesheets, we don't want to use the $data as the array
        // key as $data could be a very long string of CSS.
        $css[] = $options;
        break;
      default:
        // Local and external files must keep their name as the associative key
        // so the same CSS file is not be added twice.
        $css[$data] = $options;
    }
  }

  return $css;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
