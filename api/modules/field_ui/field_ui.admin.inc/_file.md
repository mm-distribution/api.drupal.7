# modules/field_ui/field_ui.admin.inc

- **Source:** [local](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · 2130 lines
- **Module/theme:** field_ui

## File documentation

```text
@file
Administrative interface for custom field type creation.
```

## Functions (derived index)

- [field_ui_fields_list()](field_ui_fields_list.md) — Menu callback; lists all defined fields for quick reference.
- [field_ui_inactive_message()](field_ui_inactive_message.md) — Displays a message listing the inactive fields of a given bundle.
- [_field_ui_reduce_order()](_field_ui_reduce_order.md) — Determines the rendering order of an array representing a tree.
- [field_ui_field_overview_row_region()](field_ui_field_overview_row_region.md) — Returns the region to which a row in the 'Manage fields' screen belongs.
- [field_ui_display_overview_row_region()](field_ui_display_overview_row_region.md) — Returns the region to which a row in the 'Manage display' screen belongs.
- [field_ui_table_pre_render()](field_ui_table_pre_render.md) — Pre-render callback for field_ui_table elements.
- [theme_field_ui_table()](theme_field_ui_table.md) — Returns HTML for Field UI overview tables.
- [field_ui_field_overview_form()](field_ui_field_overview_form.md) — Form constructor for the 'Manage fields' form of a bundle.
- [field_ui_field_overview_form_validate()](field_ui_field_overview_form_validate.md) — Form validation handler for field_ui_field_overview_form().
- [_field_ui_field_overview_form_validate_add_new()](_field_ui_field_overview_form_validate_add_new.md) — Validates the 'add new field' row of field_ui_field_overview_form().
- [_field_ui_field_name_exists()](_field_ui_field_name_exists.md) — Render API callback: Checks if a field machine name is taken.
- [_field_ui_field_overview_form_validate_add_existing()](_field_ui_field_overview_form_validate_add_existing.md) — Validates the 'add existing field' row of field_ui_field_overview_form().
- [field_ui_field_overview_form_submit()](field_ui_field_overview_form_submit.md) — Form submission handler for field_ui_field_overview_form().
- [field_ui_display_overview_form()](field_ui_display_overview_form.md) — Form constructor for the field display settings for a given view mode.
- [field_ui_display_overview_multistep_submit()](field_ui_display_overview_multistep_submit.md) — Form submission handler for buttons in field_ui_display_overview_form().
- [field_ui_display_overview_multistep_js()](field_ui_display_overview_multistep_js.md) — Ajax handler for multistep buttons on the 'Manage display' screen.
- [field_ui_display_overview_form_submit()](field_ui_display_overview_form_submit.md) — Form submission handler for field_ui_display_overview_form().
- [_field_ui_add_default_view_mode_settings()](_field_ui_add_default_view_mode_settings.md) — Populates display settings for a new view mode from the default view mode.
- [field_ui_field_type_options()](field_ui_field_type_options.md) — Returns an array of field_type options.
- [field_ui_widget_type_options()](field_ui_widget_type_options.md) — Returns an array of widget type options for a field type.
- [field_ui_formatter_options()](field_ui_formatter_options.md) — Returns an array of formatter options for a field type.
- [field_ui_existing_field_options()](field_ui_existing_field_options.md) — Returns an array of existing fields to be added to a bundle.
- [field_ui_field_settings_form()](field_ui_field_settings_form.md) — Form constructor for the field settings edit page.
- [field_ui_field_settings_form_submit()](field_ui_field_settings_form_submit.md) — Form submission handler for field_ui_field_settings_form().
- [field_ui_widget_type_form()](field_ui_widget_type_form.md) — Form constructor for the widget selection form.
- [field_ui_widget_type_form_submit()](field_ui_widget_type_form_submit.md) — Form submission handler for field_ui_widget_type_form().
- [field_ui_field_delete_form()](field_ui_field_delete_form.md) — Form constructor for removing a field instance from a bundle.
- [field_ui_field_delete_form_submit()](field_ui_field_delete_form_submit.md) — Form submission handler for field_ui_field_delete_form().
- [field_ui_field_edit_form()](field_ui_field_edit_form.md) — Form constructor for the field instance settings form.
- [field_ui_field_edit_instance_pre_render()](field_ui_field_edit_instance_pre_render.md) — Pre-render function for field instance settings.
- [field_ui_default_value_widget()](field_ui_default_value_widget.md) — Builds the default value fieldset for a given field instance.
- [field_ui_field_edit_form_validate()](field_ui_field_edit_form_validate.md) — Form validation handler for field_ui_field_edit_form().
- [field_ui_field_edit_form_submit()](field_ui_field_edit_form_submit.md) — Form submission handler for field_ui_field_edit_form().
- [field_ui_get_destinations()](field_ui_get_destinations.md) — Extracts next redirect path from an array of multiple destinations.
- [field_ui_next_destination()](field_ui_next_destination.md) — Returns the next redirect path in a multipage sequence.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
