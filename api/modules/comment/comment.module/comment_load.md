# comment_load()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1698–1701 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1698-L1701)
- **Module/theme:** comment

## Signature

```php
function comment_load($cid, $reset = FALSE)
```

## Documentation

```text
Load the entire comment by cid.

@param $cid
  The identifying comment id.
@param $reset
  Whether to reset the internal static entity cache. Note that the static
  cache is disabled in comment_entity_info() by default.

@return
  The comment object.
```

## Code

```php
function comment_load($cid, $reset = FALSE) {
  $comment = comment_load_multiple(array($cid), array(), $reset);
  return $comment ? $comment[$cid] : FALSE;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
