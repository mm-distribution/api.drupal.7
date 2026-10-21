# forum_update_7002()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 362–365 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L362-L365)
- **Module/theme:** forum
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function forum_update_7002()
```

## Documentation

```text
Add new index to forum_index table.
```

## Code

```php
function forum_update_7002() {
  db_drop_index('forum_index', 'forum_topics');
  db_add_index('forum_index', 'forum_topics', array('nid', 'tid', 'sticky', 'last_comment_timestamp'));
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
