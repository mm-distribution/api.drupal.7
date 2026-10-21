# includes/common.inc

- **Source:** [local](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · 8694 lines

## File documentation

```text
@file
Common functions that many Drupal modules will need to reference.

The functions that are critical and need to be available even when serving
a cached page are instead located in bootstrap.inc.
```

## Functions (derived index)

- [drupal_add_region_content()](drupal_add_region_content.md) — Adds content to a specified region.
- [drupal_get_region_content()](drupal_get_region_content.md) — Gets assigned content for a given region.
- [drupal_get_profile()](drupal_get_profile.md) — Gets the name of the currently active installation profile.
- [drupal_set_breadcrumb()](drupal_set_breadcrumb.md) — Sets the breadcrumb trail for the current page.
- [drupal_get_breadcrumb()](drupal_get_breadcrumb.md) — Gets the breadcrumb trail for the current page.
- [drupal_get_rdf_namespaces()](drupal_get_rdf_namespaces.md) — Returns a string containing RDF namespace declarations for use in XML and XHTML output.
- [drupal_add_html_head()](drupal_add_html_head.md) — Adds output to the HEAD tag of the HTML page.
- [_drupal_default_html_head()](_drupal_default_html_head.md) — Returns elements that are always displayed in the HEAD tag of the HTML page.
- [drupal_get_html_head()](drupal_get_html_head.md) — Retrieves output to be displayed in the HEAD tag of the HTML page.
- [drupal_add_feed()](drupal_add_feed.md) — Adds a feed URL for the current page.
- [drupal_get_feeds()](drupal_get_feeds.md) — Gets the feed URLs for the current page.
- [drupal_get_query_parameters()](drupal_get_query_parameters.md) — Processes a URL query parameter array to remove unwanted elements.
- [drupal_get_query_array()](drupal_get_query_array.md) — Splits a URL-encoded query string into an array.
- [drupal_http_build_query()](drupal_http_build_query.md) — Parses an array into a valid, rawurlencoded query string.
- [drupal_get_destination()](drupal_get_destination.md) — Prepares a 'destination' URL query parameter for use with drupal_goto().
- [drupal_parse_url()](drupal_parse_url.md) — Parses a URL string into its path, query, and fragment components.
- [drupal_encode_path()](drupal_encode_path.md) — Encodes a Drupal path for use in a URL.
- [drupal_goto()](drupal_goto.md) — Sends the user to a different page.
- [drupal_site_offline()](drupal_site_offline.md) — Delivers a "site is under maintenance" message to the browser.
- [drupal_not_found()](drupal_not_found.md) — Delivers a "page not found" error to the browser.
- [drupal_access_denied()](drupal_access_denied.md) — Delivers an "access denied" error to the browser.
- [drupal_http_request()](drupal_http_request.md) — Performs an HTTP request.
- [_drupal_should_strip_sensitive_headers_on_http_redirect()](_drupal_should_strip_sensitive_headers_on_http_redirect.md) — Determine whether to strip sensitive headers from a request when redirected.
- [_drupal_parse_response_status()](_drupal_parse_response_status.md) — Splits an HTTP response status line into components.
- [_drupal_http_use_proxy()](_drupal_http_use_proxy.md) — Helper function for determining hosts excluded from needing a proxy.
- [_fix_gpc_magic()](_fix_gpc_magic.md) — Strips slashes from a string or array of strings.
- [_fix_gpc_magic_files()](_fix_gpc_magic_files.md) — Strips slashes from $_FILES items.
- [fix_gpc_magic()](fix_gpc_magic.md) — Fixes double-escaping caused by "magic quotes" in some PHP installations.
- [valid_email_address()](valid_email_address.md) — Verifies the syntax of the given e-mail address.
- [valid_url()](valid_url.md) — Verifies the syntax of the given URL.
- [flood_register_event()](flood_register_event.md) — Registers an event for the current visitor to the flood control mechanism.
- [flood_clear_event()](flood_clear_event.md) — Makes the flood control mechanism forget an event for the current visitor.
- [flood_is_allowed()](flood_is_allowed.md) — Checks whether a user is allowed to proceed with the specified event.
- [drupal_strip_dangerous_protocols()](drupal_strip_dangerous_protocols.md) — Strips dangerous protocols (e.g. 'javascript:') from a URI.
- [check_url()](check_url.md) — Strips dangerous protocols from a URI and encodes it for output to HTML.
- [filter_xss_admin()](filter_xss_admin.md) — Applies a very permissive XSS/HTML filter for admin-only use.
- [filter_xss()](filter_xss.md) — Filters HTML to prevent cross-site-scripting (XSS) vulnerabilities.
- [_filter_xss_split()](_filter_xss_split.md) — Processes an HTML tag.
- [_filter_xss_attributes()](_filter_xss_attributes.md) — Processes a string of HTML attributes.
- [filter_xss_bad_protocol()](filter_xss_bad_protocol.md) — Processes an HTML attribute value and strips dangerous protocols from URLs.
- [format_rss_channel()](format_rss_channel.md) — Formats an RSS channel.
- [format_rss_item()](format_rss_item.md) — Formats a single RSS item.
- [format_xml_elements()](format_xml_elements.md) — Formats XML elements.
- [format_plural()](format_plural.md) — Formats a string containing a count of items.
- [parse_size()](parse_size.md) — Parses a given byte count.
- [format_size()](format_size.md) — Generates a string representation for the given byte count.
- [format_interval()](format_interval.md) — Formats a time interval with the requested granularity.
- [format_date()](format_date.md) — Formats a date, using a date type or a custom date format string.
- [date_iso8601()](date_iso8601.md) — Returns an ISO8601 formatted date based on the given date.
- [_format_date_callback()](_format_date_callback.md) — Translates a formatted date string.
- [format_username()](format_username.md) — Format a username.
- [url()](url.md) — Generates an internal or external URL.
- [url_is_external()](url_is_external.md) — Returns TRUE if a path is external to Drupal (e.g. http://example.com).
- [drupal_http_header_attributes()](drupal_http_header_attributes.md) — Formats an attribute string for an HTTP header.
- [drupal_attributes()](drupal_attributes.md) — Converts an associative array to an XML/HTML tag attribute string.
- [l()](l.md) — Formats an internal or external URL link as an HTML anchor tag.
- [drupal_deliver_page()](drupal_deliver_page.md) — Delivers a page callback result to the browser in the appropriate format.
- [drupal_deliver_html_page()](drupal_deliver_html_page.md) — Packages and sends the result of a page callback to the browser as HTML.
- [drupal_page_footer()](drupal_page_footer.md) — Performs end-of-request tasks.
- [drupal_exit()](drupal_exit.md) — Performs end-of-request tasks.
- [drupal_map_assoc()](drupal_map_assoc.md) — Forms an associative array from a linear array.
- [drupal_set_time_limit()](drupal_set_time_limit.md) — Attempts to set the PHP maximum execution time.
- [drupal_get_path()](drupal_get_path.md) — Returns the path to a system item (module, theme, etc.).
- [base_path()](base_path.md) — Returns the base URL path (i.e., directory) of the Drupal installation.
- [drupal_add_html_head_link()](drupal_add_html_head_link.md) — Adds a LINK tag with distinct attributes to the page's HEAD.
- [drupal_add_css()](drupal_add_css.md) — Adds a cascading stylesheet to the stylesheet queue.
- [drupal_get_css()](drupal_get_css.md) — Returns a themed representation of all stylesheets to attach to the page.
- [drupal_sort_css_js()](drupal_sort_css_js.md) — Sorts CSS and JavaScript resources.
- [drupal_group_css()](drupal_group_css.md) — Default callback to group CSS items.
- [drupal_aggregate_css()](drupal_aggregate_css.md) — Default callback to aggregate CSS files and inline content.
- [drupal_pre_render_styles()](drupal_pre_render_styles.md) — #pre_render callback to add the elements needed for CSS tags to be rendered.
- [drupal_build_css_cache()](drupal_build_css_cache.md) — Aggregates and optimizes CSS files into a cache file in the files directory.
- [_drupal_build_css_path()](_drupal_build_css_path.md) — Prefixes all paths within a CSS file for drupal_build_css_cache().
- [drupal_load_stylesheet()](drupal_load_stylesheet.md) — Loads the stylesheet and resolves all @import commands.
- [drupal_load_stylesheet_content()](drupal_load_stylesheet_content.md) — Processes the contents of a stylesheet for aggregation.
- [_drupal_load_stylesheet()](_drupal_load_stylesheet.md) — Loads stylesheets recursively and returns contents with corrected paths.
- [drupal_clear_css_cache()](drupal_clear_css_cache.md) — Deletes old cached CSS files.
- [drupal_delete_file_if_stale()](drupal_delete_file_if_stale.md) — Callback to delete files modified more than a set time ago.
- [drupal_clean_css_identifier()](drupal_clean_css_identifier.md) — Prepares a string for use as a CSS identifier (element, class, or ID name).
- [drupal_html_class()](drupal_html_class.md) — Prepares a string for use as a valid class name.
- [drupal_html_id()](drupal_html_id.md) — Prepares a string for use as a valid HTML ID and guarantees uniqueness.
- [drupal_region_class()](drupal_region_class.md) — Provides a standard HTML class name that identifies a page region.
- [drupal_add_js()](drupal_add_js.md) — Adds a JavaScript file, setting, or inline code to the page.
- [drupal_js_defaults()](drupal_js_defaults.md) — Constructs an array of the defaults that are used for JavaScript items.
- [drupal_get_js()](drupal_get_js.md) — Returns a themed presentation of all JavaScript code for the current page.
- [drupal_pre_render_scripts()](drupal_pre_render_scripts.md) — The #pre_render callback for the "scripts" element.
- [drupal_process_attached()](drupal_process_attached.md) — Adds attachments to a render() structure.
- [drupal_process_states()](drupal_process_states.md) — Adds JavaScript to change the state of an element based on another element.
- [drupal_add_library()](drupal_add_library.md) — Adds multiple JavaScript or CSS files at the same time.
- [drupal_get_library()](drupal_get_library.md) — Retrieves information for a JavaScript/CSS library.
- [drupal_add_tabledrag()](drupal_add_tabledrag.md) — Assists in adding the tableDrag JavaScript behavior to a themed table.
- [drupal_build_js_cache()](drupal_build_js_cache.md) — Aggregates JavaScript files into a cache file in the files directory.
- [drupal_clear_js_cache()](drupal_clear_js_cache.md) — Deletes old cached JavaScript files and variables.
- [drupal_json_encode()](drupal_json_encode.md) — Converts a PHP variable into its JavaScript equivalent.
- [drupal_json_decode()](drupal_json_decode.md) — Converts an HTML-safe JSON string into its PHP equivalent.
- [drupal_json_output()](drupal_json_output.md) — Returns data in JSON format.
- [drupal_get_private_key()](drupal_get_private_key.md) — Ensures the private key variable used to generate tokens is set.
- [drupal_get_token()](drupal_get_token.md) — Generates a token based on $value, the user session, and the private key.
- [drupal_valid_token()](drupal_valid_token.md) — Validates a token based on $value, the user session, and the private key.
- [_drupal_bootstrap_full()](_drupal_bootstrap_full.md)
- [drupal_page_set_cache()](drupal_page_set_cache.md) — Stores the current page in the cache.
- [drupal_cron_run()](drupal_cron_run.md) — Executes a cron run when called.
- [drupal_cron_cleanup()](drupal_cron_cleanup.md) — DEPRECATED: Shutdown function: Performs cron cleanup.
- [drupal_system_listing()](drupal_system_listing.md) — Returns information about system object files (modules, themes, etc.).
- [drupal_set_page_content()](drupal_set_page_content.md) — Sets the main page content value for later use.
- [drupal_pre_render_conditional_comments()](drupal_pre_render_conditional_comments.md) — #pre_render callback to render #browsers into #prefix and #suffix.
- [drupal_pre_render_link()](drupal_pre_render_link.md) — #pre_render callback to render a link into #markup.
- [drupal_pre_render_links()](drupal_pre_render_links.md) — #pre_render callback that collects child links into a single array.
- [drupal_pre_render_markup()](drupal_pre_render_markup.md) — #pre_render callback to append contents in #markup to #children.
- [drupal_render_page()](drupal_render_page.md) — Renders the page, including all theming.
- [drupal_render()](drupal_render.md) — Renders HTML given a structured array tree.
- [drupal_render_children()](drupal_render_children.md) — Renders children of an element and concatenates them.
- [render()](render.md) — Renders an element.
- [hide()](hide.md) — Hides an element from later rendering.
- [show()](show.md) — Shows a hidden element for later rendering.
- [drupal_render_cache_get()](drupal_render_cache_get.md) — Gets the rendered output of a renderable element from the cache.
- [drupal_render_cache_set()](drupal_render_cache_set.md) — Caches the rendered output of a renderable element.
- [drupal_render_collect_attached()](drupal_render_collect_attached.md) — Collects #attached for an element and its children into a single array.
- [drupal_render_cache_by_query()](drupal_render_cache_by_query.md) — Prepares an element for caching based on a query.
- [drupal_render_cid_parts()](drupal_render_cid_parts.md) — Returns cache ID parts for building a cache ID.
- [drupal_render_cid_create()](drupal_render_cid_create.md) — Creates the cache ID for a renderable element.
- [element_sort()](element_sort.md) — Function used by uasort to sort structured arrays by weight.
- [element_sort_by_title()](element_sort_by_title.md) — Array sorting callback; sorts elements by title.
- [element_info()](element_info.md) — Retrieves the default properties for the defined element type.
- [element_info_property()](element_info_property.md) — Retrieves a single property for the defined element type.
- [drupal_sort_weight()](drupal_sort_weight.md) — Sorts a structured array by the 'weight' element.
- [drupal_sort_title()](drupal_sort_title.md) — Array sorting callback; sorts elements by 'title' key.
- [element_property()](element_property.md) — Checks if the key is a property.
- [element_properties()](element_properties.md) — Gets properties of a structured array element (keys beginning with '#').
- [element_child()](element_child.md) — Checks if the key is a child.
- [element_children()](element_children.md) — Identifies the children of an element array, optionally sorted by weight.
- [element_get_visible_children()](element_get_visible_children.md) — Returns the visible children of an element.
- [element_set_attributes()](element_set_attributes.md) — Sets HTML attributes based on element properties.
- [drupal_array_diff_assoc_recursive()](drupal_array_diff_assoc_recursive.md) — Recursively computes the difference of arrays with additional index check.
- [drupal_array_set_nested_value()](drupal_array_set_nested_value.md) — Sets a value in a nested array with variable depth.
- [drupal_array_get_nested_value()](drupal_array_get_nested_value.md) — Retrieves a value from a nested array with variable depth.
- [drupal_array_nested_key_exists()](drupal_array_nested_key_exists.md) — Determines whether a nested array contains the requested keys.
- [drupal_common_theme()](drupal_common_theme.md) — Provides theme registration for themes across .inc files.
- [drupal_install_schema()](drupal_install_schema.md) — Creates all tables defined in a module's hook_schema().
- [drupal_uninstall_schema()](drupal_uninstall_schema.md) — Removes all tables defined in a module's hook_schema().
- [drupal_get_schema_unprocessed()](drupal_get_schema_unprocessed.md) — Returns the unprocessed and unaltered version of a module's schema.
- [_drupal_schema_initialize()](_drupal_schema_initialize.md) — Fills in required default values for table definitions from hook_schema().
- [drupal_schema_field_types()](drupal_schema_field_types.md) — Retrieves the type for every field in a table schema.
- [drupal_schema_fields_sql()](drupal_schema_fields_sql.md) — Retrieves a list of fields from a table schema.
- [drupal_write_record()](drupal_write_record.md) — Saves (inserts or updates) a record to the database based upon the schema.
- [drupal_parse_info_file()](drupal_parse_info_file.md) — Parses Drupal module and theme .info files.
- [drupal_parse_info_format()](drupal_parse_info_format.md) — Parses data in Drupal's .info format.
- [watchdog_severity_levels()](watchdog_severity_levels.md) — Returns a list of severity levels, as defined in RFC 3164.
- [drupal_explode_tags()](drupal_explode_tags.md) — Explodes a string of tags into an array.
- [drupal_implode_tags()](drupal_implode_tags.md) — Implodes an array of tags into a string.
- [drupal_flush_all_caches()](drupal_flush_all_caches.md) — Flushes all cached data on the site.
- [_drupal_flush_css_js()](_drupal_flush_css_js.md) — Changes the dummy query string added to all CSS and JavaScript files.
- [debug()](debug.md) — Outputs debug information.
- [drupal_parse_dependency()](drupal_parse_dependency.md) — Parses a dependency for comparison by drupal_check_incompatibility().
- [drupal_check_incompatibility()](drupal_check_incompatibility.md) — Checks whether a version is compatible with a given dependency.
- [entity_get_info()](entity_get_info.md) — Get the entity info array of an entity type.
- [entity_info_cache_clear()](entity_info_cache_clear.md) — Resets the cached information about entity types.
- [entity_extract_ids()](entity_extract_ids.md) — Helper function to extract id, vid, and bundle name from an entity.
- [entity_create_stub_entity()](entity_create_stub_entity.md) — Helper function to assemble an object structure with initial ids.
- [entity_load()](entity_load.md) — Load entities from the database.
- [entity_load_unchanged()](entity_load_unchanged.md) — Loads the unchanged, i.e. not modified, entity from the database.
- [entity_get_controller()](entity_get_controller.md) — Gets the entity controller for an entity type.
- [entity_prepare_view()](entity_prepare_view.md) — Invoke hook_entity_prepare_view().
- [entity_view_mode_prepare()](entity_view_mode_prepare.md) — Invoke hook_entity_view_mode_alter().
- [entity_uri()](entity_uri.md) — Returns the URI elements of an entity.
- [entity_label()](entity_label.md) — Returns the label of an entity.
- [entity_language()](entity_language.md) — Returns the language of an entity.
- [entity_form_field_validate()](entity_form_field_validate.md) — Attaches field API validation to entity forms.
- [entity_form_submit_build_entity()](entity_form_submit_build_entity.md) — Copies submitted values to entity properties for simple entity forms.
- [xmlrpc()](xmlrpc.md) — Performs one or more XML-RPC request(s).
- [archiver_get_info()](archiver_get_info.md) — Retrieves a list of all available archivers.
- [archiver_get_extensions()](archiver_get_extensions.md) — Returns a string of supported archive extensions.
- [archiver_get_archiver()](archiver_get_archiver.md) — Creates the appropriate archiver for the specified file.
- [drupal_get_updaters()](drupal_get_updaters.md) — Assembles the Drupal Updater registry.
- [drupal_get_filetransfer_info()](drupal_get_filetransfer_info.md) — Assembles the Drupal FileTransfer registry.

## Constants

### SAVED_NEW

- Line 45

```php
define('SAVED_NEW', 1);
```

```text
Return status for saving which involved creating a new item.
```

### SAVED_UPDATED

- Line 50

```php
define('SAVED_UPDATED', 2);
```

```text
Return status for saving which involved an update to an existing item.
```

### SAVED_DELETED

- Line 55

```php
define('SAVED_DELETED', 3);
```

```text
Return status for saving which deleted an existing item.
```

### CSS_SYSTEM

- Line 60

```php
define('CSS_SYSTEM', -100);
```

```text
The default group for system CSS files added to the page.
```

### CSS_DEFAULT

- Line 65

```php
define('CSS_DEFAULT', 0);
```

```text
The default group for module CSS files added to the page.
```

### CSS_THEME

- Line 70

```php
define('CSS_THEME', 100);
```

```text
The default group for theme CSS files added to the page.
```

### JS_LIBRARY

- Line 75

```php
define('JS_LIBRARY', -100);
```

```text
The default group for JavaScript and jQuery libraries added to the page.
```

### JS_DEFAULT

- Line 80

```php
define('JS_DEFAULT', 0);
```

```text
The default group for module JavaScript code added to the page.
```

### JS_THEME

- Line 85

```php
define('JS_THEME', 100);
```

```text
The default group for theme JavaScript code added to the page.
```

### HTTP_REQUEST_TIMEOUT

- Line 92

```php
define('HTTP_REQUEST_TIMEOUT', -1);
```

```text
Error code indicating that the request exceeded the specified timeout.

@see drupal_http_request()
```

### DRUPAL_NO_CACHE

- Line 127; topics: block_caching

```php
define('DRUPAL_NO_CACHE', -1);
```

```text
The block should not get cached.

This setting should be used:
- For simple blocks (notably those that do not perform any db query), where
  querying the db cache would be more expensive than directly generating the
  content.
- For blocks that change too frequently.
```

### DRUPAL_CACHE_CUSTOM

- Line 135; topics: block_caching

```php
define('DRUPAL_CACHE_CUSTOM', -2);
```

```text
The block is handling its own caching in its hook_block_view().

This setting is useful when time based expiration is needed or a site uses a
node access which invalidates standard block cache.
```

### DRUPAL_CACHE_PER_ROLE

- Line 143; topics: block_caching

```php
define('DRUPAL_CACHE_PER_ROLE', 0x0001);
```

```text
The block or element can change depending on the user's roles.

This is the default setting for blocks, used when the block does not specify
anything.
```

### DRUPAL_CACHE_PER_USER

- Line 151; topics: block_caching

```php
define('DRUPAL_CACHE_PER_USER', 0x0002);
```

```text
The block or element can change depending on the user.

This setting can be resource-consuming for sites with large number of users,
and thus should only be used when DRUPAL_CACHE_PER_ROLE is not sufficient.
```

### DRUPAL_CACHE_PER_PAGE

- Line 156; topics: block_caching

```php
define('DRUPAL_CACHE_PER_PAGE', 0x0004);
```

```text
The block or element can change depending on the page being viewed.
```

### DRUPAL_CACHE_GLOBAL

- Line 161; topics: block_caching

```php
define('DRUPAL_CACHE_GLOBAL', 0x0008);
```

```text
The block or element is the same for every user and page that it is visible.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
