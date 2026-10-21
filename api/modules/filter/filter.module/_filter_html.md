# _filter_html()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1305–1319 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1305-L1319)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_html($text, $filter)
```

## Documentation

```text
Implements callback_filter_process().

Provides filtering of input into accepted HTML.
```

## Code

```php
function _filter_html($text, $filter) {
  $allowed_tags = preg_split('/\s+|<|>/', $filter->settings['allowed_html'], -1, PREG_SPLIT_NO_EMPTY);
  $text = filter_xss($text, $allowed_tags);

  if ($filter->settings['filter_html_nofollow']) {
    $html_dom = filter_dom_load($text);
    $links = $html_dom->getElementsByTagName('a');
    foreach ($links as $link) {
      $link->setAttribute('rel', 'nofollow');
    }
    $text = filter_dom_serialize($html_dom);
  }

  return trim($text);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
