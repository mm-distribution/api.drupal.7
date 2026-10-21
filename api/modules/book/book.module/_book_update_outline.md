# _book_update_outline()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 626–684 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L626-L684)
- **Module/theme:** book

## Signature

```php
function _book_update_outline($node)
```

## Documentation

```text
Handles additions and updates to the book outline.

This common helper function performs all additions and updates to the book
outline through node addition, node editing, node deletion, or the outline
tab.

@param $node
  The node that is being saved, added, deleted, or moved.

@return
  TRUE if the menu link was saved; FALSE otherwise.
```

## Code

```php
function _book_update_outline($node) {
  if (empty($node->book['bid'])) {
    return FALSE;
  }
  $new = empty($node->book['mlid']);

  $node->book['link_path'] = 'node/' . $node->nid;
  $node->book['link_title'] = $node->title;
  $node->book['parent_mismatch'] = FALSE; // The normal case.

  if ($node->book['bid'] == $node->nid) {
    $node->book['plid'] = 0;
    $node->book['menu_name'] = book_menu_name($node->nid);
  }
  else {
    // Check in case the parent is not is this book; the book takes precedence.
    if (!empty($node->book['plid'])) {
      $parent = db_query("SELECT * FROM {book} WHERE mlid = :mlid", array(
        ':mlid' => $node->book['plid'],
      ))->fetchAssoc();
    }
    if (empty($node->book['plid']) || !$parent || $parent['bid'] != $node->book['bid']) {
      $node->book['plid'] = db_query("SELECT mlid FROM {book} WHERE nid = :nid", array(
        ':nid' => $node->book['bid'],
      ))->fetchField();
      $node->book['parent_mismatch'] = TRUE; // Likely when JS is disabled.
    }
  }

  if (menu_link_save($node->book)) {
    if ($new) {
      // Insert new.
      db_insert('book')
        ->fields(array(
          'nid' => $node->nid,
          'mlid' => $node->book['mlid'],
          'bid' => $node->book['bid'],
        ))
        ->execute();
      // Reset the cache of stored books.
      drupal_static_reset('book_get_books');
    }
    else {
      if ($node->book['bid'] != db_query("SELECT bid FROM {book} WHERE nid = :nid", array(
          ':nid' => $node->nid,
        ))->fetchField()) {
        // Update the bid for this page and all children.
        book_update_bid($node->book);
        // Reset the cache of stored books.
        drupal_static_reset('book_get_books');
      }
    }

    return TRUE;
  }

  // Failed to save the menu link.
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
