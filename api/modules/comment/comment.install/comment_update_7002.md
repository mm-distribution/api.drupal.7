# comment_update_7002()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 162–179 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L162-L179)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7002()
```

## Documentation

```text
Rename {comments} table to {comment} and upgrade it.
```

## Code

```php
function comment_update_7002() {
  db_rename_table('comments', 'comment');

  // Add user-related indexes. These may already exist from Drupal 6.
  if (!db_index_exists('comment', 'comment_uid')) {
    db_add_index('comment', 'comment_uid', array('uid'));
    db_add_index('node_comment_statistics', 'last_comment_uid', array('last_comment_uid'));
  }

  // Create a language column.
  db_add_field('comment', 'language', array(
    'type' => 'varchar',
    'length' => 12,
    'not null' => TRUE,
    'default' => '',
  ));
  db_add_index('comment', 'comment_nid_language', array('nid', 'language'));
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
