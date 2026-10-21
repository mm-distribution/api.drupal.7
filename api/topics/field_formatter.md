# Field Formatter API

- **Topic id:** `field_formatter`
- **Defined in:** [`modules/field/field.api.php`](../modules/field/field.api.php/_file.md), line 1050 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1050)

## Documentation

```text
@defgroup field_formatter Field Formatter API
@{
Define Field API formatter types.

Field API formatters specify how fields are displayed when the entity to
which the field is attached is displayed. Fields of a given
@link field_types field type @endlink may be displayed using more than one
formatter. In this case, the Field UI module allows the site builder to
choose which formatter to use. Field formatters are defined by implementing
hook_field_formatter_info().

@see field
@see field_types
@see field_widget
```

## Members (derived, 4)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_field_formatter_info()](../modules/field/field.api.php/hook_field_formatter_info.md) (function) — Expose Field API formatter types.
- [hook_field_formatter_info_alter()](../modules/field/field.api.php/hook_field_formatter_info_alter.md) (function) — Perform alterations on Field API formatter types.
- [hook_field_formatter_prepare_view()](../modules/field/field.api.php/hook_field_formatter_prepare_view.md) (function) — Allow formatters to load information for field values being displayed.
- [hook_field_formatter_view()](../modules/field/field.api.php/hook_field_formatter_view.md) (function) — Build a renderable array for a field value.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
