# _filter_url_parse_partial_links()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1629–1637 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1629-L1637)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url_parse_partial_links($match)
```

## Documentation

```text
Makes links out of domain names starting with "www."

Callback for preg_replace_callback() within _filter_url().
```

## Code

```php
function _filter_url_parse_partial_links($match) {
  // The $i:th parenthesis in the regexp contains the URL.
  $i = 1;

  $match[$i] = decode_entities($match[$i]);
  $caption = check_plain(_filter_url_trim($match[$i]));
  $match[$i] = check_plain($match[$i]);
  return '<a href="http://' . $match[$i] . '">' . $caption . '</a>' . $match[$i + 1];
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
