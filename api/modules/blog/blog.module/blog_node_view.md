# blog_node_view()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 80–96 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L80-L96)
- **Module/theme:** blog
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function blog_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function blog_node_view($node, $view_mode) {
  if ($view_mode != 'rss') {
    if ($node->type == 'blog' && (arg(0) != 'blog' || arg(1) != $node->uid)) {
      // This goes to l(), which escapes !username in both title and attributes.
      $links['blog_usernames_blog'] = array(
        'title' => t("!username's blog", array('!username' => format_username($node))),
        'href' => "blog/$node->uid",
        'attributes' => array('title' => t("Read !username's latest blog entries.", array('!username' => format_username($node)))),
      );
      $node->content['links']['blog'] = array(
        '#theme' => 'links__node__blog',
        '#links' => $links,
        '#attributes' => array('class' => array('links', 'inline')),
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
