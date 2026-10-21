# includes/theme.inc

- **Source:** [local](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · 3054 lines

## File documentation

```text
@file
The theme system, which controls the output of Drupal.

The theme system allows for nearly all output of the Drupal system to be
customized by user themes.
```

## Functions (derived index)

- [drupal_theme_access()](drupal_theme_access.md) — Determines if a theme is available to use.
- [_drupal_theme_access()](_drupal_theme_access.md) — Helper function for determining access to a theme.
- [drupal_theme_initialize()](drupal_theme_initialize.md) — Initializes the theme system by loading the theme.
- [_drupal_theme_initialize()](_drupal_theme_initialize.md) — Initializes the theme system given already loaded information.
- [theme_get_registry()](theme_get_registry.md) — Gets the theme registry.
- [_theme_registry_callback()](_theme_registry_callback.md) — Sets the callback that will be used by theme_get_registry().
- [_theme_load_registry()](_theme_load_registry.md) — Gets the theme_registry cache; if it doesn't exist, builds it.
- [_theme_save_registry()](_theme_save_registry.md) — Writes the theme_registry cache into the database.
- [drupal_theme_rebuild()](drupal_theme_rebuild.md) — Forces the system to rebuild the theme registry.
- [_theme_process_registry()](_theme_process_registry.md) — Process a single implementation of hook_theme().
- [_theme_build_registry()](_theme_build_registry.md) — Builds the theme registry cache.
- [list_themes()](list_themes.md) — Returns a list of all currently available themes.
- [drupal_find_base_themes()](drupal_find_base_themes.md) — Find all the base themes for the specified theme.
- [theme()](theme.md) — Generates themed output.
- [path_to_theme()](path_to_theme.md) — Returns the path to the current themed element.
- [drupal_find_theme_functions()](drupal_find_theme_functions.md) — Allows themes and/or theme engines to discover overridden theme functions.
- [drupal_find_theme_templates()](drupal_find_theme_templates.md) — Allows themes and/or theme engines to easily discover overridden templates.
- [theme_get_setting()](theme_get_setting.md) — Retrieves a setting for the current theme or for a given theme.
- [theme_render_template()](theme_render_template.md) — Renders a system default template, which is essentially a PHP template.
- [_theme_render_template_debug()](_theme_render_template_debug.md) — Renders a template for any engine.
- [theme_enable()](theme_enable.md) — Enables a given list of themes.
- [theme_disable()](theme_disable.md) — Disables a given list of themes.
- [theme_status_messages()](theme_status_messages.md) — Returns HTML for status and/or error messages, grouped by type.
- [theme_link()](theme_link.md) — Returns HTML for a link.
- [theme_links()](theme_links.md) — Returns HTML for a set of links.
- [theme_image()](theme_image.md) — Returns HTML for an image.
- [theme_breadcrumb()](theme_breadcrumb.md) — Returns HTML for a breadcrumb trail.
- [theme_table()](theme_table.md) — Returns HTML for a table.
- [theme_tablesort_indicator()](theme_tablesort_indicator.md) — Returns HTML for a sort icon.
- [theme_mark()](theme_mark.md) — Returns HTML for a marker for new or updated content.
- [theme_item_list()](theme_item_list.md) — Returns HTML for a list or nested list of items.
- [theme_more_help_link()](theme_more_help_link.md) — Returns HTML for a "more help" link.
- [theme_feed_icon()](theme_feed_icon.md) — Returns HTML for a feed icon.
- [theme_html_tag()](theme_html_tag.md) — Returns HTML for a generic HTML tag with attributes.
- [theme_more_link()](theme_more_link.md) — Returns HTML for a "more" link, like those used in blocks.
- [theme_username()](theme_username.md) — Returns HTML for a username, potentially linked to the user's page.
- [theme_progress_bar()](theme_progress_bar.md) — Returns HTML for a progress bar.
- [theme_indentation()](theme_indentation.md) — Returns HTML for an indentation div; used for drag and drop tables.
- [_theme_table_cell()](_theme_table_cell.md) — Returns HTML output for a single table cell for theme_table().
- [template_preprocess()](template_preprocess.md) — Adds a default set of helper variables for variable processors and templates.
- [_template_preprocess_default_variables()](_template_preprocess_default_variables.md) — Returns hook-independent variables to template_preprocess().
- [template_process()](template_process.md) — Adds helper variables derived from variables defined during preprocessing.
- [template_preprocess_html()](template_preprocess_html.md) — Preprocess variables for html.tpl.php
- [template_preprocess_page()](template_preprocess_page.md) — Preprocess variables for page.tpl.php
- [template_process_page()](template_process_page.md) — Process variables for page.tpl.php
- [template_process_html()](template_process_html.md) — Process variables for html.tpl.php
- [theme_get_suggestions()](theme_get_suggestions.md) — Generate an array of suggestions from path arguments.
- [template_preprocess_maintenance_page()](template_preprocess_maintenance_page.md) — Process variables for maintenance-page.tpl.php.
- [template_process_maintenance_page()](template_process_maintenance_page.md) — Theme process function for theme_maintenance_field().
- [template_preprocess_region()](template_preprocess_region.md) — Preprocess variables for region.tpl.php
- [template_preprocess_username()](template_preprocess_username.md) — Preprocesses variables for theme_username().
- [template_process_username()](template_process_username.md) — Processes variables for theme_username().

## Classes and interfaces (derived index)

- [ThemeRegistry](ThemeRegistry.md) — Builds the run-time theme registry.

## Constants

### MARK_READ

- Line 21; topics: content_flags

```php
define('MARK_READ', 0);
```

```text
Mark content as read.
```

### MARK_NEW

- Line 26; topics: content_flags

```php
define('MARK_NEW', 1);
```

```text
Mark content as being new.
```

### MARK_UPDATED

- Line 31; topics: content_flags

```php
define('MARK_UPDATED', 2);
```

```text
Mark content as being updated.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
