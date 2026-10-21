# _field_language_suggestion()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 131–147 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L131-L147)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function _field_language_suggestion($available_languages, $language_suggestion, $field_name)
```

## Documentation

```text
Process the given language suggestion based on the available languages.

If a non-empty language suggestion is provided it must appear among the
available languages, otherwise it will be ignored.

@param $available_languages
  An array of valid language codes.
@param $language_suggestion
  A language code or an array of language codes keyed by field name.
@param $field_name
  The name of the field being processed.

@return
  An array of valid language codes.
```

## Code

```php
function _field_language_suggestion($available_languages, $language_suggestion, $field_name) {
  // Handle possible language suggestions.
  if (!empty($language_suggestion)) {
    // We might have an array of language suggestions keyed by field name.
    if (is_array($language_suggestion) && isset($language_suggestion[$field_name])) {
      $language_suggestion = $language_suggestion[$field_name];
    }

    // If we have a language suggestion and the suggested language is available,
    // we return only it.
    if (in_array($language_suggestion, $available_languages)) {
      $available_languages = array($language_suggestion);
    }
  }

  return $available_languages;
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
