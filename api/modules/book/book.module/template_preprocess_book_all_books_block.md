# template_preprocess_book_all_books_block()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1077–1084 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1077-L1084)
- **Module/theme:** book

## Signature

```php
function template_preprocess_book_all_books_block(&$variables)
```

## Documentation

```text
Processes variables for book-all-books-block.tpl.php.

All non-renderable elements are removed so that the template has full access
to the structured data but can also simply iterate over all elements and
render them (as in the default template).

@param $variables
  An associative array containing the following key:
  - book_menus

@see book-all-books-block.tpl.php
```

## Code

```php
function template_preprocess_book_all_books_block(&$variables) {
  // Remove all non-renderable elements.
  $elements = $variables['book_menus'];
  $variables['book_menus'] = array();
  foreach (element_children($elements) as $index) {
    $variables['book_menus'][$index] = $elements[$index];
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
