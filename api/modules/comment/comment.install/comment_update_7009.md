# comment_update_7009()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 383–390 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L383-L390)
- **Module/theme:** comment
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function comment_update_7009()
```

## Documentation

```text
Change the last_comment_timestamp column description.
```

## Code

```php
function comment_update_7009() {
  db_change_field('node_comment_statistics', 'last_comment_timestamp', 'last_comment_timestamp', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'The Unix timestamp of the last comment that was posted within this node, from {comment}.changed.',
  ));
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
