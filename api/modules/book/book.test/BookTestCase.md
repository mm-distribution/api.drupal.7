# BookTestCase

- **Type:** Class
- **File:** [`modules/book/book.test`](_file.md), lines 11–398 · [local source](../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L11-L398)
- **Module/theme:** book

## Signature

```php
class BookTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the functionality of the Book module.
```

## Properties

### $book

```php
protected $book;
```

```text
A book node.

@var object
```

### $book_author

```php
protected $book_author;
```

```text
A user with permission to create and edit books.

@var object
```

### $web_user

```php
protected $web_user;
```

```text
A user with permission to view a book and access printer-friendly version.

@var object
```

### $admin_user

```php
protected $admin_user;
```

```text
A user with permission to create and edit books and to administer blocks.

@var object
```

## Methods (derived index)

- [getInfo()](BookTestCase/getInfo.md)
- [setUp()](BookTestCase/setUp.md)
- [createBook()](BookTestCase/createBook.md) — Creates a new book with a page hierarchy.
- [testBook()](BookTestCase/testBook.md) — Tests book functionality through node interfaces.
- [checkBookNode()](BookTestCase/checkBookNode.md) — Checks the outline of sub-pages; previous, up, and next.
- [generateOutlinePattern()](BookTestCase/generateOutlinePattern.md) — Creates a regular expression to check for the sub-nodes in the outline.
- [createBookNode()](BookTestCase/createBookNode.md) — Creates a book node.
- [testBookExport()](BookTestCase/testBookExport.md) — Tests book export ("printer-friendly version") functionality.
- [testBookNavigationBlock()](BookTestCase/testBookNavigationBlock.md) — Tests the functionality of the book navigation block.
- [testNavigationBlockOnAccessModuleEnabled()](BookTestCase/testNavigationBlockOnAccessModuleEnabled.md) — Tests the book navigation block when an access module is enabled.
- [testBookDelete()](BookTestCase/testBookDelete.md) — Tests the access for deleting top-level book nodes.

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
