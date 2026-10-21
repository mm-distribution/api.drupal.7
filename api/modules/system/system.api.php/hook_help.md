# hook_help()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2184–2194 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2184-L2194)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_help($path, $arg)
```

## Documentation

```text
Provide online user help.

By implementing hook_help(), a module can make documentation available to
the user for the module as a whole, or for specific paths. Help for
developers should usually be provided via function header comments in the
code, or in special API example files.

The page-specific help information provided by this hook appears as a system
help block on that page. The module overview help information is displayed
by the Help module. It can be accessed from the page at admin/help or from
the Modules page.

For detailed usage examples of:
- Module overview help, see node_help(). Module overview help should follow
  @link https://drupal.org/node/632280 the standard help template. @endlink
- Page-specific help with simple paths, see dashboard_help().
- Page-specific help using wildcards in path and $arg, see node_help()
  and block_help().

@param $path
  The router menu path, as defined in hook_menu(), for the help that is
  being requested; e.g., 'admin/people' or 'user/register'.  If the router
  path includes a wildcard, then this will appear in $path as %, even if it
  is a named %autoloader wildcard in the hook_menu() implementation; for
  example, node pages would have $path equal to 'node/%' or 'node/%/view'.
  For the help page for the module as a whole, $path will have the value
  'admin/help#module_name', where 'module_name" is the machine name of your
  module.
@param $arg
  An array that corresponds to the return value of the arg() function, for
  modules that want to provide help that is specific to certain values
  of wildcards in $path. For example, you could provide help for the path
  'user/1' by looking for the path 'user/%' and $arg[1] == '1'. This given
  array should always be used rather than directly invoking arg(), because
  your hook implementation may be called for other purposes besides building
  the current page's help. Note that depending on which module is invoking
  hook_help, $arg may contain only empty strings. Regardless, $arg[0] to
  $arg[11] will always be set.

@return
  A localized string containing the help text.
```

## Code

```php
function hook_help($path, $arg) {
  switch ($path) {
    // Main module help for the block module
    case 'admin/help#block':
      return '<p>' . t('Blocks are boxes of content rendered into an area, or region, of a web page. The default theme Bartik, for example, implements the regions "Sidebar first", "Sidebar second", "Featured", "Content", "Header", "Footer", etc., and a block may appear in any one of these areas. The <a href="@blocks">blocks administration page</a> provides a drag-and-drop interface for assigning a block to a region, and for controlling the order of blocks within regions.', array('@blocks' => url('admin/structure/block'))) . '</p>';

    // Help for another path in the block module
    case 'admin/structure/block':
      return '<p>' . t('This page provides a drag-and-drop interface for assigning a block to a region, and for controlling the order of blocks within regions. Since not all themes implement the same regions, or display regions in the same way, blocks are positioned on a per-theme basis. Remember that your changes will not be saved until you click the <em>Save blocks</em> button at the bottom of the page.') . '</p>';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_help()".

- [aggregator_help()](../../aggregator/aggregator.module/aggregator_help.md) — `modules/aggregator/aggregator.module`
- [announcements_feed_help()](../../announcements_feed/announcements_feed.module/announcements_feed_help.md) — `modules/announcements_feed/announcements_feed.module`
- [boot_test_2_help()](../../simpletest/tests/boot_test_2.module/boot_test_2_help.md) — `modules/simpletest/tests/boot_test_2.module`
- [block_help()](../../block/block.module/block_help.md) — `modules/block/block.module`
- [blog_help()](../../blog/blog.module/blog_help.md) — `modules/blog/blog.module`
- [book_help()](../../book/book.module/book_help.md) — `modules/book/book.module`
- [color_help()](../../color/color.module/color_help.md) — `modules/color/color.module`
- [comment_help()](../../comment/comment.module/comment_help.md) — `modules/comment/comment.module`
- [contact_help()](../../contact/contact.module/contact_help.md) — `modules/contact/contact.module`
- [contextual_help()](../../contextual/contextual.module/contextual_help.md) — `modules/contextual/contextual.module`
- [dashboard_help()](../../dashboard/dashboard.module/dashboard_help.md) — `modules/dashboard/dashboard.module`
- [dblog_help()](../../dblog/dblog.module/dblog_help.md) — `modules/dblog/dblog.module`
- [field_help()](../../field/field.module/field_help.md) — `modules/field/field.module`
- [field_sql_storage_help()](../../field/modules/field_sql_storage/field_sql_storage.module/field_sql_storage_help.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_ui_help()](../../field_ui/field_ui.module/field_ui_help.md) — `modules/field_ui/field_ui.module`
- [file_help()](../../file/file.module/file_help.md) — `modules/file/file.module`
- [filter_help()](../../filter/filter.module/filter_help.md) — `modules/filter/filter.module`
- [forum_help()](../../forum/forum.module/forum_help.md) — `modules/forum/forum.module`
- [help_help()](../../help/help.module/help_help.md) — `modules/help/help.module`
- [image_help()](../../image/image.module/image_help.md) — `modules/image/image.module`
- [list_help()](../../field/modules/list/list.module/list_help.md) — `modules/field/modules/list/list.module`
- [locale_help()](../../locale/locale.module/locale_help.md) — `modules/locale/locale.module`
- [menu_help()](../../menu/menu.module/menu_help.md) — `modules/menu/menu.module`
- [node_help()](../../node/node.module/node_help.md) — `modules/node/node.module`
- [number_help()](../../field/modules/number/number.module/number_help.md) — `modules/field/modules/number/number.module`
- [openid_help()](../../openid/openid.module/openid_help.md) — `modules/openid/openid.module`
- [options_help()](../../field/modules/options/options.module/options_help.md) — `modules/field/modules/options/options.module`
- [overlay_help()](../../overlay/overlay.module/overlay_help.md) — `modules/overlay/overlay.module`
- [path_help()](../../path/path.module/path_help.md) — `modules/path/path.module`
- [php_help()](../../php/php.module/php_help.md) — `modules/php/php.module`
- [poll_help()](../../poll/poll.module/poll_help.md) — `modules/poll/poll.module`
- [profile_help()](../../profile/profile.module/profile_help.md) — `modules/profile/profile.module`
- [rdf_help()](../../rdf/rdf.module/rdf_help.md) — `modules/rdf/rdf.module`
- [search_help()](../../search/search.module/search_help.md) — `modules/search/search.module`
- [shortcut_help()](../../shortcut/shortcut.module/shortcut_help.md) — `modules/shortcut/shortcut.module`
- [simpletest_help()](../../simpletest/simpletest.module/simpletest_help.md) — `modules/simpletest/simpletest.module`
- [statistics_help()](../../statistics/statistics.module/statistics_help.md) — `modules/statistics/statistics.module`
- [syslog_help()](../../syslog/syslog.module/syslog_help.md) — `modules/syslog/syslog.module`
- [system_help()](../system.module/system_help.md) — `modules/system/system.module`
- [taxonomy_help()](../../taxonomy/taxonomy.module/taxonomy_help.md) — `modules/taxonomy/taxonomy.module`
- [text_help()](../../field/modules/text/text.module/text_help.md) — `modules/field/modules/text/text.module`
- [toolbar_help()](../../toolbar/toolbar.module/toolbar_help.md) — `modules/toolbar/toolbar.module`
- [tracker_help()](../../tracker/tracker.module/tracker_help.md) — `modules/tracker/tracker.module`
- [translation_help()](../../translation/translation.module/translation_help.md) — `modules/translation/translation.module`
- [trigger_help()](../../trigger/trigger.module/trigger_help.md) — `modules/trigger/trigger.module`
- [update_help()](../../update/update.module/update_help.md) — `modules/update/update.module`
- [user_help()](../../user/user.module/user_help.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
