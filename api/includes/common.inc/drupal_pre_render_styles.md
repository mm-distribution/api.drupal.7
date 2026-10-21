# drupal_pre_render_styles()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3537–3702 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3537-L3702)

## Signature

```php
function drupal_pre_render_styles($elements)
```

## Documentation

```text
#pre_render callback to add the elements needed for CSS tags to be rendered.

For production websites, LINK tags are preferable to STYLE tags with @import
statements, because:
- They are the standard tag intended for linking to a resource.
- On Firefox 2 and perhaps other browsers, CSS files included with @import
  statements don't get saved when saving the complete web page for offline
  use: http://drupal.org/node/145218.
- On IE, if only LINK tags and no @import statements are used, all the CSS
  files are downloaded in parallel, resulting in faster page load, but if
  @import statements are used and span across multiple STYLE tags, all the
  ones from one STYLE tag must be downloaded before downloading begins for
  the next STYLE tag. Furthermore, IE7 does not support media declaration on
  the @import statement, so multiple STYLE tags must be used when different
  files are for different media types. Non-IE browsers always download in
  parallel, so this is an IE-specific performance quirk:
  http://www.stevesouders.com/blog/2009/04/09/dont-use-import/.

However, IE has an annoying limit of 31 total CSS inclusion tags
(http://drupal.org/node/228818) and LINK tags are limited to one file per
tag, whereas STYLE tags can contain multiple @import statements allowing
multiple files to be loaded per tag. When CSS aggregation is disabled, a
Drupal site can easily have more than 31 CSS files that need to be loaded, so
using LINK tags exclusively would result in a site that would display
incorrectly in IE. Depending on different needs, different strategies can be
employed to decide when to use LINK tags and when to use STYLE tags.

The strategy employed by this function is to use LINK tags for all aggregate
files and for all files that cannot be aggregated (e.g., if 'preprocess' is
set to FALSE or the type is 'external'), and to use STYLE tags for groups
of files that could be aggregated together but aren't (e.g., if the site-wide
aggregation setting is disabled). This results in all LINK tags when
aggregation is enabled, a guarantee that as many or only slightly more tags
are used with aggregation disabled than enabled (so that if the limit were to
be crossed with aggregation enabled, the site developer would also notice the
problem while aggregation is disabled), and an easy way for a developer to
view HTML source while aggregation is disabled and know what files will be
aggregated together when aggregation becomes enabled.

This function evaluates the aggregation enabled/disabled condition on a group
by group basis by testing whether an aggregate file has been made for the
group rather than by testing the site-wide aggregation setting. This allows
this function to work correctly even if modules have implemented custom
logic for grouping and aggregating files.

@param $element
  A render array containing:
  - '#items': The CSS items as returned by drupal_add_css() and altered by
    drupal_get_css().
  - '#group_callback': A function to call to group #items to enable the use
    of fewer tags by aggregating files and/or using multiple @import
    statements within a single tag.
  - '#aggregate_callback': A function to call to aggregate the items within
    the groups arranged by the #group_callback function.

@return
  A render array that will render to a string of XHTML CSS tags.

@see drupal_get_css()
```

## Code

```php
function drupal_pre_render_styles($elements) {
  // Group and aggregate the items.
  if (isset($elements['#group_callback'])) {
    $elements['#groups'] = $elements['#group_callback']($elements['#items']);
  }
  if (isset($elements['#aggregate_callback'])) {
    $elements['#aggregate_callback']($elements['#groups']);
  }

  // A dummy query-string is added to filenames, to gain control over
  // browser-caching. The string changes on every update or full cache
  // flush, forcing browsers to load a new copy of the files, as the
  // URL changed.
  $query_string = variable_get('css_js_query_string', '0');

  // For inline CSS to validate as XHTML, all CSS containing XHTML needs to be
  // wrapped in CDATA. To make that backwards compatible with HTML 4, we need to
  // comment out the CDATA-tag.
  $embed_prefix = "\n<!--/*--><![CDATA[/*><!--*/\n";
  $embed_suffix = "\n/*]]>*/-->\n";

  // Defaults for LINK and STYLE elements.
  $link_element_defaults = array(
    '#type' => 'html_tag',
    '#tag' => 'link',
    '#attributes' => array(
      'type' => 'text/css',
      'rel' => 'stylesheet',
    ),
  );
  $style_element_defaults = array(
    '#type' => 'html_tag',
    '#tag' => 'style',
    '#attributes' => array(
      'type' => 'text/css',
    ),
  );

  // Loop through each group.
  foreach ($elements['#groups'] as $group) {
    switch ($group['type']) {
      // For file items, there are three possibilites.
      // - The group has been aggregated: in this case, output a LINK tag for
      //   the aggregate file.
      // - The group can be aggregated but has not been (most likely because
      //   the site administrator disabled the site-wide setting): in this case,
      //   output as few STYLE tags for the group as possible, using @import
      //   statement for each file in the group. This enables us to stay within
      //   IE's limit of 31 total CSS inclusion tags.
      // - The group contains items not eligible for aggregation (their
      //   'preprocess' flag has been set to FALSE): in this case, output a LINK
      //   tag for each file.
      case 'file':
        // The group has been aggregated into a single file: output a LINK tag
        // for the aggregate file.
        if (isset($group['data'])) {
          $element = $link_element_defaults;
          $element['#attributes']['href'] = file_create_url($group['data']);
          $element['#attributes']['media'] = $group['media'];
          $element['#browsers'] = $group['browsers'];
          $elements[] = $element;
        }
        // The group can be aggregated, but hasn't been: combine multiple items
        // into as few STYLE tags as possible.
        elseif ($group['preprocess']) {
          $import = array();
          foreach ($group['items'] as $item) {
            // A theme's .info file may have an entry for a file that doesn't
            // exist as a way of overriding a module or base theme CSS file from
            // being added to the page. Normally, file_exists() calls that need
            // to run for every page request should be minimized, but this one
            // is okay, because it only runs when CSS aggregation is disabled.
            // On a server under heavy enough load that file_exists() calls need
            // to be minimized, CSS aggregation should be enabled, in which case
            // this code is not run. When aggregation is enabled,
            // drupal_load_stylesheet() checks file_exists(), but only when
            // building the aggregate file, which is then reused for many page
            // requests.
            if (file_exists($item['data'])) {
              // The dummy query string needs to be added to the URL to control
              // browser-caching. IE7 does not support a media type on the
              // @import statement, so we instead specify the media for the
              // group on the STYLE tag.
              $import[] = '@import url("' . check_plain(file_create_url($item['data']) . '?' . $query_string) . '");';
            }
          }
          // In addition to IE's limit of 31 total CSS inclusion tags, it also
          // has a limit of 31 @import statements per STYLE tag.
          while (!empty($import)) {
            $import_batch = array_slice($import, 0, 31);
            $import = array_slice($import, 31);
            $element = $style_element_defaults;
            // This simplifies the JavaScript regex, allowing each line
            // (separated by \n) to be treated as a completely different string.
            // This means that we can use ^ and $ on one line at a time, and not
            // worry about style tags since they'll never match the regex.
            $element['#value'] = "\n" . implode("\n", $import_batch) . "\n";
            $element['#attributes']['media'] = $group['media'];
            $element['#browsers'] = $group['browsers'];
            $elements[] = $element;
          }
        }
        // The group contains items ineligible for aggregation: output a LINK
        // tag for each file.
        else {
          foreach ($group['items'] as $item) {
            $element = $link_element_defaults;
            // We do not check file_exists() here, because this code runs for
            // files whose 'preprocess' is set to FALSE, and therefore, even
            // when aggregation is enabled, and we want to avoid needlessly
            // taxing a server that may be under heavy load. The file_exists()
            // performed above for files whose 'preprocess' is TRUE is done for
            // the benefit of theme .info files, but code that deals with files
            // whose 'preprocess' is FALSE is responsible for ensuring the file
            // exists.
            // The dummy query string needs to be added to the URL to control
            // browser-caching.
            $query_string_separator = (strpos($item['data'], '?') !== FALSE) ? '&' : '?';
            $element['#attributes']['href'] = file_create_url($item['data']) . $query_string_separator . $query_string;
            $element['#attributes']['media'] = $item['media'];
            $element['#browsers'] = $group['browsers'];
            $elements[] = $element;
          }
        }
        break;
      // For inline content, the 'data' property contains the CSS content. If
      // the group's 'data' property is set, then output it in a single STYLE
      // tag. Otherwise, output a separate STYLE tag for each item.
      case 'inline':
        if (isset($group['data'])) {
          $element = $style_element_defaults;
          $element['#value'] = $group['data'];
          $element['#value_prefix'] = $embed_prefix;
          $element['#value_suffix'] = $embed_suffix;
          $element['#attributes']['media'] = $group['media'];
          $element['#browsers'] = $group['browsers'];
          $elements[] = $element;
        }
        else {
          foreach ($group['items'] as $item) {
            $element = $style_element_defaults;
            $element['#value'] = $item['data'];
            $element['#value_prefix'] = $embed_prefix;
            $element['#value_suffix'] = $embed_suffix;
            $element['#attributes']['media'] = $item['media'];
            $element['#browsers'] = $group['browsers'];
            $elements[] = $element;
          }
        }
        break;
      // Output a LINK tag for each external item. The item's 'data' property
      // contains the full URL.
      case 'external':
        foreach ($group['items'] as $item) {
          $element = $link_element_defaults;
          $element['#attributes']['href'] = $item['data'];
          $element['#attributes']['media'] = $item['media'];
          $element['#browsers'] = $group['browsers'];
          $elements[] = $element;
        }
        break;
    }
  }

  return $elements;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
