# CommentHelperCase::setCommentSubject()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 142–144 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L142-L144)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentSubject($enabled)
```

## Documentation

```text
Set comment subject setting.

@param boolean $enabled
  Subject value.
```

## Code

```php
  function setCommentSubject($enabled) {
    $this->setCommentSettings('comment_subject_field', ($enabled ? '1' : '0'), 'Comment subject ' . ($enabled ? 'enabled' : 'disabled') . '.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
