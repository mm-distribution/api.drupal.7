# comment_update_7004()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 217–231 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L217-L231)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7004()
```

## Documentation

```text
Upgrade the {node_comment_statistics} table.
```

## Code

```php
function comment_update_7004() {
  db_add_field('node_comment_statistics', 'cid', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'The {comment}.cid of the last comment.',
  ));
  db_add_index('node_comment_statistics', 'cid', array('cid'));

  // The comment_count index may have been added in Drupal 6.
  if (!db_index_exists('node_comment_statistics', 'comment_count')) {
    // Add an index on the comment_count.
    db_add_index('node_comment_statistics', 'comment_count', array('comment_count'));
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
