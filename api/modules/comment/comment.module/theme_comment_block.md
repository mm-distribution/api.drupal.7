# theme_comment_block()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 597–610 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L597-L610)
- **Module/theme:** comment
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_comment_block()
```

## Documentation

```text
Returns HTML for a list of recent comments to be displayed in the comment block.

@ingroup themeable
```

## Code

```php
function theme_comment_block() {
  $items = array();
  $number = variable_get('comment_block_count', 10);
  foreach (comment_get_recent($number) as $comment) {
    $items[] = l($comment->subject, 'comment/' . $comment->cid, array('fragment' => 'comment-' . $comment->cid)) . '&nbsp;<span>' . t('@time ago', array('@time' => format_interval(REQUEST_TIME - $comment->changed))) . '</span>';
  }

  if ($items) {
    return theme('item_list', array('items' => $items));
  }
  else {
    return t('No comments available.');
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
