# BookTestCase::createBook()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 64–90 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L64-L90)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function createBook()
```

## Documentation

```text
Creates a new book with a page hierarchy.
```

## Code

```php
  function createBook() {
    // Create new book.
    $this->drupalLogin($this->book_author);

    $this->book = $this->createBookNode('new');
    $book = $this->book;

    /*
     * Add page hierarchy to book.
     * Book
     *  |- Node 0
     *   |- Node 1
     *   |- Node 2
     *  |- Node 3
     *  |- Node 4
     */
    $nodes = array();
    $nodes[] = $this->createBookNode($book->nid); // Node 0.
    $nodes[] = $this->createBookNode($book->nid, $nodes[0]->book['mlid']); // Node 1.
    $nodes[] = $this->createBookNode($book->nid, $nodes[0]->book['mlid']); // Node 2.
    $nodes[] = $this->createBookNode($book->nid); // Node 3.
    $nodes[] = $this->createBookNode($book->nid); // Node 4.

    $this->drupalLogout();

    return $nodes;
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
