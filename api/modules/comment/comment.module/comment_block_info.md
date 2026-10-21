# comment_block_info()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 421–426 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L421-L426)
- **Module/theme:** comment
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function comment_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function comment_block_info() {
  $blocks['recent']['info'] = t('Recent comments');
  $blocks['recent']['properties']['administrative'] = TRUE;

  return $blocks;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
