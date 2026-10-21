# comment_get_display_page()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1822–1826 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1822-L1826)
- **Module/theme:** comment

## Signature

```php
function comment_get_display_page($cid, $node_type)
```

## Documentation

```text
Return the page number for a comment.

Finds the correct page number for a comment taking into account display
and paging settings.

@param $cid
  The comment ID.
@param $node_type
  The node type the comment is attached to.
@return
  The page number.
```

## Code

```php
function comment_get_display_page($cid, $node_type) {
  $ordinal = comment_get_display_ordinal($cid, $node_type);
  $comments_per_page = variable_get('comment_default_per_page_' . $node_type, 50);
  return floor($ordinal / $comments_per_page);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
