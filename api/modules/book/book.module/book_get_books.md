# book_get_books()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 380–410 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L380-L410)
- **Module/theme:** book

## Signature

```php
function book_get_books()
```

## Documentation

```text
Returns an array of all books.

This list may be used for generating a list of all the books, or for building
the options for a form select.

@return
  An array of all books.
```

## Code

```php
function book_get_books() {
  $all_books = &drupal_static(__FUNCTION__);

  if (!isset($all_books)) {
    $all_books = array();
    $nids = db_query("SELECT DISTINCT(bid) FROM {book}")->fetchCol();

    if ($nids) {
      $query = db_select('book', 'b', array('fetch' => PDO::FETCH_ASSOC));
      $query->join('node', 'n', 'b.nid = n.nid');
      $query->join('menu_links', 'ml', 'b.mlid = ml.mlid');
      $query->addField('n', 'type', 'type');
      $query->addField('n', 'title', 'title');
      $query->fields('b');
      $query->fields('ml');
      $query->condition('n.nid', $nids, 'IN');
      $query->condition('n.status', 1);
      $query->orderBy('ml.weight');
      $query->orderBy('ml.link_title');
      $query->addTag('node_access');
      $result2 = $query->execute();
      foreach ($result2 as $link) {
        $link['href'] = $link['link_path'];
        $link['options'] = unserialize($link['options']);
        $all_books[$link['bid']] = $link;
      }
    }
  }

  return $all_books;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
