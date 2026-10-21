# drupal_get_js()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4495–4546 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4495-L4546)

## Signature

```php
function drupal_get_js($scope = 'header', $javascript = NULL, $skip_alter = FALSE)
```

## Documentation

```text
Returns a themed presentation of all JavaScript code for the current page.

References to JavaScript files are placed in a certain order: first, all
'core' files, then all 'module' and finally all 'theme' JavaScript files
are added to the page. Then, all settings are output, followed by 'inline'
JavaScript code. If running update.php, all preprocessing is disabled.

Note that hook_js_alter(&$javascript) is called during this function call
to allow alterations of the JavaScript during its presentation. Calls to
drupal_add_js() from hook_js_alter() will not be added to the output
presentation. The correct way to add JavaScript during hook_js_alter()
is to add another element to the $javascript array, deriving from
drupal_js_defaults(). See locale_js_alter() for an example of this.

@param $scope
  (optional) The scope for which the JavaScript rules should be returned.
  Defaults to 'header'.
@param $javascript
  (optional) An array with all JavaScript code. Defaults to the default
  JavaScript array for the given scope.
@param $skip_alter
  (optional) If set to TRUE, this function skips calling drupal_alter() on
  $javascript, useful when the calling function passes a $javascript array
  that has already been altered.

@return
  All JavaScript code segments and includes for the scope as HTML tags.

@see drupal_add_js()
@see locale_js_alter()
@see drupal_js_defaults()
```

## Code

```php
function drupal_get_js($scope = 'header', $javascript = NULL, $skip_alter = FALSE) {
  if (!isset($javascript)) {
    $javascript = drupal_add_js();
  }

  // If no JavaScript items have been added, or if the only JavaScript items
  // that have been added are JavaScript settings (which don't do anything
  // without any JavaScript code to use them), then no JavaScript code should
  // be added to the page.
  if (empty($javascript) || (isset($javascript['settings']) && count($javascript) == 1)) {
    return '';
  }

  // Allow modules to alter the JavaScript.
  if (!$skip_alter) {
    drupal_alter('js', $javascript);
  }

  // Filter out elements of the given scope.
  $items = array();
  foreach ($javascript as $key => $item) {
    if ($item['scope'] == $scope) {
      $items[$key] = $item;
    }
  }

  // Sort the JavaScript so that it appears in the correct order.
  uasort($items, 'drupal_sort_css_js');

  // Provide the page with information about the individual JavaScript files
  // used, information not otherwise available when aggregation is enabled.
  $setting['ajaxPageState']['js'] = array_fill_keys(array_keys($items), 1);
  unset($setting['ajaxPageState']['js']['settings']);
  drupal_add_js($setting, 'setting');

  // If we're outputting the header scope, then this might be the final time
  // that drupal_get_js() is running, so add the setting to this output as well
  // as to the drupal_add_js() cache. If $items['settings'] doesn't exist, it's
  // because drupal_get_js() was intentionally passed a $javascript argument
  // stripped off settings, potentially in order to override how settings get
  // output, so in this case, do not add the setting to this output.
  if ($scope == 'header' && isset($items['settings'])) {
    $items['settings']['data'][] = $setting;
  }

  $elements = array(
    '#type' => 'scripts',
    '#items' => $items,
  );

  return drupal_render($elements);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
