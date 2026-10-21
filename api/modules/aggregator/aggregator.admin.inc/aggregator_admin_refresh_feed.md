# aggregator_admin_refresh_feed()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 407–413 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L407-L413)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_admin_refresh_feed($feed)
```

## Documentation

```text
Page callback: Refreshes a feed, then redirects to the overview page.

@param $feed
  An object describing the feed to be refreshed.
```

## Code

```php
function aggregator_admin_refresh_feed($feed) {
  if (!isset($_GET['token']) || !drupal_valid_token($_GET['token'], 'aggregator/update/' . $feed->fid)) {
    return MENU_ACCESS_DENIED;
  }
  aggregator_refresh($feed);
  drupal_goto('admin/config/services/aggregator');
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
