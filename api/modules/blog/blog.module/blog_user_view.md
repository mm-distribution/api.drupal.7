# blog_user_view()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 24–34 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L24-L34)
- **Module/theme:** blog
- **Implements:** [hook_user_view()](../../user/user.api.php/hook_user_view.md)

## Signature

```php
function blog_user_view($account)
```

## Documentation

```text
Implements hook_user_view().
```

## Code

```php
function blog_user_view($account) {
  if (user_access('create blog content', $account)) {
    $account->content['summary']['blog'] =  array(
      '#type' => 'user_profile_item',
      '#title' => t('Blog'),
      // l() escapes the attributes, so we should not escape !username here.
      '#markup' => l(t('View recent blog entries'), "blog/$account->uid", array('attributes' => array('title' => t("Read !username's latest blog entries.", array('!username' => format_username($account)))))),
      '#attributes' => array('class' => array('blog')),
    );
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
