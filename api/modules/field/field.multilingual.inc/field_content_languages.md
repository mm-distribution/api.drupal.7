# field_content_languages()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 157–159 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L157-L159)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_content_languages()
```

## Documentation

```text
Returns available content languages.

The languages that may be associated to fields include LANGUAGE_NONE.

@return
  An array of language codes.
```

## Code

```php
function field_content_languages() {
  return array_keys(language_list() + array(LANGUAGE_NONE => NULL));
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
