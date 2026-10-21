# modules/announcements_feed/announcements_feed.module

- **Source:** [local](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · 180 lines
- **Module/theme:** announcements_feed

## File documentation

```text
@file
Used to create an announcements feed using the JSON data from drupal.org.
```

## Functions (derived index)

- [announcements_feed_help()](announcements_feed_help.md) — Implements hook_help().
- [announcements_feed_menu()](announcements_feed_menu.md) — Implements hook_menu().
- [announcements_feed_permission()](announcements_feed_permission.md) — Implements hook_permission().
- [announcements_feed_theme()](announcements_feed_theme.md) — Implements hook_theme().
- [template_preprocess_announcements_feed()](template_preprocess_announcements_feed.md) — Processes variables for announcements-feed.tpl.php.
- [_announcements_feed_preprocess_item()](_announcements_feed_preprocess_item.md) — Helper to preprocess individual announcement items.
- [announcements_feed_page_alter()](announcements_feed_page_alter.md) — Implements hook_page_alter().
- [announcements_feed_toolbar_pre_render_alter()](announcements_feed_toolbar_pre_render_alter.md) — Pre-render function for adding default class to announcement link.
- [announcements_feed_cron()](announcements_feed_cron.md) — Implements hook_cron().

## Constants

### ANNOUNCEMENTS_FEED_DEFAULT_MAX_AGE

- Line 11

```php
define('ANNOUNCEMENTS_FEED_DEFAULT_MAX_AGE', 86400);
```

```text
Default maximum age of cached feed data in seconds.
```

### ANNOUNCEMENTS_FEED_DEFAULT_CRON_INTERVAL

- Line 16

```php
define('ANNOUNCEMENTS_FEED_DEFAULT_CRON_INTERVAL', 21600);
```

```text
Default cron interval for refreshing feed data in seconds.
```

### ANNOUNCEMENTS_FEED_DEFAULT_LIMIT

- Line 21

```php
define('ANNOUNCEMENTS_FEED_DEFAULT_LIMIT', 10);
```

```text
Default limit for number of feed items to fetch.
```

### ANNOUNCEMENTS_FEED_DEFAULT_JSON_URL

- Line 26

```php
define('ANNOUNCEMENTS_FEED_DEFAULT_JSON_URL', 'https://www.drupal.org/announcements.json');
```

```text
Default URL for the announcements JSON feed.
```

### ANNOUNCEMENTS_FEED_DEFAULT_LINK

- Line 31

```php
define('ANNOUNCEMENTS_FEED_DEFAULT_LINK', 'https://www.drupal.org/about/announcements');
```

```text
Default URL for the announcements feed at drupal.org.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
