# book_next()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 809–821 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L809-L821)
- **Module/theme:** book

## Signature

```php
function book_next($book_link)
```

## Documentation

```text
Fetches the menu link for the next page of the book.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  A fully loaded menu link for the page after the one represented in
  $book_link.
```

## Code

```php
function book_next($book_link) {
  $flat = book_get_flat_menu($book_link);
  reset($flat);
  do {
    $key = key($flat);
    next($flat);
  }
  while ($key && $key != $book_link['mlid']);

  if ($key == $book_link['mlid']) {
    return current($flat);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
