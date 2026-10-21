# BookTestCase::testBookDelete()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 377–397 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L377-L397)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function testBookDelete()
```

## Documentation

```text
Tests the access for deleting top-level book nodes.
```

## Code

```php
   function testBookDelete() {
     $nodes = $this->createBook();
     $this->drupalLogin($this->admin_user);
     $edit = array();

     // Test access to delete top-level and child book nodes.
     $this->drupalGet('node/' . $this->book->nid . '/outline/remove');
     $this->assertResponse('403', 'Deleting top-level book node properly forbidden.');
     $this->drupalPost('node/' . $nodes[4]->nid . '/outline/remove', $edit, t('Remove'));
     $node4 = node_load($nodes[4]->nid, NULL, TRUE);
     $this->assertTrue(empty($node4->book), 'Deleting child book node properly allowed.');

     // Delete all child book nodes and retest top-level node deletion.
     foreach ($nodes as $node) {
       $nids[] = $node->nid;
     }
     node_delete_multiple($nids);
     $this->drupalPost('node/' . $this->book->nid . '/outline/remove', $edit, t('Remove'));
     $node = node_load($this->book->nid, NULL, TRUE);
     $this->assertTrue(empty($node->book), 'Deleting childless top-level book node properly allowed.');
   }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
