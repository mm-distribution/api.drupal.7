# CommentHelperCase::setCommentAnonymous()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 185–187 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L185-L187)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentAnonymous($level)
```

## Documentation

```text
Set comment anonymous level setting.

@param integer $level
  Anonymous level.
```

## Code

```php
  function setCommentAnonymous($level) {
    $this->setCommentSettings('comment_anonymous', $level, format_string('Anonymous commenting set to level @level.', array('@level' => $level)));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
