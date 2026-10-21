# drupal_add_js()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4341–4435 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4341-L4435)

## Signature

```php
function drupal_add_js($data = NULL, $options = NULL)
```

## Documentation

```text
Adds a JavaScript file, setting, or inline code to the page.

The behavior of this function depends on the parameters it is called with.
Generally, it handles the addition of JavaScript to the page, either as
reference to an existing file or as inline code. The following actions can be
performed using this function:
- Add a file ('file'): Adds a reference to a JavaScript file to the page.
- Add inline JavaScript code ('inline'): Executes a piece of JavaScript code
  on the current page by placing the code directly in the page (for example,
  to tell the user that a new message arrived, by opening a pop up, alert
  box, etc.). This should only be used for JavaScript that cannot be executed
  from a file. When adding inline code, make sure that you are not relying on
  $() being the jQuery function. Wrap your code in
  @code (function ($) {... })(jQuery); @endcode
  or use jQuery() instead of $().
- Add external JavaScript ('external'): Allows the inclusion of external
  JavaScript files that are not hosted on the local server. Note that these
  external JavaScript references do not get aggregated when preprocessing is
  on.
- Add settings ('setting'): Adds settings to Drupal's global storage of
  JavaScript settings. Per-page settings are required by some modules to
  function properly. All settings will be accessible at Drupal.settings.

Examples:
@code
  drupal_add_js('misc/collapse.js');
  drupal_add_js('misc/collapse.js', 'file');
  drupal_add_js('jQuery(document).ready(function () { alert("Hello!"); });', 'inline');
  drupal_add_js('jQuery(document).ready(function () { alert("Hello!"); });',
    array('type' => 'inline', 'scope' => 'footer', 'weight' => 5)
  );
  drupal_add_js('http://example.com/example.js', 'external');
  drupal_add_js(array('myModule' => array('key' => 'value')), 'setting');
@endcode

Calling drupal_static_reset('drupal_add_js') will clear all JavaScript added
so far.

If JavaScript aggregation is enabled, all JavaScript files added with
$options['preprocess'] set to TRUE will be merged into one aggregate file.
Preprocessed inline JavaScript will not be aggregated into this single file.
Externally hosted JavaScripts are never aggregated.

The reason for aggregating the files is outlined quite thoroughly here:
http://www.die.net/musings/page_load_time/ "Load fewer external objects. Due
to request overhead, one bigger file just loads faster than two smaller ones
half its size."

$options['preprocess'] should be only set to TRUE when a file is required for
all typical visitors and most pages of a site. It is critical that all
preprocessed files are added unconditionally on every page, even if the
files are not needed on a page. This is normally done by calling
drupal_add_js() in a hook_init() implementation.

Non-preprocessed files should only be added to the page when they are
actually needed.

@param $data
  (optional) If given, the value depends on the $options parameter, or
  $options['type'] if $options is passed as an associative array:
  - 'file': Path to the file relative to base_path().
  - 'inline': The JavaScript code that should be placed in the given scope.
  - 'external': The absolute path to an external JavaScript file that is not
    hosted on the local server. These files will not be aggregated if
    JavaScript aggregation is enabled.
  - 'setting': An associative array with configuration options. The array is
    merged directly into Drupal.settings. All modules should wrap their
    actual configuration settings in another variable to prevent conflicts in
    the Drupal.settings namespace. Items added with a string key will replace
    existing settings with that key; items with numeric array keys will be
    added to the existing settings array.
@param $options
  (optional) A string defining the type of JavaScript that is being added in
  the $data parameter ('file'/'setting'/'inline'/'external'), or an
  associative array. JavaScript settings should always pass the string
  'setting' only. Other types can have the following elements in the array:
  - type: The type of JavaScript that is to be added to the page. Allowed
    values are 'file', 'inline', 'external' or 'setting'. Defaults
    to 'file'.
  - scope: The location in which you want to place the script. Possible
    values are 'header' or 'footer'. If your theme implements different
    regions, you can also use these. Defaults to 'header'.
  - group: A number identifying the group in which to add the JavaScript.
    Available constants are:
    - JS_LIBRARY: Any libraries, settings, or jQuery plugins.
    - JS_DEFAULT: Any module-layer JavaScript.
    - JS_THEME: Any theme-layer JavaScript.
    The group number serves as a weight: JavaScript within a lower weight
    group is presented on the page before JavaScript within a higher weight
    group.
  - every_page: For optimal front-end performance when aggregation is
    enabled, this should be set to TRUE if the JavaScript is present on every
    page of the website for users for whom it is present at all. This
    defaults to FALSE. It is set to TRUE for JavaScript files that are added
    via module and theme .info files. Modules that add JavaScript within
    hook_init() implementations, or from other code that ensures that the
    JavaScript is added to all website pages, should also set this flag to
    TRUE. All JavaScript files within the same group and that have the
    'every_page' flag set to TRUE and do not have 'preprocess' set to FALSE
    are aggregated together into a single aggregate file, and that aggregate
    file can be reused across a user's entire site visit, leading to faster
    navigation between pages. However, JavaScript that is only needed on
    pages less frequently visited, can be added by code that only runs for
    those particular pages, and that code should not set the 'every_page'
    flag. This minimizes the size of the aggregate file that the user needs
    to download when first visiting the website. JavaScript without the
    'every_page' flag is aggregated into a separate aggregate file. This
    other aggregate file is likely to change from page to page, and each new
    aggregate file needs to be downloaded when first encountered, so it
    should be kept relatively small by ensuring that most commonly needed
    JavaScript is added to every page.
  - weight: A number defining the order in which the JavaScript is added to
    the page relative to other JavaScript with the same 'scope', 'group',
    and 'every_page' value. In some cases, the order in which the JavaScript
    is presented on the page is very important. jQuery, for example, must be
    added to the page before any jQuery code is run, so jquery.js uses the
    JS_LIBRARY group and a weight of -20, jquery.once.js (a library drupal.js
    depends on) uses the JS_LIBRARY group and a weight of -19, drupal.js uses
    the JS_LIBRARY group and a weight of -1, other libraries use the
    JS_LIBRARY group and a weight of 0 or higher, and all other scripts use
    one of the other group constants. The exact ordering of JavaScript is as
    follows:
    - First by scope, with 'header' first, 'footer' last, and any other
      scopes provided by a custom theme coming in between, as determined by
      the theme.
    - Then by group.
    - Then by the 'every_page' flag, with TRUE coming before FALSE.
    - Then by weight.
    - Then by the order in which the JavaScript was added. For example, all
      else being the same, JavaScript added by a call to drupal_add_js() that
      happened later in the page request gets added to the page after one for
      which drupal_add_js() happened earlier in the page request.
  - requires_jquery: Set this to FALSE if the JavaScript you are adding does
    not have a dependency on jQuery. Defaults to TRUE, except for JavaScript
    settings where it defaults to FALSE. This is used on sites that have the
    'javascript_always_use_jquery' variable set to FALSE; on those sites, if
    all the JavaScript added to the page by drupal_add_js() does not have a
    dependency on jQuery, then for improved front-end performance Drupal
    will not add jQuery and related libraries and settings to the page.
  - defer: If set to TRUE, the defer attribute is set on the <script>
    tag. Defaults to FALSE.
  - cache: If set to FALSE, the JavaScript file is loaded anew on every page
    call; in other words, it is not cached. Used only when 'type' references
    a JavaScript file. Defaults to TRUE.
  - preprocess: If TRUE and JavaScript aggregation is enabled, the script
    file will be aggregated. Defaults to TRUE.

@return
  The current array of JavaScript files, settings, and in-line code,
  including Drupal defaults, anything previously added with calls to
  drupal_add_js(), and this function call's additions.

@see drupal_get_js()
```

## Code

```php
function drupal_add_js($data = NULL, $options = NULL) {
  $javascript = &drupal_static(__FUNCTION__, array());
  $jquery_added = &drupal_static(__FUNCTION__ . ':jquery_added', FALSE);

  // If the $javascript variable has been reset with drupal_static_reset(),
  // jQuery and related files will have been removed from the list, so set the
  // variable back to FALSE to indicate they have not yet been added.
  if (empty($javascript)) {
    $jquery_added = FALSE;
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
  if (isset($options['type']) && $options['type'] == 'setting') {
    $options += array('requires_jquery' => FALSE);
  }
  $options += drupal_js_defaults($data);

  // Preprocess can only be set if caching is enabled.
  $options['preprocess'] = $options['cache'] ? $options['preprocess'] : FALSE;

  // Tweak the weight so that files of the same weight are included in the
  // order of the calls to drupal_add_js().
  $options['weight'] += count($javascript) / 1000;

  if (isset($data)) {
    // Add jquery.js, drupal.js, and related files and settings if they have
    // not been added yet. However, if the 'javascript_always_use_jquery'
    // variable is set to FALSE (indicating that the site does not want jQuery
    // automatically added on all pages) then only add it if a file or setting
    // that requires jQuery is being added also.
    if (!$jquery_added && (variable_get('javascript_always_use_jquery', TRUE) || $options['requires_jquery'])) {
      $jquery_added = TRUE;
      // url() generates the prefix using hook_url_outbound_alter(). Instead of
      // running the hook_url_outbound_alter() again here, extract the prefix
      // from url().
      url('', array('prefix' => &$prefix));
      $default_javascript = array(
        'settings' => array(
          'data' => array(
            array('basePath' => base_path()),
            array('pathPrefix' => empty($prefix) ? '' : $prefix),
            array('setHasJsCookie' => variable_get('set_has_js_cookie', FALSE) ? 1 : 0),
          ),
          'type' => 'setting',
          'scope' => 'header',
          'group' => JS_LIBRARY,
          'every_page' => TRUE,
          'weight' => 0,
        ),
        'misc/drupal.js' => array(
          'data' => 'misc/drupal.js',
          'type' => 'file',
          'scope' => 'header',
          'group' => JS_LIBRARY,
          'every_page' => TRUE,
          'weight' => -1,
          'requires_jquery' => TRUE,
          'preprocess' => TRUE,
          'cache' => TRUE,
          'defer' => FALSE,
        ),
      );
      $javascript = drupal_array_merge_deep($javascript, $default_javascript);
      // Register all required libraries.
      drupal_add_library('system', 'jquery', TRUE);
      drupal_add_library('system', 'jquery.once', TRUE);
    }

    switch ($options['type']) {
      case 'setting':
        // All JavaScript settings are placed in the header of the page with
        // the library weight so that inline scripts appear afterwards.
        $javascript['settings']['data'][] = $data;
        break;

      case 'inline':
        $javascript[] = $options;
        break;

      default: // 'file' and 'external'
        // Local and external files must keep their name as the associative key
        // so the same JavaScript file is not added twice.
        $javascript[$options['data']] = $options;
    }
  }
  return $javascript;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
