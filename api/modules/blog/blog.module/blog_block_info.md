# blog_block_info()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 197–201 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L197-L201)
- **Module/theme:** blog
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function blog_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function blog_block_info() {
  $block['recent']['info'] = t('Recent blog posts');
  $block['recent']['properties']['administrative'] = TRUE;
  return $block;
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
