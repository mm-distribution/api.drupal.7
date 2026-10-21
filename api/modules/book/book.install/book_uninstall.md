# book_uninstall()

- **Type:** Function
- **File:** [`modules/book/book.install`](_file.md), lines 19–29 · [local source](../../../../source/modules/book/book.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install#L19-L29)
- **Module/theme:** book
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function book_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function book_uninstall() {
  variable_del('book_allowed_types');
  variable_del('book_child_type');
  variable_del('book_block_mode');

  // Delete menu links.
  db_delete('menu_links')
    ->condition('module', 'book')
    ->execute();
  menu_cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/book/book.install](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install) · Licensed GPL-2.0-or-later (see LICENSE)._
