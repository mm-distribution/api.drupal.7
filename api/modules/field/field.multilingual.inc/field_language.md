# field_language()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 266–301 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L266-L301)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_language($entity_type, $entity, $field_name = NULL, $langcode = NULL)
```

## Documentation

```text
Returns the display language for the fields attached to the given entity.

The actual language for each given field is determined based on the requested
language and the actual data available in the fields themselves.
If there is no registered translation handler for the given entity type, the
display language to be used is just LANGUAGE_NONE, as no other language code
is allowed by field_available_languages().
If translation handlers are found, we let modules provide alternative display
languages for fields not having the requested language available.
Core language fallback rules are provided by locale_field_language_fallback()
which is called by locale_field_language_alter().

@param $entity_type
  The type of $entity.
@param $entity
  The entity to be displayed.
@param $field_name
  (optional) The name of the field to be displayed. Defaults to NULL. If
  no value is specified, the display languages for every field attached to
  the given entity will be returned.
@param $langcode
  (optional) The language code $entity has to be displayed in. Defaults to
  NULL. If no value is given the current language will be used.

@return
  A language code if a field name is specified, an array of language codes
  keyed by field name otherwise.
```

## Code

```php
function field_language($entity_type, $entity, $field_name = NULL, $langcode = NULL) {
  $display_languages = &drupal_static(__FUNCTION__, array());
  list($id, , $bundle) = entity_extract_ids($entity_type, $entity);
  $langcode = field_valid_language($langcode, FALSE);

  if (!isset($display_languages[$entity_type][$id][$langcode])) {
    $display_language = array();

    // By default display language is set to LANGUAGE_NONE if the field
    // translation is not available. It is up to translation handlers to
    // implement language fallback rules.
    foreach (field_info_instances($entity_type, $bundle) as $instance) {
      $display_language[$instance['field_name']] = isset($entity->{$instance['field_name']}[$langcode]) ? $langcode : LANGUAGE_NONE;
    }

    if (field_has_translation_handler($entity_type)) {
      $context = array(
        'entity_type' => $entity_type,
        'entity' => $entity,
        'language' => $langcode,
      );
      drupal_alter('field_language', $display_language, $context);
    }

    $display_languages[$entity_type][$id][$langcode] = $display_language;
  }

  $display_language = $display_languages[$entity_type][$id][$langcode];

  // Single-field mode.
  if (isset($field_name)) {
    return isset($display_language[$field_name]) ? $display_language[$field_name] : FALSE;
  }

  return $display_language;
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
