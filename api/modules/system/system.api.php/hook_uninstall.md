# hook_uninstall()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3641–3643 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3641-L3643)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_uninstall()
```

## Documentation

```text
Remove any information that the module sets.

The information that the module should remove includes:
- variables that the module has set using variable_set() or system_settings_form()
- modifications to existing tables

The module should not remove its entry from the {system} table. Database
tables defined by hook_schema() will be removed automatically.

The uninstall hook must be implemented in the module's .install file. It
will fire when the module gets uninstalled but before the module's database
tables are removed, allowing your module to query its own tables during
this routine.

When hook_uninstall() is called, your module will already be disabled, so
its .module file will not be automatically included. If you need to call API
functions from your .module file in this hook, use drupal_load() to make
them available. (Keep this usage to a minimum, though, especially when
calling API functions that invoke hooks, or API functions from modules
listed as dependencies, since these may not be available or work as expected
when the module is disabled.)

@see hook_install()
@see hook_schema()
@see hook_disable()
@see hook_modules_uninstalled()
```

## Code

```php
function hook_uninstall() {
  variable_del('upload_file_types');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_uninstall()".

- [aggregator_uninstall()](../../aggregator/aggregator.install/aggregator_uninstall.md) — `modules/aggregator/aggregator.install`
- [announcements_feed_uninstall()](../../announcements_feed/announcements_feed.install/announcements_feed_uninstall.md) — `modules/announcements_feed/announcements_feed.install`
- [blog_uninstall()](../../blog/blog.install/blog_uninstall.md) — `modules/blog/blog.install`
- [book_uninstall()](../../book/book.install/book_uninstall.md) — `modules/book/book.install`
- [comment_uninstall()](../../comment/comment.install/comment_uninstall.md) — `modules/comment/comment.install`
- [contact_uninstall()](../../contact/contact.install/contact_uninstall.md) — `modules/contact/contact.install`
- [dashboard_uninstall()](../../dashboard/dashboard.install/dashboard_uninstall.md) — `modules/dashboard/dashboard.install`
- [dblog_uninstall()](../../dblog/dblog.install/dblog_uninstall.md) — `modules/dblog/dblog.install`
- [forum_uninstall()](../../forum/forum.install/forum_uninstall.md) — `modules/forum/forum.install`
- [image_uninstall()](../../image/image.install/image_uninstall.md) — `modules/image/image.install`
- [locale_uninstall()](../../locale/locale.install/locale_uninstall.md) — `modules/locale/locale.install`
- [menu_uninstall()](../../menu/menu.install/menu_uninstall.md) — `modules/menu/menu.install`
- [profile_uninstall()](../../profile/profile.install/profile_uninstall.md) — `modules/profile/profile.install`
- [search_uninstall()](../../search/search.install/search_uninstall.md) — `modules/search/search.install`
- [shortcut_uninstall()](../../shortcut/shortcut.install/shortcut_uninstall.md) — `modules/shortcut/shortcut.install`
- [simpletest_uninstall()](../../simpletest/simpletest.install/simpletest_uninstall.md) — `modules/simpletest/simpletest.install`
- [statistics_uninstall()](../../statistics/statistics.install/statistics_uninstall.md) — `modules/statistics/statistics.install`
- [syslog_uninstall()](../../syslog/syslog.install/syslog_uninstall.md) — `modules/syslog/syslog.install`
- [taxonomy_uninstall()](../../taxonomy/taxonomy.install/taxonomy_uninstall.md) — `modules/taxonomy/taxonomy.install`
- [tracker_uninstall()](../../tracker/tracker.install/tracker_uninstall.md) — `modules/tracker/tracker.install`
- [update_uninstall()](../../update/update.install/update_uninstall.md) — `modules/update/update.install`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
