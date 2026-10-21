# forum_update_7011()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 447–455 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L447-L455)
- **Module/theme:** forum
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function forum_update_7011()
```

## Documentation

```text
Update {forum_index} so that only published nodes are indexed.
```

## Code

```php
function forum_update_7011() {
  $select = db_select('node', 'n')
    ->fields('n', array('nid'))
    ->condition('status', 0 );

  db_delete('forum_index')
    ->condition('nid', $select, 'IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
