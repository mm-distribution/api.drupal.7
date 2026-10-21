# drupal_pre_render_scripts()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4568–4692 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4568-L4692)

## Signature

```php
function drupal_pre_render_scripts(array $elements)
```

## Documentation

```text
The #pre_render callback for the "scripts" element.

This callback adds elements needed for <script> tags to be rendered.

@param array $elements
  A render array containing:
  - '#items': The JS items as returned by drupal_add_js() and altered by
    drupal_get_js().

@return array
  The $elements variable passed as argument with two more children keys:
    - "scripts": contains the Javascript items
    - "settings": contains the Javascript settings items.
  If those keys are already existing, then the items will be appended and
  their keys will be preserved.

@see drupal_get_js()
@see drupal_add_js()
```

## Code

```php
function drupal_pre_render_scripts(array $elements) {
  $preprocess_js = (variable_get('preprocess_js', FALSE) && !defined('MAINTENANCE_MODE'));

  // A dummy query-string is added to filenames, to gain control over
  // browser-caching. The string changes on every update or full cache
  // flush, forcing browsers to load a new copy of the files, as the
  // URL changed. Files that should not be cached (see drupal_add_js())
  // get REQUEST_TIME as query-string instead, to enforce reload on every
  // page request.
  $default_query_string = variable_get('css_js_query_string', '0');

  // For inline JavaScript to validate as XHTML, all JavaScript containing
  // XHTML needs to be wrapped in CDATA. To make that backwards compatible
  // with HTML 4, we need to comment out the CDATA-tag.
  $embed_prefix = "\n<!--//--><![CDATA[//><!--\n";
  $embed_suffix = "\n//--><!]]>\n";

  // Since JavaScript may look for arguments in the URL and act on them, some
  // third-party code might require the use of a different query string.
  $js_version_string = variable_get('drupal_js_version_query_string', 'v=');

  $files = array();

  $scripts = isset($elements['scripts']) ? $elements['scripts'] : array();
  $scripts += array('#weight' => 0);

  $settings = isset($elements['settings']) ? $elements['settings'] : array();
  $settings += array('#weight' => $scripts['#weight'] + 10);

  // The index counter is used to keep aggregated and non-aggregated files in
  // order by weight. Use existing scripts count as a starting point.
  $index = count(element_children($scripts)) + 1;

  // Loop through the JavaScript to construct the rendered output.
  $element = array(
    '#type' => 'html_tag',
    '#tag' => 'script',
    '#value' => '',
    '#attributes' => array(
      'type' => 'text/javascript',
    ),
  );

  foreach ($elements['#items'] as $item) {
    $query_string =  empty($item['version']) ? $default_query_string : $js_version_string . $item['version'];

    switch ($item['type']) {
      case 'setting':
        $js_element = $element;
        $js_element['#value_prefix'] = $embed_prefix;
        $js_element['#value'] = 'jQuery.extend(Drupal.settings, ' . drupal_json_encode(drupal_array_merge_deep_array($item['data'])) . ");";
        $js_element['#value_suffix'] = $embed_suffix;
        $settings[] = $js_element;
        break;

      case 'inline':
        $js_element = $element;
        if ($item['defer']) {
          $js_element['#attributes']['defer'] = 'defer';
        }
        $js_element['#value_prefix'] = $embed_prefix;
        $js_element['#value'] = $item['data'];
        $js_element['#value_suffix'] = $embed_suffix;
        $scripts[$index++] = $js_element;
        break;

      case 'file':
        $js_element = $element;
        if (!$item['preprocess'] || !$preprocess_js) {
          if ($item['defer']) {
            $js_element['#attributes']['defer'] = 'defer';
          }
          $query_string_separator = (strpos($item['data'], '?') !== FALSE) ? '&' : '?';
          $js_element['#attributes']['src'] = file_create_url($item['data']) . $query_string_separator . ($item['cache'] ? $query_string : REQUEST_TIME);
          $scripts[$index++] = $js_element;
        }
        else {
          // By increasing the index for each aggregated file, we maintain
          // the relative ordering of JS by weight. We also set the key such
          // that groups are split by items sharing the same 'group' value and
          // 'every_page' flag. While this potentially results in more aggregate
          // files, it helps make each one more reusable across a site visit,
          // leading to better front-end performance of a website as a whole.
          // See drupal_add_js() for details.
          $key = 'aggregate_' . $item['group'] . '_' . $item['every_page'] . '_' . $index;
          $scripts[$key] = '';
          $files[$key][$item['data']] = $item;
        }
        break;

      case 'external':
        $js_element = $element;
        // Preprocessing for external JavaScript files is ignored.
        if ($item['defer']) {
          $js_element['#attributes']['defer'] = 'defer';
        }
        $js_element['#attributes']['src'] = $item['data'];
        $scripts[$index++] = $js_element;
        break;
    }
  }

  // Aggregate any remaining JS files that haven't already been output.
  if ($preprocess_js && count($files) > 0) {
    foreach ($files as $key => $file_set) {
      $uri = drupal_build_js_cache($file_set);
      // Only include the file if was written successfully. Errors are logged
      // using watchdog.
      if ($uri) {
        $preprocess_file = file_create_url($uri);
        $js_element = $element;
        $js_element['#attributes']['src'] = $preprocess_file;
        $scripts[$key] = $js_element;
      }
    }
  }

  // Keep the order of JS files consistent as some are preprocessed and others
  // are not. Make sure any inline or JS setting variables appear last after
  // libraries have loaded.
  $element['scripts'] = $scripts;
  $element['settings'] = $settings;

  return $element;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
