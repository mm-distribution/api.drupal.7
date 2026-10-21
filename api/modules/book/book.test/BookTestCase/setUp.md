# BookTestCase::setUp()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 49–59 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L49-L59)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('book', 'node_access_test'));

    // node_access_test requires a node_access_rebuild().
    node_access_rebuild();

    // Create users.
    $this->book_author = $this->drupalCreateUser(array('create new books', 'create book content', 'edit own book content', 'add content to books'));
    $this->web_user = $this->drupalCreateUser(array('access printer-friendly version', 'node test view'));
    $this->admin_user = $this->drupalCreateUser(array('create new books', 'create book content', 'edit own book content', 'add content to books', 'administer blocks', 'administer permissions', 'administer book outlines', 'node test view'));
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
