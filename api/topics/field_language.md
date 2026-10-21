# Field Language API

- **Topic id:** `field_language`
- **Defined in:** [`modules/field/field.multilingual.inc`](../modules/field/field.multilingual.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L8)

## Documentation

```text
@defgroup field_language Field Language API
@{
Handling of multilingual fields.

Fields natively implement multilingual support, and all fields use the
following structure:
@code
$entity->{$field_name}[$langcode][$delta][$column_name]
@endcode
Every field can hold a single or multiple value for each language belonging
to the available languages set:
- For untranslatable fields this set only contains LANGUAGE_NONE.
- For translatable fields this set can contain any language code. By default
  it is the list returned by field_content_languages(), which contains all
  installed languages with the addition of LANGUAGE_NONE. This default can be
  altered by modules implementing hook_field_available_languages_alter().

The available languages for a particular field are returned by
field_available_languages(). Whether a field is translatable is determined by
calling field_is_translatable(), which checks the $field['translatable']
property returned by field_info_field(), and whether there is at least one
translation handler available for the field. A translation handler is a
module registering itself via hook_entity_info() to handle field
translations.

By default, _field_invoke() and _field_invoke_multiple() are processing a
field in all available languages, unless they are given a language
suggestion. Based on that suggestion, _field_language_suggestion() determines
the languages to act on.

Most field_attach_*() functions act on all available languages, except for
the following:
- field_attach_form() only takes a single language code, specifying which
  language the field values will be submitted in.
- field_attach_view() requires the language the entity will be displayed in.
  Since it is unknown whether a field translation exists for the requested
  language, the translation handler is responsible for performing one of the
  following actions:
  - Ignore missing translations, i.e. do not show any field values for the
    requested language. For example, see locale_field_language_alter().
  - Provide a value in a different language as fallback. By default, the
    fallback logic is applied separately to each field to ensure that there
    is a value for each field to display.
  The field language fallback logic relies on the global language fallback
  configuration. Therefore, the displayed field values can be in the
  requested language, but may be different if no values for the requested
  language are available. The default language fallback rules inspect all the
  enabled languages ordered by their weight. This behavior can be altered or
  even disabled by modules implementing hook_field_language_alter(), making
  it possible to choose the first approach. The display language for each
  field is returned by field_language().

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 11)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_field_language_suggestion()](../modules/field/field.multilingual.inc/_field_language_suggestion.md) (function) — Process the given language suggestion based on the available languages.
- [field_available_languages()](../modules/field/field.multilingual.inc/field_available_languages.md) (function) — Collects the available languages for the given entity type and field.
- [field_content_languages()](../modules/field/field.multilingual.inc/field_content_languages.md) (function) — Returns available content languages.
- [field_has_translation_handler()](../modules/field/field.multilingual.inc/field_has_translation_handler.md) (function) — Checks if a module is registered as a translation handler for a given entity.
- [field_is_translatable()](../modules/field/field.multilingual.inc/field_is_translatable.md) (function) — Checks whether a field has language support.
- [field_language()](../modules/field/field.multilingual.inc/field_language.md) (function) — Returns the display language for the fields attached to the given entity.
- [field_multilingual_settings_changed()](../modules/field/field.multilingual.inc/field_multilingual_settings_changed.md) (function) — Implements hook_multilingual_settings_changed().
- [field_valid_language()](../modules/field/field.multilingual.inc/field_valid_language.md) (function) — Ensures that a given language code is valid.
- [hook_field_available_languages_alter()](../modules/field/field.api.php/hook_field_available_languages_alter.md) (function) — Alter field_available_languages() values.
- [hook_field_language_alter()](../modules/field/field.api.php/hook_field_language_alter.md) (function) — Perform alterations on field_language() values.
- [hook_field_prepare_translation()](../modules/field/field.api.php/hook_field_prepare_translation.md) (function) — Define custom prepare_translation behavior for this module's field types.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
