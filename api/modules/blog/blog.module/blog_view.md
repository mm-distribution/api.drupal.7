# blog_view()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 69–75 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L69-L75)
- **Module/theme:** blog
- **Implements:** [hook_view()](../../node/node.api.php/hook_view.md)

## Signature

```php
function blog_view($node, $view_mode)
```

## Documentation

```text
Implements hook_view().
```

## Code

```php
function blog_view($node, $view_mode) {
  if ($view_mode == 'full' && node_is_page($node)) {
    // Breadcrumb navigation.  l() escapes title, so we should not escape !name.
    drupal_set_breadcrumb(array(l(t('Home'), NULL), l(t('Blogs'), 'blog'), l(t("!name's blog", array('!name' => format_username($node))), 'blog/' . $node->uid)));
  }
  return $node;
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
