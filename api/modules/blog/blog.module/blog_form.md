# blog_form()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 62–64 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L62-L64)
- **Module/theme:** blog
- **Implements:** [hook_form()](../../node/node.api.php/hook_form.md)

## Signature

```php
function blog_form($node, $form_state)
```

## Documentation

```text
Implements hook_form().
```

## Code

```php
function blog_form($node, $form_state) {
  return node_content_form($node, $form_state);
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
