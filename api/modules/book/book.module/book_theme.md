# book_theme()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 38–63 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L38-L63)
- **Module/theme:** book
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function book_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function book_theme() {
  return array(
    'book_navigation' => array(
      'variables' => array('book_link' => NULL),
      'template' => 'book-navigation',
    ),
    'book_export_html' => array(
      'variables' => array('title' => NULL, 'contents' => NULL, 'depth' => NULL),
      'template' => 'book-export-html',
    ),
    'book_admin_table' => array(
      'render element' => 'form',
    ),
    'book_title_link' => array(
      'variables' => array('link' => NULL),
    ),
    'book_all_books_block' => array(
      'render element' => 'book_menus',
      'template' => 'book-all-books-block',
    ),
    'book_node_export_html' => array(
      'variables' => array('node' => NULL, 'children' => NULL),
      'template' => 'book-node-export-html',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
