# modules/file/file.field.inc

- **Source:** [local](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · 1029 lines
- **Module/theme:** file

## File documentation

```text
@file
Field module functionality for the File module.
```

## Functions (derived index)

- [file_field_info()](file_field_info.md) — Implements hook_field_info().
- [file_field_settings_form()](file_field_settings_form.md) — Implements hook_field_settings_form().
- [file_field_instance_settings_form()](file_field_instance_settings_form.md) — Implements hook_field_instance_settings_form().
- [_file_generic_settings_max_filesize()](_file_generic_settings_max_filesize.md) — Element validate callback for the maximum upload size field.
- [_file_generic_settings_extensions()](_file_generic_settings_extensions.md) — Element validate callback for the allowed file extensions field.
- [_file_generic_settings_file_directory_validate()](_file_generic_settings_file_directory_validate.md) — Element validate callback for the file destination field.
- [file_field_load()](file_field_load.md) — Implements hook_field_load().
- [file_field_prepare_view()](file_field_prepare_view.md) — Implements hook_field_prepare_view().
- [file_field_presave()](file_field_presave.md) — Implements hook_field_presave().
- [file_field_insert()](file_field_insert.md) — Implements hook_field_insert().
- [file_field_update()](file_field_update.md) — Implements hook_field_update().
- [file_field_delete()](file_field_delete.md) — Implements hook_field_delete().
- [file_field_delete_revision()](file_field_delete_revision.md) — Implements hook_field_delete_revision().
- [file_field_delete_file()](file_field_delete_file.md) — Decrements the usage count for a file and attempts to delete it.
- [file_field_is_empty()](file_field_is_empty.md) — Implements hook_field_is_empty().
- [file_field_displayed()](file_field_displayed.md) — Determines whether a file should be displayed when outputting field content.
- [file_field_formatter_info()](file_field_formatter_info.md) — Implements hook_field_formatter_info().
- [file_field_widget_info()](file_field_widget_info.md) — Implements hook_field_widget_info().
- [file_field_widget_settings_form()](file_field_widget_settings_form.md) — Implements hook_field_widget_settings_form().
- [file_field_widget_form()](file_field_widget_form.md) — Implements hook_field_widget_form().
- [file_field_widget_upload_validators()](file_field_widget_upload_validators.md) — Retrieves the upload validators for a file field.
- [file_field_widget_uri()](file_field_widget_uri.md) — Determines the URI for a file field instance.
- [file_field_widget_value()](file_field_widget_value.md) — The #value_callback for the file_generic field element.
- [file_field_widget_process()](file_field_widget_process.md) — An element #process callback for the file_generic field type.
- [file_field_widget_process_multiple()](file_field_widget_process_multiple.md) — An element #process callback for a group of file_generic fields.
- [_file_field_get_description_from_element()](_file_field_get_description_from_element.md) — Retrieves the file description from a field field element.
- [file_field_widget_submit()](file_field_widget_submit.md) — Form submission handler for upload/remove button of file_field_widget_form().
- [theme_file_widget()](theme_file_widget.md) — Returns HTML for an individual file upload widget.
- [theme_file_widget_multiple()](theme_file_widget_multiple.md) — Returns HTML for a group of file upload widgets.
- [theme_file_upload_help()](theme_file_upload_help.md) — Returns HTML for help text based on file upload validators.
- [file_field_formatter_view()](file_field_formatter_view.md) — Implements hook_field_formatter_view().
- [theme_file_formatter_table()](theme_file_formatter_table.md) — Returns HTML for a file attachments table.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
