# CommentContentRebuild::testCommentRebuild()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1826–1847 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1826-L1847)
- **Class:** [CommentContentRebuild](../CommentContentRebuild.md)
- **Module/theme:** comment

## Signature

```php
function testCommentRebuild()
```

## Documentation

```text
Test to ensure that the comment's content array is rebuilt for every
call to comment_view().
```

## Code

```php
  function testCommentRebuild() {
    // Update the comment settings so preview isn't required.
    $this->drupalLogin($this->admin_user);
    $this->setCommentSubject(TRUE);
    $this->setCommentPreview(DRUPAL_OPTIONAL);
    $this->drupalLogout();

    // Log in as the web user and add the comment.
    $this->drupalLogin($this->web_user);
    $subject_text = $this->randomName();
    $comment_text = $this->randomName();
    $comment = $this->postComment($this->node, $comment_text, $subject_text, TRUE);
    $comment_loaded = comment_load($comment->id);
    $this->assertTrue($this->commentExists($comment), 'Comment found.');

    // Add the property to the content array and then see if it still exists on build.
    $comment_loaded->content['test_property'] = array('#value' => $this->randomString());
    $built_content = comment_view($comment_loaded, $this->node);

    // This means that the content was rebuilt as the added test property no longer exists.
    $this->assertFalse(isset($built_content['test_property']), 'Comment content was emptied before being built.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
