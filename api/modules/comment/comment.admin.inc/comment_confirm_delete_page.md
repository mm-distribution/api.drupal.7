# comment_confirm_delete_page()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 244–249 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L244-L249)
- **Module/theme:** comment

## Signature

```php
function comment_confirm_delete_page($cid)
```

## Documentation

```text
Page callback for comment deletions.
```

## Code

```php
function comment_confirm_delete_page($cid) {
  if ($comment = comment_load($cid)) {
    return drupal_get_form('comment_confirm_delete', $comment);
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
