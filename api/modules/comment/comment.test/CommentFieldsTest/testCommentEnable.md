# CommentFieldsTest::testCommentEnable()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2154–2196 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2154-L2196)
- **Class:** [CommentFieldsTest](../CommentFieldsTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentEnable()
```

## Documentation

```text
Test that comment module works when enabled after a content module.
```

## Code

```php
  function testCommentEnable() {
    // Create a user to do module administration.
    $this->admin_user = $this->drupalCreateUser(array('access administration pages', 'administer modules'));
    $this->drupalLogin($this->admin_user);

    // Disable the comment module.
    $edit = array();
    $edit['modules[Core][comment][enable]'] = FALSE;
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->resetAll();
    $this->assertFalse(module_exists('comment'), 'Comment module disabled.');

    // Enable core content type modules (blog, book, and poll).
    $edit = array();
    $edit['modules[Core][blog][enable]'] = 'blog';
    $edit['modules[Core][book][enable]'] = 'book';
    $edit['modules[Core][poll][enable]'] = 'poll';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->resetAll();

    // Now enable the comment module.
    $edit = array();
    $edit['modules[Core][comment][enable]'] = 'comment';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->resetAll();
    $this->assertTrue(module_exists('comment'), 'Comment module enabled.');

    // Create nodes of each type.
    $blog_node = $this->drupalCreateNode(array('type' => 'blog'));
    $book_node = $this->drupalCreateNode(array('type' => 'book'));
    $poll_node = $this->drupalCreateNode(array('type' => 'poll', 'active' => 1, 'runtime' => 0, 'choice' => array(array('chtext' => ''))));

    $this->drupalLogout();

    // Try to post a comment on each node. A failure will be triggered if the
    // comment body is missing on one of these forms, due to postComment()
    // asserting that the body is actually posted correctly.
    $this->web_user = $this->drupalCreateUser(array('access content', 'access comments', 'post comments', 'skip comment approval'));
    $this->drupalLogin($this->web_user);
    $this->postComment($blog_node, $this->randomName(), $this->randomName());
    $this->postComment($book_node, $this->randomName(), $this->randomName());
    $this->postComment($poll_node, $this->randomName(), $this->randomName());
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
