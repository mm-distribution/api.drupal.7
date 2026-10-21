# modules/dashboard/dashboard.module

- **Source:** [local](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · 682 lines
- **Module/theme:** dashboard

## File documentation

```text
@file
Provides a dashboard page in the administrative interface.
```

## Functions (derived index)

- [dashboard_help()](dashboard_help.md) — Implements hook_help().
- [dashboard_menu()](dashboard_menu.md) — Implements hook_menu().
- [dashboard_permission()](dashboard_permission.md) — Implements hook_permission().
- [dashboard_block_info_alter()](dashboard_block_info_alter.md) — Implements hook_block_info_alter().
- [dashboard_block_list_alter()](dashboard_block_list_alter.md) — Implements hook_block_list_alter().
- [dashboard_page_build()](dashboard_page_build.md) — Implements hook_page_build().
- [dashboard_system_info_alter()](dashboard_system_info_alter.md) — Implements hook_system_info_alter().
- [dashboard_theme()](dashboard_theme.md) — Implements hook_theme().
- [dashboard_forms()](dashboard_forms.md) — Implements hook_forms().
- [dashboard_admin()](dashboard_admin.md) — Page callback: Displays the dashboard.
- [dashboard_admin_blocks()](dashboard_admin_blocks.md) — Page callback: Builds the page for administering dashboard blocks.
- [dashboard_form_block_admin_display_form_alter()](dashboard_form_block_admin_display_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [dashboard_form_dashboard_admin_display_form_alter()](dashboard_form_dashboard_admin_display_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [dashboard_form_block_admin_configure_alter()](dashboard_form_block_admin_configure_alter.md) — Implements hook_form_FORM_ID_alter().
- [dashboard_form_block_add_block_form_alter()](dashboard_form_block_add_block_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [template_preprocess_dashboard_admin_display_form()](template_preprocess_dashboard_admin_display_form.md) — Preprocesses variables for block-admin-display-form.tpl.php.
- [dashboard_is_visible()](dashboard_is_visible.md) — Determines if the dashboard should be displayed on the current page.
- [dashboard_region_descriptions()](dashboard_region_descriptions.md) — Returns an array of dashboard region descriptions, keyed by region name.
- [dashboard_regions()](dashboard_regions.md) — Returns an array of dashboard region names.
- [dashboard_dashboard_regions()](dashboard_dashboard_regions.md) — Implements hook_dashboard_regions().
- [dashboard_show_disabled()](dashboard_show_disabled.md) — Ajax callback: Shows disabled blocks in the dashboard customization mode.
- [dashboard_show_block_content()](dashboard_show_block_content.md) — Ajax callback: Displays the rendered contents of a specific block.
- [dashboard_update()](dashboard_update.md) — Sets the new weight of each region according to the drag-and-drop order.
- [theme_dashboard()](theme_dashboard.md) — Returns HTML for the entire dashboard.
- [theme_dashboard_admin()](theme_dashboard_admin.md) — Returns HTML for the non-customizable part of the dashboard page.
- [theme_dashboard_region()](theme_dashboard_region.md) — Returns HTML for a generic dashboard region.
- [theme_dashboard_disabled_blocks()](theme_dashboard_disabled_blocks.md) — Returns HTML for disabled blocks, for use in dashboard customization mode.
- [theme_dashboard_disabled_block()](theme_dashboard_disabled_block.md) — Returns HTML for disabled blocks, for use in dashboard customization mode.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
