# callback_filter_prepare()

- **Type:** Function
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 203–207 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L203-L207)
- **Module/theme:** filter
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_filter_prepare($text, $filter, $format, $langcode, $cache, $cache_id)
```

## Documentation

```text
Provide prepared text with special characters escaped.

Callback for hook_filter_info().

See hook_filter_info() for a description of the filtering process. Filters
should not use the 'prepare callback' step for anything other than escaping,
because that would short-circuit the control the user has over the order in
which filters are applied.

@param $text
  The text string to be filtered.
@param $filter
  The filter object containing settings for the given format.
@param $format
  The text format object assigned to the text to be filtered.
@param $langcode
  The language code of the text to be filtered.
@param $cache
  A Boolean indicating whether the filtered text is going to be cached in
  {cache_filter}.
@param $cache_id
  The ID of the filtered text in {cache_filter}, if $cache is TRUE.

@return
  The prepared, escaped text.

@ingroup callbacks
```

## Code

```php
function callback_filter_prepare($text, $filter, $format, $langcode, $cache, $cache_id) {
  // Escape <code> and </code> tags.
  $text = preg_replace('|<code>(.+?)</code>|s', "[codefilter_code]$1[/codefilter_code]", $text);
  return $text;
}
```

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
