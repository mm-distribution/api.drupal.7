# Menu item types

- **Topic id:** `menu_item_types`
- **Defined in:** [`includes/menu.inc`](../includes/menu.inc/_file.md), line 127 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L127)

## Documentation

```text
@defgroup menu_item_types Menu item types
@{
Definitions for various menu item types.

Menu item definitions provide one of these constants, which are shortcuts for
combinations of @link menu_flags Menu flags @endlink.
```

## Members (derived, 6)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [MENU_CALLBACK](../includes/menu.inc/_file.md#menu_callback) (constant) — Menu type -- A hidden, internal callback, typically used for API calls.
- [MENU_DEFAULT_LOCAL_TASK](../includes/menu.inc/_file.md#menu_default_local_task) (constant) — Menu type -- The "default" local task, which is initially active.
- [MENU_LOCAL_ACTION](../includes/menu.inc/_file.md#menu_local_action) (constant) — Menu type -- An action specific to the parent, usually rendered as a link.
- [MENU_LOCAL_TASK](../includes/menu.inc/_file.md#menu_local_task) (constant) — Menu type -- A task specific to the parent item, usually rendered as a tab.
- [MENU_NORMAL_ITEM](../includes/menu.inc/_file.md#menu_normal_item) (constant) — Menu type -- A "normal" menu item that's shown in menu and breadcrumbs.
- [MENU_SUGGESTED_ITEM](../includes/menu.inc/_file.md#menu_suggested_item) (constant) — Menu type -- A normal menu item, hidden until enabled by an administrator.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
