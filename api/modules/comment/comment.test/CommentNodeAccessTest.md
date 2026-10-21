# CommentNodeAccessTest

- **Type:** Class
- **File:** [`modules/comment/comment.test`](_file.md), lines 1503–1563 · [local source](../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1503-L1563)
- **Module/theme:** comment

## Signature

```php
class CommentNodeAccessTest extends CommentHelperCase
```

## Documentation

```text
Tests comments with node access.

See http://drupal.org/node/886752 -- verify there is no PostgreSQL error when
viewing a node with threaded comments (a comment and a reply), if a node
access module is in use.
```

## Methods (derived index)

- [getInfo()](CommentNodeAccessTest/getInfo.md)
- [setUp()](CommentNodeAccessTest/setUp.md)
- [testThreadedCommentView()](CommentNodeAccessTest/testThreadedCommentView.md) — Test that threaded comments can be viewed.

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
