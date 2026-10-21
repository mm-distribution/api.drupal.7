# field_valid_language()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 228–235 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L228-L235)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_valid_language($langcode, $default = TRUE)
```

## Documentation

```text
Ensures that a given language code is valid.

Checks whether the given language is one of the enabled languages. Otherwise,
it returns the current, global language; or the site's default language, if
the additional parameter $default is TRUE.

@param $langcode
  The language code to validate.
@param $default
  Whether to return the default language code or the current language code in
  case $langcode is invalid.
@return
  A valid language code.
```

## Code

```php
function field_valid_language($langcode, $default = TRUE) {
  $enabled_languages = field_content_languages();
  if (in_array($langcode, $enabled_languages)) {
    return $langcode;
  }
  global $language_content;
  return $default ? language_default('language') : $language_content->language;
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
