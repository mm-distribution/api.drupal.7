# book_update_bid()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 692–706 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L692-L706)
- **Module/theme:** book

## Signature

```php
function book_update_bid($book_link)
```

## Documentation

```text
Updates the book ID of a page and its children when it moves to a new book.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.
```

## Code

```php
function book_update_bid($book_link) {
  $query = db_select('menu_links');
  $query->addField('menu_links', 'mlid');
  for ($i = 1; $i <= MENU_MAX_DEPTH && $book_link["p$i"]; $i++) {
    $query->condition("p$i", $book_link["p$i"]);
  }
  $mlids = $query->execute()->fetchCol();

  if ($mlids) {
    db_update('book')
      ->fields(array('bid' => $book_link['bid']))
      ->condition('mlid', $mlids, 'IN')
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
