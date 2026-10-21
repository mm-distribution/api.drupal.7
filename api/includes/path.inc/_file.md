# includes/path.inc

- **Source:** [local](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · 593 lines

## File documentation

```text
@file
Functions to handle paths in Drupal, including path aliasing.

These functions are not loaded for cached pages, but modules that need
to use them in hook_boot() or hook exit() can make them available, by
executing "drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);".
```

## Functions (derived index)

- [drupal_path_initialize()](drupal_path_initialize.md) — Initialize the $_GET['q'] variable to the proper normal path.
- [drupal_lookup_path()](drupal_lookup_path.md) — Given an alias, return its Drupal system URL if one exists. Given a Drupal system URL return one of its aliases if such a one exists. Otherwise, return FALSE.
- [drupal_cache_system_paths()](drupal_cache_system_paths.md) — Cache system paths for a page.
- [drupal_get_path_alias()](drupal_get_path_alias.md) — Given an internal Drupal path, return the alias set by the administrator.
- [drupal_get_normal_path()](drupal_get_normal_path.md) — Given a path alias, return the internal path it represents.
- [drupal_is_front_page()](drupal_is_front_page.md) — Check if the current page is the front page.
- [drupal_match_path()](drupal_match_path.md) — Check if a path matches any pattern in a set of patterns.
- [current_path()](current_path.md) — Return the current URL path of the page being viewed.
- [drupal_path_alias_whitelist_rebuild()](drupal_path_alias_whitelist_rebuild.md) — Rebuild the path alias white list.
- [path_load()](path_load.md) — Fetches a specific URL alias from the database.
- [path_save()](path_save.md) — Save a path alias to the database.
- [path_delete()](path_delete.md) — Delete a URL alias.
- [path_is_admin()](path_is_admin.md) — Determines whether a path is in the administrative section of the site.
- [path_get_admin_paths()](path_get_admin_paths.md) — Gets a list of administrative and non-administrative paths.
- [drupal_valid_path()](drupal_valid_path.md) — Checks a path exists and the current user has access to it.
- [drupal_clear_path_cache()](drupal_clear_path_cache.md) — Clear the path cache.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
