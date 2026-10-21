# check_markup()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 766–821 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L766-L821)
- **Module/theme:** filter
- **Topics:** [sanitization](../../../topics/sanitization.md)

## Signature

```php
function check_markup($text, $format_id = NULL, $langcode = '', $cache = FALSE)
```

## Documentation

```text
Runs all the enabled filters on a piece of text.

Note: Because filters can inject JavaScript or execute PHP code, security is
vital here. When a user supplies a text format, you should validate it using
filter_access() before accepting/using it. This is normally done in the
validation stage of the Form API. You should for example never make a preview
of content in a disallowed format.

@param $text
  The text to be filtered.
@param $format_id
  (optional) The machine name of the filter format to be used to filter the
  text. Defaults to the fallback format. See filter_fallback_format().
@param $langcode
  (optional) The language code of the text to be filtered, e.g. 'en' for
  English. This allows filters to be language aware so language specific
  text replacement can be implemented. Defaults to an empty string.
@param $cache
  (optional) A Boolean indicating whether to cache the filtered output in the
  {cache_filter} table. The caller may set this to FALSE when the output is
  already cached elsewhere to avoid duplicate cache lookups and storage.
  Defaults to FALSE.

@return
  The filtered text.

@ingroup sanitization
```

## Code

```php
function check_markup($text, $format_id = NULL, $langcode = '', $cache = FALSE) {
  if (!isset($format_id)) {
    $format_id = filter_fallback_format();
  }
  // If the requested text format does not exist, the text cannot be filtered.
  if (!$format = filter_format_load($format_id)) {
    watchdog('filter', 'Missing text format: %format.', array('%format' => $format_id), WATCHDOG_ALERT);
    return '';
  }

  $text = (string) $text;

  // Check for a cached version of this piece of text.
  $cache = $cache && !empty($format->cache);
  $cache_id = '';
  if ($cache) {
    $cache_id = $format->format . ':' . $langcode . ':' . hash('sha256', $text);
    if ($cached = cache_get($cache_id, 'cache_filter')) {
      return $cached->data;
    }
  }

  // Convert all Windows and Mac newlines to a single newline, so filters only
  // need to deal with one possibility.
  $text = str_replace(array("\r\n", "\r"), "\n", $text);

  // Get a complete list of filters, ordered properly.
  $filters = filter_list_format($format->format);
  $filter_info = filter_get_filters();

  // Give filters the chance to escape HTML-like data such as code or formulas.
  foreach ($filters as $name => $filter) {
    if ($filter->status && isset($filter_info[$name]['prepare callback']) && function_exists($filter_info[$name]['prepare callback'])) {
      $function = $filter_info[$name]['prepare callback'];
      $text = $function($text, $filter, $format, $langcode, $cache, $cache_id);
    }
  }

  // Perform filtering.
  foreach ($filters as $name => $filter) {
    if ($filter->status && isset($filter_info[$name]['process callback']) && function_exists($filter_info[$name]['process callback'])) {
      $function = $filter_info[$name]['process callback'];
      $text = $function($text, $filter, $format, $langcode, $cache, $cache_id);
    }
  }

  // Cache the filtered text. This cache is infinitely valid. It becomes
  // obsolete when $text changes (which leads to a new $cache_id). It is
  // automatically flushed when the text format is updated.
  // @see filter_format_save()
  if ($cache) {
    cache_set($cache_id, $text, 'cache_filter');
  }

  return $text;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
