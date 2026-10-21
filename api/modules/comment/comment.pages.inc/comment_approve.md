# comment_approve()

- **Type:** Function
- **File:** [`modules/comment/comment.pages.inc`](_file.md), lines 111–123 · [local source](../../../../source/modules/comment/comment.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.pages.inc#L111-L123)
- **Module/theme:** comment

## Signature

```php
function comment_approve($cid)
```

## Documentation

```text
Menu callback; publish specified comment.

@param $cid
  A comment identifier.
```

## Code

```php
function comment_approve($cid) {
  if (!isset($_GET['token']) || !drupal_valid_token($_GET['token'], "comment/$cid/approve")) {
    return MENU_ACCESS_DENIED;
  }
  if ($comment = comment_load($cid)) {
    $comment->status = COMMENT_PUBLISHED;
    comment_save($comment);

    drupal_set_message(t('Comment approved.'));
    drupal_goto('node/' . $comment->nid);
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/comment/comment.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
