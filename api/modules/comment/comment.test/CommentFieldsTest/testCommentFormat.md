# CommentFieldsTest::testCommentFormat()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2201–2211 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2201-L2211)
- **Class:** [CommentFieldsTest](../CommentFieldsTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentFormat()
```

## Documentation

```text
Test that comment module works correctly with plain text format.
```

## Code

```php
  function testCommentFormat() {
    // Disable text processing for comments.
    $this->drupalLogin($this->admin_user);
    $edit = array('instance[settings][text_processing]' => 0);
    $this->drupalPost('admin/structure/types/manage/article/comment/fields/comment_body', $edit, t('Save settings'));

    // Post a comment without an explicit subject.
    $this->drupalLogin($this->web_user);
    $edit = array('comment_body[und][0][value]' => $this->randomName(8));
    $this->drupalPost('node/' . $this->node->nid, $edit, t('Save'));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
