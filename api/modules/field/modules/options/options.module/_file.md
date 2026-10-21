# modules/field/modules/options/options.module

- **Source:** [local](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · 426 lines
- **Module/theme:** options

## File documentation

```text
@file
Defines selection, check box and radio button widgets for text and numeric fields.
```

## Functions (derived index)

- [options_help()](options_help.md) — Implements hook_help().
- [options_theme()](options_theme.md) — Implements hook_theme().
- [options_field_widget_info()](options_field_widget_info.md) — Implements hook_field_widget_info().
- [options_field_widget_form()](options_field_widget_form.md) — Implements hook_field_widget_form().
- [options_field_widget_settings_form()](options_field_widget_settings_form.md) — Implements hook_field_widget_settings_form().
- [options_field_widget_validate()](options_field_widget_validate.md) — Form element validation handler for options element.
- [_options_properties()](_options_properties.md) — Describes the preparation steps required by each widget.
- [_options_get_options()](_options_get_options.md) — Collects the options for a field.
- [_options_prepare_options()](_options_prepare_options.md) — Sanitizes the options.
- [_options_storage_to_form()](_options_storage_to_form.md) — Transforms stored field values into the format the widgets need.
- [_options_form_to_storage()](_options_form_to_storage.md) — Transforms submitted form values into field storage format.
- [options_array_transpose()](options_array_transpose.md) — Manipulates a 2D array to reverse rows and columns.
- [options_array_flatten()](options_array_flatten.md) — Flattens an array of allowed values.
- [options_field_widget_error()](options_field_widget_error.md) — Implements hook_field_widget_error().
- [theme_options_none()](theme_options_none.md) — Returns HTML for the label for the empty value for options that are not required.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
