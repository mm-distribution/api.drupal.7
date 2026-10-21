# callback_filter_tips()

- **Type:** Function
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 264–271 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L264-L271)
- **Module/theme:** filter
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_filter_tips($filter, $format, $long)
```

## Documentation

```text
Return help text for a filter.

Callback for hook_filter_info().

A filter's tips should be informative and to the point. Short tips are
preferably one-liners.

@param $filter
  An object representing the filter.
@param $format
  An object representing the text format the filter is contained in.
@param $long
  Whether this callback should return a short tip to display in a form
  (FALSE), or whether a more elaborate filter tips should be returned for
  theme_filter_tips() (TRUE).

@return
  Translated text to display as a tip.

@ingroup callbacks
```

## Code

```php
function callback_filter_tips($filter, $format, $long) {
 if ($long) {
    return t('Lines and paragraphs are automatically recognized. The &lt;br /&gt; line break, &lt;p&gt; paragraph and &lt;/p&gt; close paragraph tags are inserted automatically. If paragraphs are not recognized simply add a couple blank lines.');
  }
  else {
    return t('Lines and paragraphs break automatically.');
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
