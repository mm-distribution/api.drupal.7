# blog_block_save()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 221–225 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L221-L225)
- **Module/theme:** blog
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function blog_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function blog_block_save($delta = '', $edit = array()) {
  if ($delta == 'recent') {
    variable_set('blog_block_count', $edit['blog_block_count']);
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
