# book_menu_name()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 867–869 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L867-L869)
- **Module/theme:** book

## Signature

```php
function book_menu_name($bid)
```

## Documentation

```text
Generates the corresponding menu name from a book ID.

@param $bid
  The book ID for which to make a menu name.

@return
  The menu name.
```

## Code

```php
function book_menu_name($bid) {
  return 'book-toc-' . $bid;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
