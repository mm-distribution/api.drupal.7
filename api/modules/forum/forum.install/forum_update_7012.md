# forum_update_7012()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 460–463 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L460-L463)
- **Module/theme:** forum
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function forum_update_7012()
```

## Documentation

```text
Add 'created' and 'last_comment_timestamp' indexes.
```

## Code

```php
function forum_update_7012() {
  db_add_index('forum_index', 'created', array('created'));
  db_add_index('forum_index', 'last_comment_timestamp', array('last_comment_timestamp'));
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
