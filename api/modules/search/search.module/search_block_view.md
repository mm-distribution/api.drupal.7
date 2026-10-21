# search_block_view()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 152–157 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L152-L157)
- **Module/theme:** search
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function search_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function search_block_view($delta = '') {
  if (user_access('search content')) {
    $block['content'] = drupal_get_form('search_block_form');
    return $block;
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
