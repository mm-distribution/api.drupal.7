# _filter_tips()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1063–1090 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1063-L1090)
- **Module/theme:** filter

## Signature

```php
function _filter_tips($format_id, $long = FALSE)
```

## Documentation

```text
Retrieves the filter tips.

@param $format_id
  The ID of the text format for which to retrieve tips, or -1 to return tips
  for all formats accessible to the current user.
@param $long
  (optional) Boolean indicating whether the long form of tips should be
  returned. Defaults to FALSE.

@return
  An associative array of filtering tips, keyed by filter name. Each
  filtering tip is an associative array with elements:
  - tip: Tip text.
  - id: Filter ID.
```

## Code

```php
function _filter_tips($format_id, $long = FALSE) {
  global $user;

  $formats = filter_formats($user);
  $filter_info = filter_get_filters();

  $tips = array();

  // If only listing one format, extract it from the $formats array.
  if ($format_id != -1) {
    $formats = array($formats[$format_id]);
  }

  foreach ($formats as $format) {
    $filters = filter_list_format($format->format);
    $tips[$format->name] = array();
    foreach ($filters as $name => $filter) {
      if ($filter->status && isset($filter_info[$name]['tips callback']) && function_exists($filter_info[$name]['tips callback'])) {
        $tip = $filter_info[$name]['tips callback']($filter, $format, $long);
        if (isset($tip)) {
          $tips[$format->name][$name] = array('tip' => $tip, 'id' => $name);
        }
      }
    }
  }

  return $tips;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
