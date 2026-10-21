# modules/overlay/overlay.module

- **Source:** [local](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · 1025 lines
- **Module/theme:** overlay

## File documentation

```text
@file
Displays the Drupal administration interface in an overlay.
```

## Functions (derived index)

- [overlay_help()](overlay_help.md) — Implements hook_help().
- [overlay_menu()](overlay_menu.md) — Implements hook_menu().
- [overlay_admin_paths()](overlay_admin_paths.md) — Implements hook_admin_paths().
- [overlay_permission()](overlay_permission.md) — Implements hook_permission().
- [overlay_theme()](overlay_theme.md) — Implements hook_theme().
- [overlay_form_alter()](overlay_form_alter.md) — Implements hook_form_alter().
- [overlay_form_user_profile_form_alter()](overlay_form_user_profile_form_alter.md) — Implements hook_form_FORM_ID_alter().
- [overlay_user_presave()](overlay_user_presave.md) — Implements hook_user_presave().
- [overlay_init()](overlay_init.md) — Implements hook_init().
- [overlay_exit()](overlay_exit.md) — Implements hook_exit().
- [overlay_library()](overlay_library.md) — Implements hook_library().
- [overlay_drupal_goto_alter()](overlay_drupal_goto_alter.md) — Implements hook_drupal_goto_alter().
- [overlay_batch_alter()](overlay_batch_alter.md) — Implements hook_batch_alter().
- [overlay_page_alter()](overlay_page_alter.md) — Implements hook_page_alter().
- [overlay_user_dismiss_message()](overlay_user_dismiss_message.md) — Page callback: Dismisses the overlay accessibility message for this user.
- [overlay_disable_message()](overlay_disable_message.md) — Returns a renderable array representing a message for disabling the overlay.
- [theme_overlay_disable_message()](theme_overlay_disable_message.md) — Returns the HTML for the message about how to disable the overlay.
- [overlay_block_list_alter()](overlay_block_list_alter.md) — Implements hook_block_list_alter().
- [overlay_system_info_alter()](overlay_system_info_alter.md) — Implements hook_system_info_alter().
- [overlay_preprocess_html()](overlay_preprocess_html.md) — Implements hook_preprocess_html().
- [overlay_preprocess_maintenance_page()](overlay_preprocess_maintenance_page.md) — Implements hook_preprocess_maintenance_page().
- [template_preprocess_overlay()](template_preprocess_overlay.md) — Implements template_preprocess_HOOK() for overlay.tpl.php
- [template_process_overlay()](template_process_overlay.md) — Implements template_process_HOOK() for overlay.tpl.php
- [overlay_preprocess_page()](overlay_preprocess_page.md) — Implements hook_preprocess_page().
- [overlay_display_empty_page()](overlay_display_empty_page.md) — Stores and returns whether an empty page override is needed.
- [overlay_page_delivery_callback_alter()](overlay_page_delivery_callback_alter.md) — Implements hook_page_delivery_callback_alter().
- [overlay_deliver_empty_page()](overlay_deliver_empty_page.md) — Prints an empty page.
- [overlay_get_mode()](overlay_get_mode.md) — Gets the current overlay mode.
- [overlay_set_mode()](overlay_set_mode.md) — Sets the overlay mode and adds proper JavaScript and styles to the page.
- [overlay_overlay_parent_initialize()](overlay_overlay_parent_initialize.md) — Implements hook_overlay_parent_initialize().
- [overlay_overlay_child_initialize()](overlay_overlay_child_initialize.md) — Implements hook_overlay_child_initialize().
- [overlay_close_dialog()](overlay_close_dialog.md) — Requests that the overlay closes when the page is displayed.
- [overlay_regions()](overlay_regions.md) — Returns a list of page regions that appear in the overlay.
- [overlay_supplemental_regions()](overlay_supplemental_regions.md) — Returns a list of supplemental page regions for the overlay.
- [_overlay_region_list()](_overlay_region_list.md) — Returns a list of page regions related to the overlay.
- [overlay_get_regions_to_render()](overlay_get_regions_to_render.md) — Returns a list of page regions that rendering should be limited to.
- [overlay_set_regions_to_render()](overlay_set_regions_to_render.md) — Sets the regions of the page that rendering will be limited to.
- [overlay_render_region()](overlay_render_region.md) — Renders an individual page region.
- [overlay_get_rendered_content()](overlay_get_rendered_content.md) — Returns any rendered content that was stored earlier in the page request.
- [overlay_store_rendered_content()](overlay_store_rendered_content.md) — Stores strings representing rendered HTML content.
- [overlay_request_refresh()](overlay_request_refresh.md) — Requests that the parent window refreshes a particular page region.
- [overlay_request_page_refresh()](overlay_request_page_refresh.md) — Requests that the entire parent window is reloaded when the overlay closes.
- [overlay_trigger_refresh()](overlay_trigger_refresh.md) — Checks if the parent window needs to be refreshed on this page load.
- [overlay_ajax_render_region()](overlay_ajax_render_region.md) — Prints the markup obtained by rendering a single region of the page.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
