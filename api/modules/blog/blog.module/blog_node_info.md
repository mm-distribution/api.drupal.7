# blog_node_info()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 11–19 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L11-L19)
- **Module/theme:** blog
- **Implements:** [hook_node_info()](../../node/node.api.php/hook_node_info.md)

## Signature

```php
function blog_node_info()
```

## Documentation

```text
Implements hook_node_info().
```

## Code

```php
function blog_node_info() {
  return array(
    'blog' => array(
      'name' => t('Blog entry'),
      'base' => 'blog',
      'description' => t('Use for multi-user blogs. Every user gets a personal blog.'),
    )
  );
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
