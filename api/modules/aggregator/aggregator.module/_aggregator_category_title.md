# _aggregator_category_title()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 277–279 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L277-L279)
- **Module/theme:** aggregator

## Signature

```php
function _aggregator_category_title($category)
```

## Documentation

```text
Title callback: Returns a title for aggregator category pages.

@param $category
  An aggregator category.

@return
  A string with the aggregator category title.
```

## Code

```php
function _aggregator_category_title($category) {
  return $category['title'];
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
