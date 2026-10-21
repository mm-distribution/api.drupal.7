# includes/ajax.inc

- **Source:** [local](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · 1319 lines

## File documentation

```text
@file
Functions for use with Drupal's Ajax framework.
```

## Functions (derived index)

- [ajax_render()](ajax_render.md) — Renders a commands array into JSON.
- [ajax_get_form()](ajax_get_form.md) — Gets a form submitted via #ajax during an Ajax callback.
- [ajax_form_callback()](ajax_form_callback.md) — Menu callback; handles Ajax requests for the #ajax Form API property.
- [ajax_base_page_theme()](ajax_base_page_theme.md) — Theme callback for Ajax requests.
- [ajax_deliver()](ajax_deliver.md) — Packages and sends the result of a page callback as an Ajax response.
- [ajax_prepare_response()](ajax_prepare_response.md) — Converts the return value of a page callback into an Ajax commands array.
- [ajax_set_verification_header()](ajax_set_verification_header.md) — Sets a response header for ajax.js to trust the response body.
- [ajax_footer()](ajax_footer.md) — Performs end-of-Ajax-request tasks.
- [ajax_process_form()](ajax_process_form.md) — Form element processing handler for the #ajax form property.
- [ajax_pre_render_element()](ajax_pre_render_element.md) — Adds Ajax information about an element to communicate with JavaScript.
- [ajax_command_alert()](ajax_command_alert.md) — Creates a Drupal Ajax 'alert' command.
- [ajax_command_insert()](ajax_command_insert.md) — Creates a Drupal Ajax 'insert' command using the method in #ajax['method'].
- [ajax_command_replace()](ajax_command_replace.md) — Creates a Drupal Ajax 'insert/replaceWith' command.
- [ajax_command_html()](ajax_command_html.md) — Creates a Drupal Ajax 'insert/html' command.
- [ajax_command_prepend()](ajax_command_prepend.md) — Creates a Drupal Ajax 'insert/prepend' command.
- [ajax_command_append()](ajax_command_append.md) — Creates a Drupal Ajax 'insert/append' command.
- [ajax_command_after()](ajax_command_after.md) — Creates a Drupal Ajax 'insert/after' command.
- [ajax_command_before()](ajax_command_before.md) — Creates a Drupal Ajax 'insert/before' command.
- [ajax_command_remove()](ajax_command_remove.md) — Creates a Drupal Ajax 'remove' command.
- [ajax_command_changed()](ajax_command_changed.md) — Creates a Drupal Ajax 'changed' command.
- [ajax_command_css()](ajax_command_css.md) — Creates a Drupal Ajax 'css' command.
- [ajax_command_settings()](ajax_command_settings.md) — Creates a Drupal Ajax 'settings' command.
- [ajax_command_data()](ajax_command_data.md) — Creates a Drupal Ajax 'data' command.
- [ajax_command_invoke()](ajax_command_invoke.md) — Creates a Drupal Ajax 'invoke' command.
- [ajax_command_restripe()](ajax_command_restripe.md) — Creates a Drupal Ajax 'restripe' command.
- [ajax_command_update_build_id()](ajax_command_update_build_id.md) — Creates a Drupal Ajax 'update_build_id' command.
- [ajax_command_add_css()](ajax_command_add_css.md) — Creates a Drupal Ajax 'add_css' command.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
