# comment_enable()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 32–46 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L32-L46)
- **Module/theme:** comment
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function comment_enable()
```

## Documentation

```text
Implements hook_enable().
```

## Code

```php
function comment_enable() {
  // Insert records into the node_comment_statistics for nodes that are missing.
  $query = db_select('node', 'n');
  $query->leftJoin('node_comment_statistics', 'ncs', 'ncs.nid = n.nid');
  $query->addField('n', 'created', 'last_comment_timestamp');
  $query->addField('n', 'uid', 'last_comment_uid');
  $query->addField('n', 'nid');
  $query->addExpression('0', 'comment_count');
  $query->addExpression('NULL', 'last_comment_name');
  $query->isNull('ncs.comment_count');

  db_insert('node_comment_statistics')
    ->from($query)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
