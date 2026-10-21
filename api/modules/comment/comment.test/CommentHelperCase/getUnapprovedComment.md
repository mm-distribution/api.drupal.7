# CommentHelperCase::getUnapprovedComment()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 257–262 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L257-L262)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function getUnapprovedComment($subject)
```

## Documentation

```text
Get the comment ID for an unapproved comment.

@param string $subject
  Comment subject to find.
@return integer
  Comment id.
```

## Code

```php
  function getUnapprovedComment($subject) {
    $this->drupalGet('admin/content/comment/approval');
    preg_match('/href="(.*?)#comment-([^"]+)"(.*?)>(' . $subject . ')/', $this->drupalGetContent(), $match);

    return $match[2];
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
