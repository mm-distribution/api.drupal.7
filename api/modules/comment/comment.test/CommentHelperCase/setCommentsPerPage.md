# CommentHelperCase::setCommentsPerPage()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 195–197 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L195-L197)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentsPerPage($number)
```

## Documentation

```text
Set the default number of comments per page.

@param integer $comments
  Comments per page value.
```

## Code

```php
  function setCommentsPerPage($number) {
    $this->setCommentSettings('comment_default_per_page', $number, format_string('Number of comments per page set to @number.', array('@number' => $number)));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
