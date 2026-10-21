# filter_list_format()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 698–735 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L698-L735)
- **Module/theme:** filter

## Signature

```php
function filter_list_format($format_id)
```

## Documentation

```text
Retrieves a list of filters for a given text format.

Note that this function returns all associated filters regardless of whether
they are enabled or disabled. All functions working with the filter
information outside of filter administration should test for $filter->status
before performing actions with the filter.

@param $format_id
  The format ID to retrieve filters for.

@return
  An array of filter objects associated to the given text format, keyed by
  filter name.
```

## Code

```php
function filter_list_format($format_id) {
  $filters = &drupal_static(__FUNCTION__, array());
  $filter_info = filter_get_filters();

  if (!isset($filters['all'])) {
    if ($cache = cache_get('filter_list_format')) {
      $filters['all'] = $cache->data;
    }
    else {
      $result = db_query('SELECT * FROM {filter} ORDER BY weight, module, name');
      foreach ($result as $record) {
        $filters['all'][$record->format][$record->name] = $record;
      }
      cache_set('filter_list_format', $filters['all']);
    }
  }

  if (!isset($filters[$format_id])) {
    $format_filters = array();
    $filter_map = isset($filters['all'][$format_id]) ? $filters['all'][$format_id] : array();
    foreach ($filter_map as $name => $filter) {
      if (isset($filter_info[$name])) {
        $filter->title = $filter_info[$name]['title'];
        // Unpack stored filter settings.
        $filter->settings = (isset($filter->settings) ? unserialize($filter->settings) : array());
        // Merge in default settings.
        if (isset($filter_info[$name]['default settings'])) {
          $filter->settings += $filter_info[$name]['default settings'];
        }

        $format_filters[$name] = $filter;
      }
    }
    $filters[$format_id] = $format_filters;
  }

  return isset($filters[$format_id]) ? $filters[$format_id] : array();
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
