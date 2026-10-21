# modules/filter/filter.module

- **Source:** [local](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · 1824 lines
- **Module/theme:** filter

## File documentation

```text
@file
Framework for handling the filtering of content.
```

## Functions (derived index)

- [filter_help()](filter_help.md) — Implements hook_help().
- [filter_theme()](filter_theme.md) — Implements hook_theme().
- [filter_element_info()](filter_element_info.md) — Implements hook_element_info().
- [filter_menu()](filter_menu.md) — Implements hook_menu().
- [_filter_disable_format_access()](_filter_disable_format_access.md) — Access callback: Checks access for disabling text formats.
- [filter_format_load()](filter_format_load.md) — Loads a text format object from the database.
- [filter_format_save()](filter_format_save.md) — Saves a text format object to the database.
- [filter_format_disable()](filter_format_disable.md) — Disables a text format.
- [filter_format_exists()](filter_format_exists.md) — Determines if a text format exists.
- [filter_admin_format_title()](filter_admin_format_title.md) — Displays a text format form title.
- [filter_permission()](filter_permission.md) — Implements hook_permission().
- [filter_permission_name()](filter_permission_name.md) — Returns the machine-readable permission name for a provided text format.
- [filter_modules_enabled()](filter_modules_enabled.md) — Implements hook_modules_enabled().
- [filter_modules_disabled()](filter_modules_disabled.md) — Implements hook_modules_disabled().
- [filter_formats()](filter_formats.md) — Retrieves a list of text formats, ordered by weight.
- [filter_formats_reset()](filter_formats_reset.md) — Resets the text format caches.
- [filter_get_roles_by_format()](filter_get_roles_by_format.md) — Retrieves a list of roles that are allowed to use a given text format.
- [filter_get_formats_by_role()](filter_get_formats_by_role.md) — Retrieves a list of text formats that are allowed for a given role.
- [filter_default_format()](filter_default_format.md) — Returns the ID of the default text format for a particular user.
- [filter_fallback_format()](filter_fallback_format.md) — Returns the ID of the fallback text format that all users have access to.
- [filter_fallback_format_title()](filter_fallback_format_title.md) — Returns the title of the fallback text format.
- [filter_get_filters()](filter_get_filters.md) — Returns a list of all filters provided by modules.
- [_filter_list_cmp()](_filter_list_cmp.md) — Sorts an array of filters by filter name.
- [filter_format_allowcache()](filter_format_allowcache.md) — Checks if the text in a certain text format is allowed to be cached.
- [_filter_format_is_cacheable()](_filter_format_is_cacheable.md) — Helper function to determine whether the output of a given text format can be cached.
- [filter_list_format()](filter_list_format.md) — Retrieves a list of filters for a given text format.
- [check_markup()](check_markup.md) — Runs all the enabled filters on a piece of text.
- [filter_process_format()](filter_process_format.md) — Expands an element into a base element with text format selector attached.
- [filter_form_access_denied()](filter_form_access_denied.md) — Render API callback: Hides the field value of 'text_format' elements.
- [theme_text_format_wrapper()](theme_text_format_wrapper.md) — Returns HTML for a text format-enabled form element.
- [filter_access()](filter_access.md) — Checks if a user has access to a particular text format.
- [_filter_tips()](_filter_tips.md) — Retrieves the filter tips.
- [filter_dom_load()](filter_dom_load.md) — Parses an HTML snippet and returns it as a DOM object.
- [filter_dom_serialize()](filter_dom_serialize.md) — Converts a DOM object back to an HTML snippet.
- [filter_dom_serialize_escape_cdata_element()](filter_dom_serialize_escape_cdata_element.md) — Adds comments around the <!CDATA section in a dom element.
- [theme_filter_tips_more_info()](theme_filter_tips_more_info.md) — Returns HTML for a link to the more extensive filter tips.
- [theme_filter_guidelines()](theme_filter_guidelines.md) — Returns HTML for guidelines for a text format.
- [filter_filter_info()](filter_filter_info.md) — Implements hook_filter_info().
- [_filter_html_settings()](_filter_html_settings.md) — Implements callback_filter_settings().
- [_filter_html()](_filter_html.md) — Implements callback_filter_process().
- [_filter_html_tips()](_filter_html_tips.md) — Implements callback_filter_tips().
- [_filter_url_settings()](_filter_url_settings.md) — Implements callback_filter_settings().
- [_filter_url()](_filter_url.md) — Implements callback_filter_process().
- [_filter_url_parse_full_links()](_filter_url_parse_full_links.md) — Makes links out of absolute URLs.
- [_filter_url_parse_email_links()](_filter_url_parse_email_links.md) — Makes links out of e-mail addresses.
- [_filter_url_parse_partial_links()](_filter_url_parse_partial_links.md) — Makes links out of domain names starting with "www."
- [_filter_url_escape_comments()](_filter_url_escape_comments.md) — Escapes the contents of HTML comments.
- [_filter_url_trim()](_filter_url_trim.md) — Shortens long URLs to http://www.example.com/long/url...
- [_filter_url_tips()](_filter_url_tips.md) — Implements callback_filter_tips().
- [_filter_htmlcorrector()](_filter_htmlcorrector.md) — Implements callback_filter_process().
- [_filter_autop()](_filter_autop.md) — Implements callback_filter_process().
- [_filter_autop_tips()](_filter_autop_tips.md) — Implements callback_filter_tips().
- [_filter_html_escape()](_filter_html_escape.md) — Implements callback_filter_process().
- [_filter_html_escape_tips()](_filter_html_escape_tips.md) — Implements callback_filter_tips().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
