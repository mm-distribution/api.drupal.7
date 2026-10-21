# book_admin_paths()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 235–243 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L235-L243)
- **Module/theme:** book
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function book_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function book_admin_paths() {
  if (variable_get('node_admin_theme')) {
    $paths = array(
      'node/*/outline' => TRUE,
      'node/*/outline/remove' => TRUE,
    );
    return $paths;
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
