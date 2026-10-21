# comment_delete()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1621–1623 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1621-L1623)
- **Module/theme:** comment

## Signature

```php
function comment_delete($cid)
```

## Documentation

```text
Delete a comment and all its replies.

@param $cid
  The comment to delete.
```

## Code

```php
function comment_delete($cid) {
  comment_delete_multiple(array($cid));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
