# CommentHelperCase::commentExists()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 109–123 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L109-L123)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function commentExists($comment, $reply = FALSE)
```

## Documentation

```text
Checks current page for specified comment.

@param object $comment Comment object.
@param boolean $reply The comment is a reply to another comment.
@return boolean Comment found.
```

## Code

```php
  function commentExists($comment, $reply = FALSE) {
    if ($comment && is_object($comment)) {
      $regex = '/' . ($reply ? '<div class="indented">(.*?)' : '');
      $regex .= '<a id="comment-' . $comment->id . '"(.*?)'; // Comment anchor.
      $regex .= '<div(.*?)'; // Begin in comment div.
      $regex .= $comment->subject . '(.*?)'; // Match subject.
      $regex .= $comment->comment . '(.*?)'; // Match comment.
      $regex .= '/s';

      return (boolean)preg_match($regex, $this->drupalGetContent());
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
