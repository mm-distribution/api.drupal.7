# Form builder functions

- **Topic id:** `forms`
- **Defined in:** [`includes/form.inc`](../includes/form.inc/_file.md), line 7 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L7)

## Documentation

```text
@defgroup forms Form builder functions
@{
Functions that build an abstract representation of a HTML form.

All modules should declare their form builder functions to be in this
group and each builder function should reference its validate and submit
functions using \@see. Conversely, validate and submit functions should
reference the form builder function using \@see. For examples, of this see
system_modules_uninstall() or user_pass(), the latter of which has the
following in its doxygen documentation:
- \@ingroup forms
- \@see user_pass_validate()
- \@see user_pass_submit()

@}
```

## Members (derived, 131)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_install_configure_form()](../includes/install.core.inc/_install_configure_form.md) (function) — Form constructor for a site configuration form.
- [aggregator_admin_form()](../modules/aggregator/aggregator.admin.inc/aggregator_admin_form.md) (function) — Form constructor for the aggregator system settings.
- [aggregator_categorize_items()](../modules/aggregator/aggregator.pages.inc/aggregator_categorize_items.md) (function) — Form constructor to build the page list form.
- [aggregator_form_category()](../modules/aggregator/aggregator.admin.inc/aggregator_form_category.md) (function) — Form constructor to add/edit/delete aggregator categories.
- [aggregator_form_feed()](../modules/aggregator/aggregator.admin.inc/aggregator_form_feed.md) (function) — Form constructor for adding and editing feed sources.
- [aggregator_form_opml()](../modules/aggregator/aggregator.admin.inc/aggregator_form_opml.md) (function) — Form constructor for importing feeds from OPML.
- [authorize_filetransfer_form()](../includes/authorize.inc/authorize_filetransfer_form.md) (function) — Form constructor for the file transfer authorization form.
- [block_add_block_form()](../modules/block/block.admin.inc/block_add_block_form.md) (function) — Form constructor for the add block form.
- [block_admin_configure()](../modules/block/block.admin.inc/block_admin_configure.md) (function) — Form constructor for the block configuration form.
- [block_admin_display_form()](../modules/block/block.admin.inc/block_admin_display_form.md) (function) — Form constructor for the main block administration form.
- [block_custom_block_form()](../modules/block/block.module/block_custom_block_form.md) (function) — Form constructor for the custom block form.
- [book_admin_edit()](../modules/book/book.admin.inc/book_admin_edit.md) (function) — Form constructor for administering a single book's hierarchy.
- [book_admin_settings()](../modules/book/book.admin.inc/book_admin_settings.md) (function) — Form constructor for the book settings form.
- [book_outline_form()](../modules/book/book.pages.inc/book_outline_form.md) (function) — Form constructor for the book outline form.
- [book_remove_form()](../modules/book/book.pages.inc/book_remove_form.md) (function) — Form constructor to confirm removal of a node from a book.
- [color_scheme_form()](../modules/color/color.module/color_scheme_form.md) (function) — Form constructor for the color configuration form for a particular theme.
- [comment_admin_overview()](../modules/comment/comment.admin.inc/comment_admin_overview.md) (function) — Form builder for the comment overview administration form.
- [comment_confirm_delete()](../modules/comment/comment.admin.inc/comment_confirm_delete.md) (function) — Form builder; Builds the confirmation form for deleting a single comment.
- [comment_form()](../modules/comment/comment.module/comment_form.md) (function) — Generate the basic commenting form, for appending to a node or display on a separate page.
- [comment_multiple_delete_confirm()](../modules/comment/comment.admin.inc/comment_multiple_delete_confirm.md) (function) — List the selected comments and verify that the admin wants to delete them.
- [comment_unpublish_by_keyword_action_form()](../modules/comment/comment.module/comment_unpublish_by_keyword_action_form.md) (function) — Form builder; Prepare a form for blacklisted keywords.
- [contact_category_edit_form()](../modules/contact/contact.admin.inc/contact_category_edit_form.md) (function) — Form constructor for the category edit form.
- [contact_personal_form()](../modules/contact/contact.pages.inc/contact_personal_form.md) (function) — Form constructor for the personal contact form.
- [contact_site_form()](../modules/contact/contact.pages.inc/contact_site_form.md) (function) — Form constructor for the site-wide contact form.
- [dblog_clear_log_form()](../modules/dblog/dblog.admin.inc/dblog_clear_log_form.md) (function) — Form constructor for the form that clears out the log.
- [dblog_filter_form()](../modules/dblog/dblog.admin.inc/dblog_filter_form.md) (function) — Form constructor for the database logging filter form.
- [field_ui_display_overview_form()](../modules/field_ui/field_ui.admin.inc/field_ui_display_overview_form.md) (function) — Form constructor for the field display settings for a given view mode.
- [field_ui_field_delete_form()](../modules/field_ui/field_ui.admin.inc/field_ui_field_delete_form.md) (function) — Form constructor for removing a field instance from a bundle.
- [field_ui_field_edit_form()](../modules/field_ui/field_ui.admin.inc/field_ui_field_edit_form.md) (function) — Form constructor for the field instance settings form.
- [field_ui_field_overview_form()](../modules/field_ui/field_ui.admin.inc/field_ui_field_overview_form.md) (function) — Form constructor for the 'Manage fields' form of a bundle.
- [field_ui_field_settings_form()](../modules/field_ui/field_ui.admin.inc/field_ui_field_settings_form.md) (function) — Form constructor for the field settings edit page.
- [field_ui_widget_type_form()](../modules/field_ui/field_ui.admin.inc/field_ui_widget_type_form.md) (function) — Form constructor for the widget selection form.
- [file_module_test_form()](../modules/file/tests/file_module_test.module/file_module_test_form.md) (function) — Form constructor for testing a 'managed_file' element.
- [filter_admin_disable()](../modules/filter/filter.admin.inc/filter_admin_disable.md) (function) — Form constructor for the text format deletion confirmation form.
- [filter_admin_format_form()](../modules/filter/filter.admin.inc/filter_admin_format_form.md) (function) — Form constructor for the text format add/edit form.
- [filter_admin_overview()](../modules/filter/filter.admin.inc/filter_admin_overview.md) (function) — Page callback: Form constructor for a form to list and reorder text formats.
- [forum_admin_settings()](../modules/forum/forum.admin.inc/forum_admin_settings.md) (function) — Form constructor for the forum settings page.
- [forum_confirm_delete()](../modules/forum/forum.admin.inc/forum_confirm_delete.md) (function) — Form constructor for confirming deletion of a forum taxonomy term.
- [forum_form_container()](../modules/forum/forum.admin.inc/forum_form_container.md) (function) — Form constructor for adding and editing forum containers.
- [forum_form_forum()](../modules/forum/forum.admin.inc/forum_form_forum.md) (function) — Form constructor for adding and editing a forum.
- [forum_overview()](../modules/forum/forum.admin.inc/forum_overview.md) (function) — Form constructor for the forum overview form.
- [image_effect_delete_form()](../modules/image/image.admin.inc/image_effect_delete_form.md) (function) — Form builder; Form for deleting an image effect.
- [image_effect_form()](../modules/image/image.admin.inc/image_effect_form.md) (function) — Form builder; Form for adding and editing image effects.
- [image_style_add_form()](../modules/image/image.admin.inc/image_style_add_form.md) (function) — Form builder; Form for adding a new image style.
- [image_style_delete_form()](../modules/image/image.admin.inc/image_style_delete_form.md) (function) — Form builder; Form for deleting an image style.
- [image_style_form()](../modules/image/image.admin.inc/image_style_form.md) (function) — Form builder; Edit an image style name and effects order.
- [install_configure_form()](../includes/install.core.inc/install_configure_form.md) (function) — Form constructor for a form to configure the new site.
- [install_select_locale_form()](../includes/install.core.inc/install_select_locale_form.md) (function) — Form constructor for the language selection form.
- [install_select_profile_form()](../includes/install.core.inc/install_select_profile_form.md) (function) — Form constructor for the profile selection form.
- [install_settings_form()](../includes/install.core.inc/install_settings_form.md) (function) — Form constructor for a form to configure and rewrite settings.php.
- [locale_language_selector_form()](../modules/locale/locale.module/locale_language_selector_form.md) (function) — Form builder callback to display language selection widget.
- [locale_translation_filter_form()](../modules/locale/locale.admin.inc/locale_translation_filter_form.md) (function) — Return form for locale translation filters.
- [node_admin_content()](../modules/node/node.admin.inc/node_admin_content.md) (function) — Page callback: Form constructor for the content administration form.
- [node_admin_nodes()](../modules/node/node.admin.inc/node_admin_nodes.md) (function) — Form builder: Builds the node administration overview.
- [node_assign_owner_action_form()](../modules/node/node.module/node_assign_owner_action_form.md) (function) — Generates the settings form for node_assign_owner_action().
- [node_configure_rebuild_confirm()](../modules/node/node.admin.inc/node_configure_rebuild_confirm.md) (function) — Menu callback: confirm rebuilding of permissions.
- [node_filter_form()](../modules/node/node.admin.inc/node_filter_form.md) (function) — Returns the node administration filters form array to node_admin_content().
- [node_form()](../modules/node/node.pages.inc/node_form.md) (function) — Form constructor for the node add/edit form.
- [node_multiple_delete_confirm()](../modules/node/node.admin.inc/node_multiple_delete_confirm.md) (function) — Multiple node deletion confirmation form for node_admin_content().
- [node_revision_delete_confirm()](../modules/node/node.pages.inc/node_revision_delete_confirm.md) (function) — Form constructor for the revision deletion confirmation form.
- [node_revision_revert_confirm()](../modules/node/node.pages.inc/node_revision_revert_confirm.md) (function) — Asks for confirmation of the reversion to prevent against CSRF attacks.
- [node_type_delete_confirm()](../modules/node/content_types.inc/node_type_delete_confirm.md) (function) — Menu callback; delete a single content type.
- [node_type_form()](../modules/node/content_types.inc/node_type_form.md) (function) — Form constructor for the node type editing form.
- [openid_user_add()](../modules/openid/openid.pages.inc/openid_user_add.md) (function) — Form builder; Add an OpenID identity.
- [path_admin_filter_form()](../modules/path/path.admin.inc/path_admin_filter_form.md) (function) — Form constructor for the path admin overview filter form.
- [path_admin_form()](../modules/path/path.admin.inc/path_admin_form.md) (function) — Form constructor for the path administration form.
- [poll_cancel_form()](../modules/poll/poll.module/poll_cancel_form.md) (function) — Builds the cancel form for a poll.
- [poll_view_voting()](../modules/poll/poll.module/poll_view_voting.md) (function) — Generates the voting form for a poll.
- [profile_admin_overview()](../modules/profile/profile.admin.inc/profile_admin_overview.md) (function) — Form builder to display a listing of all editable profile fields.
- [profile_field_form()](../modules/profile/profile.admin.inc/profile_field_form.md) (function) — Menu callback: Generate a form to add/edit a user profile field.
- [search_admin_settings()](../modules/search/search.admin.inc/search_admin_settings.md) (function) — Menu callback: displays the search module settings page.
- [search_box()](../modules/search/search.module/search_box.md) (function) — Form builder; Output a search form for the search block's search box.
- [shortcut_link_add()](../modules/shortcut/shortcut.admin.inc/shortcut_link_add.md) (function) — Form callback: builds the form for adding a new shortcut link.
- [shortcut_link_delete()](../modules/shortcut/shortcut.admin.inc/shortcut_link_delete.md) (function) — Form callback: builds the confirmation form for deleting a shortcut link.
- [shortcut_link_edit()](../modules/shortcut/shortcut.admin.inc/shortcut_link_edit.md) (function) — Form callback: builds the form for editing a shortcut link.
- [shortcut_set_add_form()](../modules/shortcut/shortcut.admin.inc/shortcut_set_add_form.md) (function) — Form callback: builds the form for adding a shortcut set.
- [shortcut_set_customize()](../modules/shortcut/shortcut.admin.inc/shortcut_set_customize.md) (function) — Form callback: builds the form for customizing shortcut sets.
- [shortcut_set_delete_form()](../modules/shortcut/shortcut.admin.inc/shortcut_set_delete_form.md) (function) — Form callback: builds the confirmation form for deleting a shortcut set.
- [shortcut_set_edit_form()](../modules/shortcut/shortcut.admin.inc/shortcut_set_edit_form.md) (function) — Form callback: builds the form for editing the shortcut set name.
- [shortcut_set_switch()](../modules/shortcut/shortcut.admin.inc/shortcut_set_switch.md) (function) — Form callback: builds the form for switching shortcut sets.
- [simpletest_settings_form()](../modules/simpletest/simpletest.pages.inc/simpletest_settings_form.md) (function) — Provides settings form for SimpleTest variables.
- [statistics_settings_form()](../modules/statistics/statistics.admin.inc/statistics_settings_form.md) (function) — Form constructor for the statistics administration form.
- [system_actions_delete_form()](../modules/system/system.admin.inc/system_actions_delete_form.md) (function) — Create the form for confirmation of deleting an action.
- [system_actions_manage_form()](../modules/system/system.admin.inc/system_actions_manage_form.md) (function) — Define the form for the actions overview page.
- [system_add_date_format_type_form()](../modules/system/system.admin.inc/system_add_date_format_type_form.md) (function) — Add new date type.
- [system_clean_url_settings()](../modules/system/system.admin.inc/system_clean_url_settings.md) (function) — Form builder; Configure clean URL settings.
- [system_clear_cache_submit()](../modules/system/system.admin.inc/system_clear_cache_submit.md) (function) — Submit callback; clear system caches.
- [system_clear_page_cache_submit()](../modules/system/system.admin.inc/system_clear_page_cache_submit.md) (function) — Submit callback; clear the page cache.
- [system_cron_settings()](../modules/system/system.admin.inc/system_cron_settings.md) (function) — Form builder; Cron form.
- [system_date_time_settings()](../modules/system/system.admin.inc/system_date_time_settings.md) (function) — Form builder; Configure the site date and time settings.
- [system_file_system_settings()](../modules/system/system.admin.inc/system_file_system_settings.md) (function) — Form builder; Configure the site file handling.
- [system_image_toolkit_settings()](../modules/system/system.admin.inc/system_image_toolkit_settings.md) (function) — Form builder; Configure site image toolkit usage.
- [system_ip_blocking_form()](../modules/system/system.admin.inc/system_ip_blocking_form.md) (function) — Define the form for blocking IP addresses.
- [system_logging_settings()](../modules/system/system.admin.inc/system_logging_settings.md) (function) — Form builder; Configure error reporting settings.
- [system_modules()](../modules/system/system.admin.inc/system_modules.md) (function) — Menu callback; provides module enable/disable interface.
- [system_modules_confirm_form()](../modules/system/system.admin.inc/system_modules_confirm_form.md) (function) — Display confirmation form for required modules.
- [system_modules_uninstall()](../modules/system/system.admin.inc/system_modules_uninstall.md) (function) — Builds a form of currently disabled modules.
- [system_modules_uninstall_confirm_form()](../modules/system/system.admin.inc/system_modules_uninstall_confirm_form.md) (function) — Confirm uninstall of selected modules.
- [system_performance_settings()](../modules/system/system.admin.inc/system_performance_settings.md) (function) — Form builder; Configure site performance settings.
- [system_regional_settings()](../modules/system/system.admin.inc/system_regional_settings.md) (function) — Form builder; Configure the site regional settings.
- [system_rss_feeds_settings()](../modules/system/system.admin.inc/system_rss_feeds_settings.md) (function) — Form builder; Configure how the site handles RSS feeds.
- [system_run_cron_submit()](../modules/system/system.admin.inc/system_run_cron_submit.md) (function) — Submit callback; run cron.
- [system_settings_form()](../modules/system/system.module/system_settings_form.md) (function) — Sets up a form to save information automatically.
- [system_site_information_settings()](../modules/system/system.admin.inc/system_site_information_settings.md) (function) — Form builder; The general site information form.
- [system_site_maintenance_mode()](../modules/system/system.admin.inc/system_site_maintenance_mode.md) (function) — Form builder; Configure the site's maintenance status.
- [system_theme_settings()](../modules/system/system.admin.inc/system_theme_settings.md) (function) — Form builder; display theme configuration for entire site and individual themes.
- [system_themes_admin_form()](../modules/system/system.admin.inc/system_themes_admin_form.md) (function) — Form to select the administration theme.
- [taxonomy_form_term()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_form_term.md) (function) — Form function for the term edit form.
- [taxonomy_form_vocabulary()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_form_vocabulary.md) (function) — Form builder for the vocabulary editing form.
- [taxonomy_overview_terms()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_overview_terms.md) (function) — Form builder for the taxonomy terms overview.
- [taxonomy_overview_vocabularies()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_overview_vocabularies.md) (function) — Form builder to list and manage vocabularies.
- [taxonomy_term_confirm_delete()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_term_confirm_delete.md) (function) — Form builder for the term delete form.
- [taxonomy_vocabulary_confirm_delete()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_vocabulary_confirm_delete.md) (function) — Form builder for the vocabulary delete confirmation form.
- [taxonomy_vocabulary_confirm_reset_alphabetical()](../modules/taxonomy/taxonomy.admin.inc/taxonomy_vocabulary_confirm_reset_alphabetical.md) (function) — Form builder to confirm resetting a vocabulary to alphabetical order.
- [trigger_assign_form()](../modules/trigger/trigger.admin.inc/trigger_assign_form.md) (function) — Returns the form for assigning an action to a trigger.
- [trigger_unassign()](../modules/trigger/trigger.admin.inc/trigger_unassign.md) (function) — Form constructor for confirmation page for removal of an assigned action.
- [update_manager_install_form()](../modules/update/update.manager.inc/update_manager_install_form.md) (function) — Form constructor for the install form of the Update Manager module.
- [update_manager_update_form()](../modules/update/update.manager.inc/update_manager_update_form.md) (function) — Form constructor for the update form of the Update Manager module.
- [update_manager_update_ready_form()](../modules/update/update.manager.inc/update_manager_update_ready_form.md) (function) — Form constructor for the update ready form.
- [update_settings()](../modules/update/update.settings.inc/update_settings.md) (function) — Form constructor for the update settings form.
- [user_admin_account()](../modules/user/user.admin.inc/user_admin_account.md) (function) — Form builder; User administration page.
- [user_admin_permissions()](../modules/user/user.admin.inc/user_admin_permissions.md) (function) — Menu callback: administer permissions.
- [user_admin_role()](../modules/user/user.admin.inc/user_admin_role.md) (function) — Form to configure a single role.
- [user_admin_roles()](../modules/user/user.admin.inc/user_admin_roles.md) (function) — Form to re-order roles or add a new one.
- [user_admin_settings()](../modules/user/user.admin.inc/user_admin_settings.md) (function) — Form builder; Configure user settings for this site.
- [user_cancel_confirm_form()](../modules/user/user.pages.inc/user_cancel_confirm_form.md) (function) — Form builder; confirm form for cancelling user account.
- [user_filter_form()](../modules/user/user.admin.inc/user_filter_form.md) (function) — Form builder; Return form for user administration filters.
- [user_login()](../modules/user/user.module/user_login.md) (function) — Form builder; the main user login form.
- [user_pass()](../modules/user/user.pages.inc/user_pass.md) (function) — Form builder; Request a password reset.
- [user_profile_form()](../modules/user/user.pages.inc/user_profile_form.md) (function) — Form builder; edit a user account or one of their profile categories.
- [user_register_form()](../modules/user/user.module/user_register_form.md) (function) — Form builder; the user registration form.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
