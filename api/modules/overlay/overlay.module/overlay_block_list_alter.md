# overlay_block_list_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 449–463 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L449-L463)
- **Module/theme:** overlay
- **Implements:** [hook_block_list_alter()](../../block/block.api.php/hook_block_list_alter.md)

## Signature

```php
function overlay_block_list_alter(&$blocks)
```

## Documentation

```text
Implements hook_block_list_alter().
```

## Code

```php
function overlay_block_list_alter(&$blocks) {
  // If we are limiting rendering to a subset of page regions, hide all blocks
  // which appear in regions not on that list. Note that overlay_page_alter()
  // does a more comprehensive job of preventing unwanted regions from being
  // displayed (regardless of whether they contain blocks or not), but the
  // reason for duplicating effort here is performance; we do not even want
  // these blocks to be built if they are not going to be displayed.
  if ($regions_to_render = overlay_get_regions_to_render()) {
    foreach ($blocks as $bid => $block) {
      if (!in_array($block->region, $regions_to_render)) {
        unset($blocks[$bid]);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
