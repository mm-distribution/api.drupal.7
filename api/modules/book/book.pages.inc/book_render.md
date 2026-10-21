# book_render()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 16–23 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L16-L23)
- **Module/theme:** book

## Signature

```php
function book_render()
```

## Documentation

```text
Menu callback: Prints a listing of all books.

@return string
  A HTML-formatted string with the listing of all books content.

@see book_menu()
```

## Code

```php
function book_render() {
  $book_list = array();
  foreach (book_get_books() as $book) {
    $book_list[] = l($book['title'], $book['href'], $book['options']);
  }

  return theme('item_list', array('items' => $book_list));
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
