# blog_install()

- **Type:** Function
- **File:** [`modules/blog/blog.install`](_file.md), lines 11–16 · [local source](../../../../source/modules/blog/blog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.install#L11-L16)
- **Module/theme:** blog
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function blog_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function blog_install() {
  // Ensure the blog node type is available.
  node_types_rebuild();
  $types = node_type_get_types();
  node_add_body_field($types['blog']);
}
```

---
_Drupal 7.103 · [modules/blog/blog.install](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
