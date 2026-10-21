# drupal_aggregate_css()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3452–3474 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3452-L3474)

## Signature

```php
function drupal_aggregate_css(&$css_groups)
```

## Documentation

```text
Default callback to aggregate CSS files and inline content.

Having the browser load fewer CSS files results in much faster page loads
than when it loads many small files. This function aggregates files within
the same group into a single file unless the site-wide setting to do so is
disabled (commonly the case during site development). To optimize download,
it also compresses the aggregate files by removing comments, whitespace, and
other unnecessary content. Additionally, this functions aggregates inline
content together, regardless of the site-wide aggregation setting.

@param $css_groups
  An array of CSS groups as returned by drupal_group_css(). This function
  modifies the group's 'data' property for each group that is aggregated.

@see drupal_group_css()
@see drupal_pre_render_styles()
@see system_element_info()
```

## Code

```php
function drupal_aggregate_css(&$css_groups) {
  $preprocess_css = (variable_get('preprocess_css', FALSE) && !defined('MAINTENANCE_MODE'));

  // For each group that needs aggregation, aggregate its items.
  foreach ($css_groups as $key => $group) {
    switch ($group['type']) {
      // If a file group can be aggregated into a single file, do so, and set
      // the group's data property to the file path of the aggregate file.
      case 'file':
        if ($group['preprocess'] && $preprocess_css) {
          $css_groups[$key]['data'] = drupal_build_css_cache($group['items']);
        }
        break;
      // Aggregate all inline CSS content into the group's data property.
      case 'inline':
        $css_groups[$key]['data'] = '';
        foreach ($group['items'] as $item) {
          $css_groups[$key]['data'] .= drupal_load_stylesheet_content($item['data'], $item['preprocess']);
        }
        break;
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
