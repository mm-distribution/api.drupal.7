# CommentHelperCase::setCommentForm()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 175–177 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L175-L177)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentForm($enabled)
```

## Documentation

```text
Set comment form location setting.

@param boolean $enabled
  Form value.
```

## Code

```php
  function setCommentForm($enabled) {
    $this->setCommentSettings('comment_form_location', ($enabled ? COMMENT_FORM_BELOW : COMMENT_FORM_SEPARATE_PAGE), 'Comment controls ' . ($enabled ? 'enabled' : 'disabled') . '.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
