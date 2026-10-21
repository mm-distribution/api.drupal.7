# forum_block_save()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 675–677 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L675-L677)
- **Module/theme:** forum
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function forum_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function forum_block_save($delta = '', $edit = array()) {
  variable_set('forum_block_num_' . $delta, $edit['forum_block_num_' . $delta]);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
