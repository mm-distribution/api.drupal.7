# forum_update_7000()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 261–264 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L261-L264)
- **Module/theme:** forum

## Signature

```php
function forum_update_7000()
```

## Documentation

```text
Add new index to forum table.
```

## Code

```php
function forum_update_7000() {
  db_drop_index('forum', 'nid');
  db_add_index('forum', 'forum_topic', array('nid', 'tid'));
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
