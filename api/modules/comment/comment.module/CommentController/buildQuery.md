# CommentController::buildQuery()

- **Type:** Method
- **File:** [`modules/comment/comment.module`](../_file.md), lines 1711–1720 · [local source](../../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1711-L1720)
- **Class:** [CommentController](../CommentController.md)
- **Module/theme:** comment

## Signature

```php
protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE) {
    $query = parent::buildQuery($ids, $conditions, $revision_id);
    // Specify additional fields from the user and node tables.
    $query->innerJoin('node', 'n', 'base.nid = n.nid');
    $query->addField('n', 'type', 'node_type');
    $query->innerJoin('users', 'u', 'base.uid = u.uid');
    $query->addField('u', 'name', 'registered_name');
    $query->fields('u', array('uid', 'signature', 'signature_format', 'picture'));
    return $query;
  }
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
