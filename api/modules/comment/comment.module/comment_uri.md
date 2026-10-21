# comment_uri()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 157–162 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L157-L162)
- **Module/theme:** comment

## Signature

```php
function comment_uri($comment)
```

## Documentation

```text
Implements callback_entity_info_uri().
```

## Code

```php
function comment_uri($comment) {
  return array(
    'path' => 'comment/' . $comment->cid,
    'options' => array('fragment' => 'comment-' . $comment->cid),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
