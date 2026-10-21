# CommentHelperCase::performCommentOperation()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 234–247 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L234-L247)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function performCommentOperation($comment, $operation, $approval = FALSE)
```

## Documentation

```text
Perform the specified operation on the specified comment.

@param object $comment
  Comment to perform operation on.
@param string $operation
  Operation to perform.
@param boolean $aproval
  Operation is found on approval page.
```

## Code

```php
  function performCommentOperation($comment, $operation, $approval = FALSE) {
    $edit = array();
    $edit['operation'] = $operation;
    $edit['comments[' . $comment->id . ']'] = TRUE;
    $this->drupalPost('admin/content/comment' . ($approval ? '/approval' : ''), $edit, t('Update'));

    if ($operation == 'delete') {
      $this->drupalPost(NULL, array(), t('Delete comments'));
      $this->assertRaw(format_plural(1, 'Deleted 1 comment.', 'Deleted @count comments.'), format_string('Operation @operation was performed on comment.', array('@operation' => $operation)));
    }
    else {
      $this->assertText(t('The update has been performed.'), format_string('Operation @operation was performed on comment.', array('@operation' => $operation)));
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
