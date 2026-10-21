# BookTestCase::testNavigationBlockOnAccessModuleEnabled()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 335–372 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L335-L372)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function testNavigationBlockOnAccessModuleEnabled()
```

## Documentation

```text
Tests the book navigation block when an access module is enabled.
```

## Code

```php
   function testNavigationBlockOnAccessModuleEnabled() {
     $this->drupalLogin($this->admin_user);
     $edit = array();

     // Set the block title.
     $block_title = $this->randomName(16);
     $edit['title'] = $block_title;

     // Set block display to 'Show block only on book pages'.
     $edit['book_block_mode'] = 'book pages';
     $this->drupalPost('admin/structure/block/manage/book/navigation/configure', $edit, t('Save block'));
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

     // Create a book.
     $this->createBook();

     // Test correct display of the block to registered users.
     $this->drupalLogin($this->web_user);
     $this->drupalGet('node/' . $this->book->nid);
     $this->assertText($block_title, 'Book navigation block is displayed to registered users.');
     $this->drupalLogout();

     // Test correct display of the block to anonymous users.
     $this->drupalGet('node/' . $this->book->nid);
     $this->assertText($block_title, 'Book navigation block is displayed to anonymous users.');
   }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
