# _update_authorize_clear_update_status()

- **Type:** Function
- **File:** [`modules/update/update.authorize.inc`](_file.md), lines 331–339 · [local source](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc#L331-L339)
- **Module/theme:** update

## Signature

```php
function _update_authorize_clear_update_status()
```

## Documentation

```text
Clears cached available update status data.

Since this function is run at such a low bootstrap level, the Update Manager
module is not loaded. So, we can't just call _update_cache_clear(). However,
the database is bootstrapped, so we can do a query ourselves to clear out
what we want to clear.

Note that we do not want to just truncate the table, since that would remove
items related to currently pending fetch attempts.

@see update_authorize_update_batch_finished()
@see _update_cache_clear()
```

## Code

```php
function _update_authorize_clear_update_status() {
  $query = db_delete('cache_update');
  $query->condition(
    db_or()
    ->condition('cid', 'update_project_%', 'LIKE')
    ->condition('cid', 'available_releases::%', 'LIKE')
  );
  $query->execute();
}
```

---
_Drupal 7.103 · [modules/update/update.authorize.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
