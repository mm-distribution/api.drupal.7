# menu_rebuild()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2774–2821 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2774-L2821)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_rebuild()
```

## Documentation

```text
Populates the database tables used by various menu functions.

This function will clear and populate the {menu_router} table, add entries
to {menu_links} for new router items, and then remove stale items from
{menu_links}. If called from update.php or install.php, it will also
schedule a call to itself on the first real page load from
menu_execute_active_handler(), because the maintenance page environment
is different and leaves stale data in the menu tables.

@return
  TRUE if the menu was rebuilt, FALSE if another thread was rebuilding
  in parallel and the current thread just waited for completion.
```

## Code

```php
function menu_rebuild() {
  if (!lock_acquire('menu_rebuild')) {
    // Wait for another request that is already doing this work.
    // We choose to block here since otherwise the router item may not
    // be available in menu_execute_active_handler() resulting in a 404.
    lock_wait('menu_rebuild');

    if (_menu_check_rebuild()) {
      // If we get here and menu_masks was not set, then it is possible a menu
      // is being reloaded, or that the process rebuilding the menu was unable
      // to complete successfully. A missing menu_masks variable could result
      // in a 404, so re-run the function.
      return menu_rebuild();
    }
    return FALSE;
  }

  $transaction = db_transaction();

  try {
    list($menu, $masks) = menu_router_build();
    _menu_router_save($menu, $masks);
    _menu_navigation_links_rebuild($menu);
    // Clear the menu, page and block caches.
    menu_cache_clear_all();
    _menu_clear_page_cache();

    if (defined('MAINTENANCE_MODE')) {
      variable_set('menu_rebuild_needed', TRUE);
    }
    else {
      variable_del('menu_rebuild_needed');
    }
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('menu', $e);
  }
  // Explicitly commit the transaction now; this ensures that the database
  // operations during the menu rebuild are committed before the lock is made
  // available again, since locks may not always reside in the same database
  // connection. The lock is acquired outside of the transaction so should also
  // be released outside of it.
  unset($transaction);

  lock_release('menu_rebuild');
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
