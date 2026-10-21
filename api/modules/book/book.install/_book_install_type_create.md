# _book_install_type_create()

- **Type:** Function
- **File:** [`modules/book/book.install`](_file.md), lines 34–54 · [local source](../../../../source/modules/book/book.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install#L34-L54)
- **Module/theme:** book

## Signature

```php
function _book_install_type_create()
```

## Documentation

```text
Creates the book content type.
```

## Code

```php
function _book_install_type_create() {
  // Create an additional node type.
  $book_node_type = array(
    'type' => 'book',
    'name' => t('Book page'),
    'base' => 'node_content',
    'description' => t('<em>Books</em> have a built-in hierarchical navigation. Use for handbooks or tutorials.'),
    'custom' => 1,
    'modified' => 1,
    'locked' => 0,
  );

  $book_node_type = node_type_set_defaults($book_node_type);
  node_type_save($book_node_type);
  node_add_body_field($book_node_type);
  // Default to not promoted.
  variable_set('node_options_book', array('status'));
  // Use this default type for adding content to books.
  variable_set('book_allowed_types', array('book'));
  variable_set('book_child_type', 'book');
}
```

---
_Drupal 7.103 · [modules/book/book.install](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install) · Licensed GPL-2.0-or-later (see LICENSE)._
