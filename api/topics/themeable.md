# Default theme implementations

- **Topic id:** `themeable`
- **Defined in:** [`modules/system/theme.api.php`](../modules/system/theme.api.php/_file.md), line 3 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L3)

## Documentation

```text
@defgroup themeable Default theme implementations
@{
Functions and templates for the user interface to be implemented by themes.

Drupal's presentation layer is a pluggable system known as the theme
layer. Each theme can take control over most of Drupal's output, and
has complete control over the CSS.

Inside Drupal, the theme layer is utilized by the use of the theme()
function, which is passed the name of a component (the theme hook)
and an array of variables. For example,
theme('table', array('header' => $header, 'rows' => $rows));
Additionally, the theme() function can take an array of theme
hooks, which can be used to provide 'fallback' implementations to
allow for more specific control of output. For example, the function:
theme(array('table__foo', 'table'), $variables) would look to see if
'table__foo' is registered anywhere; if it is not, it would 'fall back'
to the generic 'table' implementation. This can be used to attach specific
theme functions to named objects, allowing the themer more control over
specific types of output.

As of Drupal 6, every theme hook is required to be registered by the
module that owns it, so that Drupal can tell what to do with it and
to make it simple for themes to identify and override the behavior
for these calls.

The theme hooks are registered via hook_theme(), which returns an
array of arrays with information about the hook. It describes the
arguments the function or template will need, and provides
defaults for the template in case they are not filled in. If the default
implementation is a function, by convention it is named theme_HOOK().

Each module should provide a default implementation for theme_hooks that
it registers. This implementation may be either a function or a template;
if it is a function it must be specified via hook_theme(). By convention,
default implementations of theme hooks are named theme_HOOK. Default
template implementations are stored in the module directory.

Drupal's default template renderer is a simple PHP parsing engine that
includes the template and stores the output. Drupal's theme engines
can provide alternate template engines, such as XTemplate, Smarty and
PHPTal. The most common template engine is PHPTemplate (included with
Drupal and implemented in phptemplate.engine, which uses Drupal's default
template renderer.

In order to create theme-specific implementations of these hooks, themes can
implement their own version of theme hooks, either as functions or templates.
These implementations will be used instead of the default implementation. If
using a pure .theme without an engine, the .theme is required to implement
its own version of hook_theme() to tell Drupal what it is implementing;
themes utilizing an engine will have their well-named theming functions
automatically registered for them. While this can vary based upon the theme
engine, the standard set by phptemplate is that theme functions should be
named THEMENAME_HOOK. For example, for Drupal's default theme (Bartik) to
implement the 'table' hook, the phptemplate.engine would find
bartik_table().

The theme system is described and defined in theme.inc.

@see theme()
@see hook_theme()
@see hooks
@see callbacks

@} End of "defgroup themeable".
```

## Members (derived, 143)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [theme_admin_block()](../modules/system/system.admin.inc/theme_admin_block.md) (function) — Returns HTML for an administrative block for display.
- [theme_admin_block_content()](../modules/system/system.admin.inc/theme_admin_block_content.md) (function) — Returns HTML for the content of an administrative block.
- [theme_admin_page()](../modules/system/system.admin.inc/theme_admin_page.md) (function) — Returns HTML for an administrative page.
- [theme_aggregator_block_item()](../modules/aggregator/aggregator.module/theme_aggregator_block_item.md) (function) — Returns HTML for an individual feed item for display in the block.
- [theme_aggregator_categorize_items()](../modules/aggregator/aggregator.pages.inc/theme_aggregator_categorize_items.md) (function) — Returns HTML for the aggregator page list form for assigning categories.
- [theme_aggregator_page_opml()](../modules/aggregator/aggregator.pages.inc/theme_aggregator_page_opml.md) (function) — Prints the OPML page for the feed.
- [theme_aggregator_page_rss()](../modules/aggregator/aggregator.pages.inc/theme_aggregator_page_rss.md) (function) — Prints the RSS page for a feed.
- [theme_authorize_message()](../includes/theme.maintenance.inc/theme_authorize_message.md) (function) — Returns HTML for a single log message from the authorize.php batch operation.
- [theme_authorize_report()](../includes/theme.maintenance.inc/theme_authorize_report.md) (function) — Returns HTML for a results report of an operation run by authorize.php.
- [theme_book_admin_table()](../modules/book/book.admin.inc/theme_book_admin_table.md) (function) — Returns HTML for a book administration form.
- [theme_book_title_link()](../modules/book/book.module/theme_book_title_link.md) (function) — Returns HTML for a link to a book title when used as a block title.
- [theme_breadcrumb()](../includes/theme.inc/theme_breadcrumb.md) (function) — Returns HTML for a breadcrumb trail.
- [theme_button()](../includes/form.inc/theme_button.md) (function) — Returns HTML for a button form element.
- [theme_checkbox()](../includes/form.inc/theme_checkbox.md) (function) — Returns HTML for a checkbox form element.
- [theme_checkboxes()](../includes/form.inc/theme_checkboxes.md) (function) — Returns HTML for a set of checkbox form elements.
- [theme_color_scheme_form()](../modules/color/color.module/theme_color_scheme_form.md) (function) — Returns HTML for a theme's color form.
- [theme_comment_block()](../modules/comment/comment.module/theme_comment_block.md) (function) — Returns HTML for a list of recent comments to be displayed in the comment block.
- [theme_comment_post_forbidden()](../modules/comment/comment.module/theme_comment_post_forbidden.md) (function) — Returns HTML for a "you can't post comments" notice.
- [theme_confirm_form()](../modules/system/system.module/theme_confirm_form.md) (function) — Returns HTML for a confirmation form.
- [theme_container()](../includes/form.inc/theme_container.md) (function) — Returns HTML to wrap child elements in a container.
- [theme_dashboard()](../modules/dashboard/dashboard.module/theme_dashboard.md) (function) — Returns HTML for the entire dashboard.
- [theme_dashboard_admin()](../modules/dashboard/dashboard.module/theme_dashboard_admin.md) (function) — Returns HTML for the non-customizable part of the dashboard page.
- [theme_dashboard_disabled_block()](../modules/dashboard/dashboard.module/theme_dashboard_disabled_block.md) (function) — Returns HTML for disabled blocks, for use in dashboard customization mode.
- [theme_dashboard_disabled_blocks()](../modules/dashboard/dashboard.module/theme_dashboard_disabled_blocks.md) (function) — Returns HTML for disabled blocks, for use in dashboard customization mode.
- [theme_dashboard_region()](../modules/dashboard/dashboard.module/theme_dashboard_region.md) (function) — Returns HTML for a generic dashboard region.
- [theme_date()](../includes/form.inc/theme_date.md) (function) — Returns HTML for a date selection form element.
- [theme_dblog_message()](../modules/dblog/dblog.admin.inc/theme_dblog_message.md) (function) — Returns HTML for a log message.
- [theme_exposed_filters()](../modules/system/system.module/theme_exposed_filters.md) (function) — Returns HTML for an exposed filter form.
- [theme_feed_icon()](../includes/theme.inc/theme_feed_icon.md) (function) — Returns HTML for a feed icon.
- [theme_field()](../modules/field/field.module/theme_field.md) (function) — Returns HTML for a field.
- [theme_field_multiple_value_form()](../modules/field/field.form.inc/theme_field_multiple_value_form.md) (function) — Returns HTML for an individual form element.
- [theme_field_ui_table()](../modules/field_ui/field_ui.admin.inc/theme_field_ui_table.md) (function) — Returns HTML for Field UI overview tables.
- [theme_fieldset()](../includes/form.inc/theme_fieldset.md) (function) — Returns HTML for a fieldset form element and its children.
- [theme_file()](../includes/form.inc/theme_file.md) (function) — Returns HTML for a file upload form element.
- [theme_file_formatter_table()](../modules/file/file.field.inc/theme_file_formatter_table.md) (function) — Returns HTML for a file attachments table.
- [theme_file_icon()](../modules/file/file.module/theme_file_icon.md) (function) — Returns HTML for an image with an appropriate icon for the given file.
- [theme_file_link()](../modules/file/file.module/theme_file_link.md) (function) — Returns HTML for a link to a file.
- [theme_file_managed_file()](../modules/file/file.module/theme_file_managed_file.md) (function) — Returns HTML for a managed file element.
- [theme_file_upload_help()](../modules/file/file.field.inc/theme_file_upload_help.md) (function) — Returns HTML for help text based on file upload validators.
- [theme_file_widget()](../modules/file/file.field.inc/theme_file_widget.md) (function) — Returns HTML for an individual file upload widget.
- [theme_file_widget_multiple()](../modules/file/file.field.inc/theme_file_widget_multiple.md) (function) — Returns HTML for a group of file upload widgets.
- [theme_filter_admin_format_filter_order()](../modules/filter/filter.admin.inc/theme_filter_admin_format_filter_order.md) (function) — Returns HTML for a text format's filter order form.
- [theme_filter_admin_overview()](../modules/filter/filter.admin.inc/theme_filter_admin_overview.md) (function) — Returns HTML for the text format administration overview form.
- [theme_filter_guidelines()](../modules/filter/filter.module/theme_filter_guidelines.md) (function) — Returns HTML for guidelines for a text format.
- [theme_filter_tips()](../modules/filter/filter.pages.inc/theme_filter_tips.md) (function) — Returns HTML for a set of filter tips.
- [theme_filter_tips_more_info()](../modules/filter/filter.module/theme_filter_tips_more_info.md) (function) — Returns HTML for a link to the more extensive filter tips.
- [theme_form()](../includes/form.inc/theme_form.md) (function) — Returns HTML for a form.
- [theme_form_element()](../includes/form.inc/theme_form_element.md) (function) — Returns HTML for a form element.
- [theme_form_element_label()](../includes/form.inc/theme_form_element_label.md) (function) — Returns HTML for a form element label and required marker.
- [theme_form_required_marker()](../includes/form.inc/theme_form_required_marker.md) (function) — Returns HTML for a marker for required form elements.
- [theme_forum_form()](../modules/forum/forum.admin.inc/theme_forum_form.md) (function) — Returns HTML for a forum form.
- [theme_hidden()](../includes/form.inc/theme_hidden.md) (function) — Returns HTML for a hidden form element.
- [theme_html_tag()](../includes/theme.inc/theme_html_tag.md) (function) — Returns HTML for a generic HTML tag with attributes.
- [theme_image()](../includes/theme.inc/theme_image.md) (function) — Returns HTML for an image.
- [theme_image_anchor()](../modules/image/image.admin.inc/theme_image_anchor.md) (function) — Returns HTML for a 3x3 grid of checkboxes for image anchors.
- [theme_image_button()](../includes/form.inc/theme_image_button.md) (function) — Returns HTML for an image button form element.
- [theme_image_crop_summary()](../modules/image/image.admin.inc/theme_image_crop_summary.md) (function) — Returns HTML for a summary of an image crop effect.
- [theme_image_formatter()](../modules/image/image.field.inc/theme_image_formatter.md) (function) — Returns HTML for an image field formatter.
- [theme_image_resize_summary()](../modules/image/image.admin.inc/theme_image_resize_summary.md) (function) — Returns HTML for a summary of an image resize effect.
- [theme_image_rotate_summary()](../modules/image/image.admin.inc/theme_image_rotate_summary.md) (function) — Returns HTML for a summary of an image rotate effect.
- [theme_image_scale_summary()](../modules/image/image.admin.inc/theme_image_scale_summary.md) (function) — Returns HTML for a summary of an image scale effect.
- [theme_image_style()](../modules/image/image.module/theme_image_style.md) (function) — Returns HTML for an image using a specific image style.
- [theme_image_style_effects()](../modules/image/image.admin.inc/theme_image_style_effects.md) (function) — Returns HTML for a listing of the effects within a specific image style.
- [theme_image_style_list()](../modules/image/image.admin.inc/theme_image_style_list.md) (function) — Returns HTML for the page containing the list of image styles.
- [theme_image_style_preview()](../modules/image/image.admin.inc/theme_image_style_preview.md) (function) — Returns HTML for a preview of an image style.
- [theme_image_widget()](../modules/image/image.field.inc/theme_image_widget.md) (function) — Returns HTML for an image field widget.
- [theme_indentation()](../includes/theme.inc/theme_indentation.md) (function) — Returns HTML for an indentation div; used for drag and drop tables.
- [theme_item_list()](../includes/theme.inc/theme_item_list.md) (function) — Returns HTML for a list or nested list of items.
- [theme_link()](../includes/theme.inc/theme_link.md) (function) — Returns HTML for a link.
- [theme_links()](../includes/theme.inc/theme_links.md) (function) — Returns HTML for a set of links.
- [theme_locale_date_format_form()](../modules/locale/locale.admin.inc/theme_locale_date_format_form.md) (function) — Returns HTML for a locale date format form.
- [theme_locale_languages_configure_form()](../modules/locale/locale.admin.inc/theme_locale_languages_configure_form.md) (function) — Returns HTML for a language configuration form.
- [theme_locale_languages_overview_form()](../modules/locale/locale.admin.inc/theme_locale_languages_overview_form.md) (function) — Returns HTML for the language overview form.
- [theme_mark()](../includes/theme.inc/theme_mark.md) (function) — Returns HTML for a marker for new or updated content.
- [theme_menu_admin_overview()](../modules/menu/menu.admin.inc/theme_menu_admin_overview.md) (function) — Returns HTML for a menu title and description for the menu overview page.
- [theme_menu_link()](../includes/menu.inc/theme_menu_link.md) (function) — Returns HTML for a menu link and submenu.
- [theme_menu_local_action()](../includes/menu.inc/theme_menu_local_action.md) (function) — Returns HTML for a single local action link.
- [theme_menu_local_task()](../includes/menu.inc/theme_menu_local_task.md) (function) — Returns HTML for a single local task link.
- [theme_menu_local_tasks()](../includes/menu.inc/theme_menu_local_tasks.md) (function) — Returns HTML for primary and secondary local tasks.
- [theme_menu_overview_form()](../modules/menu/menu.admin.inc/theme_menu_overview_form.md) (function) — Returns HTML for the menu overview form into a table.
- [theme_menu_tree()](../includes/menu.inc/theme_menu_tree.md) (function) — Returns HTML for a wrapper for a menu sub-tree.
- [theme_more_help_link()](../includes/theme.inc/theme_more_help_link.md) (function) — Returns HTML for a "more help" link.
- [theme_more_link()](../includes/theme.inc/theme_more_link.md) (function) — Returns HTML for a "more" link, like those used in blocks.
- [theme_node_add_list()](../modules/node/node.pages.inc/theme_node_add_list.md) (function) — Returns HTML for a list of available node types for node creation.
- [theme_node_admin_overview()](../modules/node/content_types.inc/theme_node_admin_overview.md) (function) — Returns HTML for a node type description for the content type admin overview page.
- [theme_node_preview()](../modules/node/node.pages.inc/theme_node_preview.md) (function) — Returns HTML for a node preview for display during node creation and editing.
- [theme_node_recent_block()](../modules/node/node.module/theme_node_recent_block.md) (function) — Returns HTML for a list of recent content.
- [theme_node_recent_content()](../modules/node/node.module/theme_node_recent_content.md) (function) — Returns HTML for a recent node to be displayed in the recent content block.
- [theme_node_search_admin()](../modules/node/node.module/theme_node_search_admin.md) (function) — Returns HTML for the content ranking part of the search settings admin page.
- [theme_options_none()](../modules/field/modules/options/options.module/theme_options_none.md) (function) — Returns HTML for the label for the empty value for options that are not required.
- [theme_overlay_disable_message()](../modules/overlay/overlay.module/theme_overlay_disable_message.md) (function) — Returns the HTML for the message about how to disable the overlay.
- [theme_pager()](../includes/pager.inc/theme_pager.md) (function) — Returns HTML for a query pager.
- [theme_pager_first()](../includes/pager.inc/theme_pager_first.md) (function) — Returns HTML for the "first page" link in a query pager.
- [theme_pager_last()](../includes/pager.inc/theme_pager_last.md) (function) — Returns HTML for the "last page" link in query pager.
- [theme_pager_link()](../includes/pager.inc/theme_pager_link.md) (function) — Returns HTML for a link to a specific query result page.
- [theme_pager_next()](../includes/pager.inc/theme_pager_next.md) (function) — Returns HTML for the "next page" link in a query pager.
- [theme_pager_previous()](../includes/pager.inc/theme_pager_previous.md) (function) — Returns HTML for the "previous page" link in a query pager.
- [theme_password()](../includes/form.inc/theme_password.md) (function) — Returns HTML for a password form element.
- [theme_poll_choices()](../modules/poll/poll.module/theme_poll_choices.md) (function) — Returns HTML for an admin poll form for choices.
- [theme_profile_admin_overview()](../modules/profile/profile.admin.inc/theme_profile_admin_overview.md) (function) — Returns HTML for the profile field overview form into a drag and drop enabled table.
- [theme_progress_bar()](../includes/theme.inc/theme_progress_bar.md) (function) — Returns HTML for a progress bar.
- [theme_radio()](../includes/form.inc/theme_radio.md) (function) — Returns HTML for a radio button form element.
- [theme_radios()](../includes/form.inc/theme_radios.md) (function) — Returns HTML for a set of radio button form elements.
- [theme_rdf_metadata()](../modules/rdf/rdf.module/theme_rdf_metadata.md) (function) — Returns HTML for a series of empty spans for exporting RDF metadata in RDFa.
- [theme_rdf_template_variable_wrapper()](../modules/rdf/rdf.module/theme_rdf_template_variable_wrapper.md) (function) — Returns HTML for a template variable wrapped in an HTML element with the RDF attributes.
- [theme_select()](../includes/form.inc/theme_select.md) (function) — Returns HTML for a select form element.
- [theme_shortcut_set_customize()](../modules/shortcut/shortcut.admin.inc/theme_shortcut_set_customize.md) (function) — Returns HTML for a shortcut set customization form.
- [theme_simpletest_result_summary()](../modules/simpletest/simpletest.pages.inc/theme_simpletest_result_summary.md) (function) — Returns HTML for the summary status of a simpletest result.
- [theme_simpletest_test_table()](../modules/simpletest/simpletest.pages.inc/theme_simpletest_test_table.md) (function) — Returns HTML for a test list generated by simpletest_test_form() into a table.
- [theme_status_messages()](../includes/theme.inc/theme_status_messages.md) (function) — Returns HTML for status and/or error messages, grouped by type.
- [theme_status_report()](../modules/system/system.admin.inc/theme_status_report.md) (function) — Returns HTML for the status report.
- [theme_submit()](../includes/form.inc/theme_submit.md) (function) — Returns HTML for a submit button form element.
- [theme_system_admin_index()](../modules/system/system.admin.inc/theme_system_admin_index.md) (function) — Returns HTML for the output of the dashboard page.
- [theme_system_compact_link()](../modules/system/system.module/theme_system_compact_link.md) (function) — Returns HTML for a link to show or hide inline help descriptions.
- [theme_system_date_time_settings()](../modules/system/system.admin.inc/theme_system_date_time_settings.md) (function) — Returns HTML for the date settings form.
- [theme_system_modules_fieldset()](../modules/system/system.admin.inc/theme_system_modules_fieldset.md) (function) — Returns HTML for the modules form.
- [theme_system_modules_incompatible()](../modules/system/system.admin.inc/theme_system_modules_incompatible.md) (function) — Returns HTML for a message about incompatible modules.
- [theme_system_modules_uninstall()](../modules/system/system.admin.inc/theme_system_modules_uninstall.md) (function) — Returns HTML for a table of currently disabled modules.
- [theme_system_powered_by()](../modules/system/system.module/theme_system_powered_by.md) (function) — Returns HTML for the Powered by Drupal text.
- [theme_system_settings_form()](../modules/system/system.module/theme_system_settings_form.md) (function) — Returns HTML for a system settings form.
- [theme_system_themes_page()](../modules/system/system.admin.inc/theme_system_themes_page.md) (function) — Returns HTML for the Appearance page.
- [theme_table()](../includes/theme.inc/theme_table.md) (function) — Returns HTML for a table.
- [theme_tableselect()](../includes/form.inc/theme_tableselect.md) (function) — Returns HTML for a table with radio buttons or checkboxes.
- [theme_tablesort_indicator()](../includes/theme.inc/theme_tablesort_indicator.md) (function) — Returns HTML for a sort icon.
- [theme_task_list()](../includes/theme.maintenance.inc/theme_task_list.md) (function) — Returns HTML for a list of maintenance tasks to perform.
- [theme_taxonomy_overview_terms()](../modules/taxonomy/taxonomy.admin.inc/theme_taxonomy_overview_terms.md) (function) — Returns HTML for a terms overview form as a sortable list of terms.
- [theme_taxonomy_overview_vocabularies()](../modules/taxonomy/taxonomy.admin.inc/theme_taxonomy_overview_vocabularies.md) (function) — Returns HTML for the vocabulary overview form as a sortable list of vocabularies.
- [theme_text_format_wrapper()](../modules/filter/filter.module/theme_text_format_wrapper.md) (function) — Returns HTML for a text format-enabled form element.
- [theme_textarea()](../includes/form.inc/theme_textarea.md) (function) — Returns HTML for a textarea form element.
- [theme_textfield()](../includes/form.inc/theme_textfield.md) (function) — Returns HTML for a textfield form element.
- [theme_trigger_display()](../modules/trigger/trigger.admin.inc/theme_trigger_display.md) (function) — Returns HTML for the form showing actions assigned to a trigger.
- [theme_update_last_check()](../modules/update/update.module/theme_update_last_check.md) (function) — Returns HTML for the last time we checked for update data.
- [theme_update_manager_update_form()](../modules/update/update.manager.inc/theme_update_manager_update_form.md) (function) — Returns HTML for the first page in the process of updating projects.
- [theme_update_report()](../modules/update/update.report.inc/theme_update_report.md) (function) — Returns HTML for the project status report.
- [theme_update_status_label()](../modules/update/update.report.inc/theme_update_status_label.md) (function) — Returns HTML for a label to display for a project's update status.
- [theme_update_version()](../modules/update/update.report.inc/theme_update_version.md) (function) — Returns HTML for the version display of a project.
- [theme_user_admin_permissions()](../modules/user/user.admin.inc/theme_user_admin_permissions.md) (function) — Returns HTML for the administer permissions page.
- [theme_user_admin_roles()](../modules/user/user.admin.inc/theme_user_admin_roles.md) (function) — Returns HTML for the role order and new role form.
- [theme_user_list()](../modules/user/user.module/theme_user_list.md) (function) — Returns HTML for a list of users.
- [theme_user_permission_description()](../modules/user/user.admin.inc/theme_user_permission_description.md) (function) — Returns HTML for an individual permission description.
- [theme_user_signature()](../modules/user/user.module/theme_user_signature.md) (function) — Returns HTML for a user signature.
- [theme_username()](../includes/theme.inc/theme_username.md) (function) — Returns HTML for a username, potentially linked to the user's page.
- [theme_vertical_tabs()](../includes/form.inc/theme_vertical_tabs.md) (function) — Returns HTML for an element's children fieldsets as vertical tabs.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
