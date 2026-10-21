# comment_update_7003()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 184–212 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L184-L212)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7003()
```

## Documentation

```text
Split {comment}.timestamp into 'created' and 'changed', improve indexing on {comment}.
```

## Code

```php
function comment_update_7003() {
  // Drop the old indexes.
  db_drop_index('comment', 'status');
  db_drop_index('comment', 'pid');

  // Create a created column.
  db_add_field('comment', 'created', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
  ));

  // Rename the timestamp column to changed.
  db_change_field('comment', 'timestamp', 'changed', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
  ));

  // Migrate the data.
  // @todo db_update() should support this.
  db_query('UPDATE {comment} SET created = changed');

  // Recreate the indexes.
  // The 'comment_num_new' index is optimized for comment_num_new()
  // and comment_new_page_count().
  db_add_index('comment', 'comment_num_new', array('nid', 'status', 'created', 'cid', 'thread'));
  db_add_index('comment', 'comment_pid_status', array('pid', 'status'));
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
