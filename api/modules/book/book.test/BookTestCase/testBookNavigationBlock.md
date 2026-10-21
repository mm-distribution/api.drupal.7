# BookTestCase::testBookNavigationBlock()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 304–330 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L304-L330)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function testBookNavigationBlock()
```

## Documentation

```text
Tests the functionality of the book navigation block.
```

## Code

```php
  function testBookNavigationBlock() {
    $this->drupalLogin($this->admin_user);

    // Set block title to confirm that the interface is available.
    $block_title = $this->randomName(16);
    $this->drupalPost('admin/structure/block/manage/book/navigation/configure', array('title' => $block_title), t('Save block'));
    $this->assertText(t('The block configuration has been saved.'), 'Block configuration set.');

    // Set the block to a region to confirm block is available.
    $edit = array();
    $edit['blocks[book_navigation][region]'] = 'footer';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), 'Block successfully move to footer region.');

     // Give anonymous users the permission 'node test view'.
     $edit = array();
     $edit[DRUPAL_ANONYMOUS_RID . '[node test view]'] = TRUE;
     $this->drupalPost('admin/people/permissions/' . DRUPAL_ANONYMOUS_RID, $edit, t('Save permissions'));
     $this->assertText(t('The changes have been saved.'), "Permission 'node test view' successfully assigned to anonymous users.");

    // Test correct display of the block.
    $nodes = $this->createBook();
    $this->drupalGet('<front>');
    $this->assertText($block_title, 'Book navigation block is displayed.');
    $this->assertText($this->book->title, format_string('Link to book root (@title) is displayed.', array('@title' => $nodes[0]->title)));
    $this->assertNoText($nodes[0]->title, 'No links to individual book pages are displayed.');
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
