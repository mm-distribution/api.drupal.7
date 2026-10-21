# CommentHelperCase

- **Type:** Class
- **File:** [`modules/comment/comment.test`](_file.md), lines 8–263 · [local source](../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L8-L263)
- **Module/theme:** comment

## Signature

```php
class CommentHelperCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $super_user

```php
protected $super_user;
```

### $admin_user

```php
protected $admin_user;
```

### $web_user

```php
protected $web_user;
```

### $node

```php
protected $node;
```

## Methods (derived index)

- [setUp()](CommentHelperCase/setUp.md)
- [postComment()](CommentHelperCase/postComment.md) — Post comment.
- [commentExists()](CommentHelperCase/commentExists.md) — Checks current page for specified comment.
- [deleteComment()](CommentHelperCase/deleteComment.md) — Delete comment.
- [setCommentSubject()](CommentHelperCase/setCommentSubject.md) — Set comment subject setting.
- [setCommentPreview()](CommentHelperCase/setCommentPreview.md) — Set comment preview setting.
- [setCommentForm()](CommentHelperCase/setCommentForm.md) — Set comment form location setting.
- [setCommentAnonymous()](CommentHelperCase/setCommentAnonymous.md) — Set comment anonymous level setting.
- [setCommentsPerPage()](CommentHelperCase/setCommentsPerPage.md) — Set the default number of comments per page.
- [setCommentSettings()](CommentHelperCase/setCommentSettings.md) — Set comment setting for article content type.
- [commentContactInfoAvailable()](CommentHelperCase/commentContactInfoAvailable.md) — Check for contact info.
- [performCommentOperation()](CommentHelperCase/performCommentOperation.md) — Perform the specified operation on the specified comment.
- [getUnapprovedComment()](CommentHelperCase/getUnapprovedComment.md) — Get the comment ID for an unapproved comment.

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
