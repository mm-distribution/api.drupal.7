# BookTestCase::createBookNode()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 227–254 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L227-L254)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function createBookNode($book_nid, $parent = NULL)
```

## Documentation

```text
Creates a book node.

@param $book_nid
  A book node ID or set to 'new' to create a new book.
@param $parent
  (optional) Parent book reference ID. Defaults to NULL.
```

## Code

```php
  function createBookNode($book_nid, $parent = NULL) {
    // $number does not use drupal_static as it should not be reset
    // since it uniquely identifies each call to createBookNode().
    static $number = 0; // Used to ensure that when sorted nodes stay in same order.

    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $number . ' - SimpleTest test node ' . $this->randomName(10);
    $edit["body[$langcode][0][value]"] = 'SimpleTest test body ' . $this->randomName(32) . ' ' . $this->randomName(32);
    $edit['book[bid]'] = $book_nid;

    if ($parent !== NULL) {
      $this->drupalPost('node/add/book', $edit, t('Change book (update list of parents)'));

      $edit['book[plid]'] = $parent;
      $this->drupalPost(NULL, $edit, t('Save'));
    }
    else {
      $this->drupalPost('node/add/book', $edit, t('Save'));
    }

    // Check to make sure the book node was created.
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertNotNull(($node === FALSE ? NULL : $node), 'Book node found in database.');
    $number++;

    return $node;
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
