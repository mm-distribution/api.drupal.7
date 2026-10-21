# Field Widget API

- **Topic id:** `field_widget`
- **Defined in:** [`modules/field/field.api.php`](../modules/field/field.api.php/_file.md), line 730 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L730)

## Documentation

```text
@defgroup field_widget Field Widget API
@{
Define Field API widget types.

Field API widgets specify how fields are displayed in edit forms. Fields of a
given @link field_types field type @endlink may be edited using more than one
widget. In this case, the Field UI module allows the site builder to choose
which widget to use. Widget types are defined by implementing
hook_field_widget_info().

Widgets are @link forms_api_reference.html Form API @endlink elements with
additional processing capabilities. Widget hooks are typically called by the
Field Attach API during the creation of the field form structure with
field_attach_form().

@see field
@see field_types
@see field_formatter
```

## Members (derived, 8)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_field_widget_WIDGET_TYPE_form_alter()](../modules/field/field.api.php/hook_field_widget_WIDGET_TYPE_form_alter.md) (function) — Alter widget forms for a specific widget provided by another module.
- [hook_field_widget_error()](../modules/field/field.api.php/hook_field_widget_error.md) (function) — Flag a field-level validation error.
- [hook_field_widget_form()](../modules/field/field.api.php/hook_field_widget_form.md) (function) — Return the form for a single field widget.
- [hook_field_widget_form_alter()](../modules/field/field.api.php/hook_field_widget_form_alter.md) (function) — Alter forms for field widgets provided by other modules.
- [hook_field_widget_info()](../modules/field/field.api.php/hook_field_widget_info.md) (function) — Expose Field API widget types.
- [hook_field_widget_info_alter()](../modules/field/field.api.php/hook_field_widget_info_alter.md) (function) — Perform alterations on Field API widget types.
- [hook_field_widget_properties_ENTITY_TYPE_alter()](../modules/field/field.api.php/hook_field_widget_properties_ENTITY_TYPE_alter.md) (function) — Alters the widget properties of a field instance on a given entity type before it gets displayed.
- [hook_field_widget_properties_alter()](../modules/field/field.api.php/hook_field_widget_properties_alter.md) (function) — Alters the widget properties of a field instance before it gets displayed.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
