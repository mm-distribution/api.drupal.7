# comment_block_save()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 445–447 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L445-L447)
- **Module/theme:** comment
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function comment_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function comment_block_save($delta = '', $edit = array()) {
  variable_set('comment_block_count', (int) $edit['comment_block_count']);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
