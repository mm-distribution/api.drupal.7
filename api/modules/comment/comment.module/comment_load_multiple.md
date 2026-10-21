# comment_load_multiple()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1682–1684 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1682-L1684)
- **Module/theme:** comment

## Signature

```php
function comment_load_multiple($cids = array(), $conditions = array(), $reset = FALSE)
```

## Documentation

```text
Load comments from the database.

@param $cids
  An array of comment IDs.
@param $conditions
  (deprecated) An associative array of conditions on the {comments}
  table, where the keys are the database fields and the values are the
  values those fields must have. Instead, it is preferable to use
  EntityFieldQuery to retrieve a list of entity IDs loadable by
  this function.
@param $reset
  Whether to reset the internal static entity cache. Note that the static
  cache is disabled in comment_entity_info() by default.

@return
  An array of comment objects, indexed by comment ID.

@see entity_load()
@see EntityFieldQuery

@todo Remove $conditions in Drupal 8.
```

## Code

```php
function comment_load_multiple($cids = array(), $conditions = array(), $reset = FALSE) {
  return entity_load('comment', $cids, $conditions, $reset);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
