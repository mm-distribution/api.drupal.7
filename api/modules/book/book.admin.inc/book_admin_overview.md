# book_admin_overview()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 16–27 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L16-L27)
- **Module/theme:** book

## Signature

```php
function book_admin_overview()
```

## Documentation

```text
Returns an administrative overview of all books.

@return string
  A HTML-formatted string with the administrative page content.

@see book_menu()
```

## Code

```php
function book_admin_overview() {
  $rows = array();

  $headers = array(t('Book'), t('Operations'));

  // Add any recognized books to the table list.
  foreach (book_get_books() as $book) {
    $rows[] = array(l($book['title'], $book['href'], $book['options']), l(t('edit order and titles'), 'admin/content/book/' . $book['nid']));
  }

  return theme('table', array('header' => $headers, 'rows' => $rows, 'empty' => t('No books available.')));
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
