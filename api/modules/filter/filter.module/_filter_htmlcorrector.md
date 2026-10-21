# _filter_htmlcorrector()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1712–1714 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1712-L1714)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_htmlcorrector($text)
```

## Documentation

```text
Implements callback_filter_process().

Scans the input and makes sure that HTML tags are properly closed.
```

## Code

```php
function _filter_htmlcorrector($text) {
  return filter_dom_serialize(filter_dom_load($text));
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
