# comment_update_7008()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 363–378 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L363-L378)
- **Module/theme:** comment
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function comment_update_7008()
```

## Documentation

```text
Update database to match Drupal 7 schema.
```

## Code

```php
function comment_update_7008() {
  // Update default status to 1.
  db_change_field('comment', 'status', 'status', array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => TRUE,
    'default' => 1,
    'size' => 'tiny',
  ));

  // Realign indexes.
  db_drop_index('comment', 'comment_status_pid');
  db_add_index('comment', 'comment_status_pid', array('pid', 'status'));
  db_drop_index('comment', 'comment_pid_status');
  db_drop_index('comment', 'nid');
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
