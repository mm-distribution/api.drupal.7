# BookTestCase::testBook()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 95–129 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L95-L129)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function testBook()
```

## Documentation

```text
Tests book functionality through node interfaces.
```

## Code

```php
  function testBook() {
    // Create new book.
    $nodes = $this->createBook();
    $book = $this->book;

    $this->drupalLogin($this->web_user);

    // Check that book pages display along with the correct outlines and
    // previous/next links.
    $this->checkBookNode($book, array($nodes[0], $nodes[3], $nodes[4]), FALSE, FALSE, $nodes[0]);
    $this->checkBookNode($nodes[0], array($nodes[1], $nodes[2]), $book, $book, $nodes[1], array($book));
    $this->checkBookNode($nodes[1], NULL, $nodes[0], $nodes[0], $nodes[2], array($book, $nodes[0]));
    $this->checkBookNode($nodes[2], NULL, $nodes[1], $nodes[0], $nodes[3], array($book, $nodes[0]));
    $this->checkBookNode($nodes[3], NULL, $nodes[2], $book, $nodes[4], array($book));
    $this->checkBookNode($nodes[4], NULL, $nodes[3], $book, FALSE, array($book));

    $this->drupalLogout();

    // Create a second book, and move an existing book page into it.
    $this->drupalLogin($this->book_author);
    $other_book = $this->createBookNode('new');
    $node = $this->createBookNode($book->nid);
    $edit = array('book[bid]' => $other_book->nid);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    $this->drupalLogout();
    $this->drupalLogin($this->web_user);

    // Check that the nodes in the second book are displayed correctly.
    // First we must set $this->book to the second book, so that the
    // correct regex will be generated for testing the outline.
    $this->book = $other_book;
    $this->checkBookNode($other_book, array($node), FALSE, FALSE, $node);
    $this->checkBookNode($node, NULL, $other_book, $other_book, FALSE, array($other_book));
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
