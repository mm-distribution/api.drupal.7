# blog_uninstall()

- **Type:** Function
- **File:** [`modules/blog/blog.install`](_file.md), lines 21–23 · [local source](../../../../source/modules/blog/blog.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.install#L21-L23)
- **Module/theme:** blog
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function blog_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function blog_uninstall() {
  variable_del('blog_block_count');
}
```

---
_Drupal 7.103 · [modules/blog/blog.install](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.install) · Licensed GPL-2.0-or-later (see LICENSE)._
