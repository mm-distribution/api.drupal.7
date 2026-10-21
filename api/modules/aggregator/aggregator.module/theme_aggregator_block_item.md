# theme_aggregator_block_item()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 728–731 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L728-L731)
- **Module/theme:** aggregator
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_aggregator_block_item($variables)
```

## Documentation

```text
Returns HTML for an individual feed item for display in the block.

@param $variables
  An associative array containing:
  - item: The item to be displayed.
  - feed: Not used.

@ingroup themeable
```

## Code

```php
function theme_aggregator_block_item($variables) {
  // Display the external link to the item.
  return '<a href="' . check_url($variables['item']->link) . '">' . check_plain($variables['item']->title) . "</a>\n";
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
