# comment_edit_page()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1831–1835 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1831-L1835)
- **Module/theme:** comment

## Signature

```php
function comment_edit_page($comment)
```

## Documentation

```text
Page callback for comment editing.
```

## Code

```php
function comment_edit_page($comment) {
  drupal_set_title(t('Edit comment %comment', array('%comment' => $comment->subject)), PASS_THROUGH);
  $node = node_load($comment->nid);
  return drupal_get_form("comment_node_{$node->type}_form", $comment);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
