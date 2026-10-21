# blog_page_user_access()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 172–177 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L172-L177)
- **Module/theme:** blog

## Signature

```php
function blog_page_user_access($account)
```

## Documentation

```text
Access callback for user blog pages.
```

## Code

```php
function blog_page_user_access($account) {
  // The visitor must be able to access the site's content.
  // For a blog to 'exist' the user must either be able to
  // create new blog entries, or it must have existing posts.
  return $account->uid && user_access('access content') && (user_access('create blog content', $account) || _blog_post_exists($account));
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
