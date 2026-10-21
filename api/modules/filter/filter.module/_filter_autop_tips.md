# _filter_autop_tips()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1792–1799 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1792-L1799)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_autop_tips($filter, $format, $long = FALSE)
```

## Documentation

```text
Implements callback_filter_tips().

Provides help for the auto-paragraph filter.

@see filter_filter_info()
```

## Code

```php
function _filter_autop_tips($filter, $format, $long = FALSE) {
  if ($long) {
    return t('Lines and paragraphs are automatically recognized. The &lt;br /&gt; line break, &lt;p&gt; paragraph and &lt;/p&gt; close paragraph tags are inserted automatically. If paragraphs are not recognized simply add a couple blank lines.');
  }
  else {
    return t('Lines and paragraphs break automatically.');
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
