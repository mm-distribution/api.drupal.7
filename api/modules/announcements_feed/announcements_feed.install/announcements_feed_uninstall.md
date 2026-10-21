# announcements_feed_uninstall()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.install`](_file.md), lines 11–19 · [local source](../../../../source/modules/announcements_feed/announcements_feed.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.install#L11-L19)
- **Module/theme:** announcements_feed
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function announcements_feed_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function announcements_feed_uninstall() {
  // Delete the announcements_feed module variables.
  variable_del('announcements_feed_limit');
  variable_del('announcements_feed_cron_interval');
  variable_del('announcements_feed_max_age');
  variable_del('announcements_feed_json_url');
  variable_del('announcements_feed_link');
  variable_del('announcements_feed_last_fetch');
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.install](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.install) · Licensed GPL-2.0-or-later (see LICENSE)._
