# BookTestCase::testBookExport()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 259–299 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L259-L299)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function testBookExport()
```

## Documentation

```text
Tests book export ("printer-friendly version") functionality.
```

## Code

```php
  function testBookExport() {
    // Create a book.
    $nodes = $this->createBook();

    // Login as web user and view printer-friendly version.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/' . $this->book->nid);
    $this->clickLink(t('Printer-friendly version'));

    // Make sure each part of the book is there.
    foreach ($nodes as $node) {
      $this->assertText($node->title, 'Node title found in printer friendly version.');
      $this->assertRaw(check_markup($node->body[LANGUAGE_NONE][0]['value'], $node->body[LANGUAGE_NONE][0]['format']), 'Node body found in printer friendly version.');
    }

    // Make sure we can't export an unsupported format.
    $this->drupalGet('book/export/foobar/' . $this->book->nid);
    $this->assertResponse('404', 'Unsupported export format returned "not found".');

    // Make sure we get a 404 on a not existing book node.
    $this->drupalGet('book/export/html/123');
    $this->assertResponse('404', 'Not existing book node returned "not found".');

    // Make sure an anonymous user cannot view printer-friendly version.
    $this->drupalLogout();

    // Load the book and verify there is no printer-friendly version link.
    $this->drupalGet('node/' . $this->book->nid);
    $this->assertNoLink(t('Printer-friendly version'), 'Anonymous user is not shown link to printer-friendly version.');

    // Try getting the URL directly, and verify it fails.
    $this->drupalGet('book/export/html/' . $this->book->nid);
    $this->assertResponse('403', 'Anonymous user properly forbidden.');

    // Now grant anonymous users permission to view the printer-friendly
    // version and verify that node access restrictions still prevent them from
    // seeing it.
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array('access printer-friendly version'));
    $this->drupalGet('book/export/html/' . $this->book->nid);
    $this->assertResponse('403', 'Anonymous user properly forbidden from seeing the printer-friendly version when denied by node access.');
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
