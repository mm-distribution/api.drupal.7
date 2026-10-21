# filter_format_save()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 206–286 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L206-L286)
- **Module/theme:** filter

## Signature

```php
function filter_format_save($format)
```

## Documentation

```text
Saves a text format object to the database.

@param $format
  A format object having the properties:
  - format: A machine-readable name representing the ID of the text format
    to save. If this corresponds to an existing text format, that format
    will be updated; otherwise, a new format will be created.
  - name: The title of the text format.
  - status: (optional) An integer indicating whether the text format is
    enabled (1) or not (0). Defaults to 1.
  - weight: (optional) The weight of the text format, which controls its
    placement in text format lists. If omitted, the weight is set to 0.
  - filters: (optional) An associative, multi-dimensional array of filters
    assigned to the text format, keyed by the name of each filter and using
    the properties:
    - weight: (optional) The weight of the filter in the text format. If
      omitted, either the currently stored weight is retained (if there is
      one), or the filter is assigned a weight of 10, which will usually
      put it at the bottom of the list.
    - status: (optional) A boolean indicating whether the filter is
      enabled in the text format. If omitted, the filter will be disabled.
    - settings: (optional) An array of configured settings for the filter.
      See hook_filter_info() for details.

@return
  SAVED_NEW or SAVED_UPDATED.
```

## Code

```php
function filter_format_save($format) {
  $format->name = trim($format->name);
  $format->cache = _filter_format_is_cacheable($format);
  if (!isset($format->status)) {
    $format->status = 1;
  }
  if (!isset($format->weight)) {
    $format->weight = 0;
  }

  // Insert or update the text format.
  $return = db_merge('filter_format')
    ->key(array('format' => $format->format))
    ->fields(array(
      'name' => $format->name,
      'cache' => (int) $format->cache,
      'status' => (int) $format->status,
      'weight' => (int) $format->weight,
    ))
    ->execute();

  // Programmatic saves may not contain any filters.
  if (!isset($format->filters)) {
    $format->filters = array();
  }
  $filter_info = filter_get_filters();
  foreach ($filter_info as $name => $filter) {
    // If the format does not specify an explicit weight for a filter, assign
    // a default weight, either defined in hook_filter_info(), or the default of
    // 0 by filter_get_filters()
    if (!isset($format->filters[$name]['weight'])) {
      $format->filters[$name]['weight'] = $filter['weight'];
    }
    $format->filters[$name]['status'] = isset($format->filters[$name]['status']) ? $format->filters[$name]['status'] : 0;
    $format->filters[$name]['module'] = $filter['module'];

    // If settings were passed, only ensure default settings.
    if (isset($format->filters[$name]['settings'])) {
      if (isset($filter['default settings'])) {
        $format->filters[$name]['settings'] = array_merge($filter['default settings'], $format->filters[$name]['settings']);
      }
    }
    // Otherwise, use default settings or fall back to an empty array.
    else {
      $format->filters[$name]['settings'] = isset($filter['default settings']) ? $filter['default settings'] : array();
    }

    $fields = array();
    $fields['weight'] = $format->filters[$name]['weight'];
    $fields['status'] = $format->filters[$name]['status'];
    $fields['module'] = $format->filters[$name]['module'];
    $fields['settings'] = serialize($format->filters[$name]['settings']);

    db_merge('filter')
      ->key(array(
        'format' => $format->format,
        'name' => $name,
      ))
      ->fields($fields)
      ->execute();
  }

  if ($return == SAVED_NEW) {
    module_invoke_all('filter_format_insert', $format);
  }
  else {
    module_invoke_all('filter_format_update', $format);
    // Explicitly indicate that the format was updated. We need to do this
    // since if the filters were updated but the format object itself was not,
    // the merge query above would not return an indication that anything had
    // changed.
    $return = SAVED_UPDATED;

    // Clear the filter cache whenever a text format is updated.
    cache_clear_all($format->format . ':', 'cache_filter', TRUE);
  }

  filter_formats_reset();

  return $return;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
