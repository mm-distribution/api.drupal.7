# _blog_post_exists()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 182–192 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L182-L192)
- **Module/theme:** blog

## Signature

```php
function _blog_post_exists($account)
```

## Documentation

```text
Helper function to determine if a user has blog posts already.
```

## Code

```php
function _blog_post_exists($account) {
  return (bool)db_select('node', 'n')
    ->fields('n', array('nid'))
    ->condition('type', 'blog')
    ->condition('uid', $account->uid)
    ->condition('status', 1)
    ->range(0, 1)
    ->addTag('node_access')
    ->execute()
    ->fetchField();
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
