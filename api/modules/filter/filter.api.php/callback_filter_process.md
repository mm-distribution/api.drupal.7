# callback_filter_process()

- **Type:** Function
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 236–240 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L236-L240)
- **Module/theme:** filter
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_filter_process($text, $filter, $format, $langcode, $cache, $cache_id)
```

## Documentation

```text
Provide text filtered to conform to the supplied format.

Callback for hook_filter_info().

See hook_filter_info() for a description of the filtering process. This step
is where the filter actually transforms the text.

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
  The filtered text.

@ingroup callbacks
```

## Code

```php
function callback_filter_process($text, $filter, $format, $langcode, $cache, $cache_id) {
  $text = preg_replace('|\[codefilter_code\](.+?)\[/codefilter_code\]|s', "<pre>$1</pre>", $text);

  return $text;
}
```

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
