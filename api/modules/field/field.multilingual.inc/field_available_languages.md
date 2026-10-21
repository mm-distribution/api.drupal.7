# field_available_languages()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 89–113 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L89-L113)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_available_languages($entity_type, $field)
```

## Documentation

```text
Collects the available languages for the given entity type and field.

If the given field has language support enabled, an array of available
languages will be returned, otherwise only LANGUAGE_NONE will be returned.
Since the default value for a 'translatable' entity property is FALSE, we
ensure that only entities that are able to handle translations actually get
translatable fields.

@param $entity_type
  The type of the entity the field is attached to, e.g. 'node' or 'user'.
@param $field
  A field structure.

@return
  An array of valid language codes.
```

## Code

```php
function field_available_languages($entity_type, $field) {
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['field_languages'] = &drupal_static(__FUNCTION__);
  }
  $field_languages = &$drupal_static_fast['field_languages'];
  $field_name = $field['field_name'];

  if (!isset($field_languages[$entity_type][$field_name])) {
    // If the field has language support enabled we retrieve an (alterable) list
    // of enabled languages, otherwise we return just LANGUAGE_NONE.
    if (field_is_translatable($entity_type, $field)) {
      $languages = field_content_languages();
      // Let other modules alter the available languages.
      $context = array('entity_type' => $entity_type, 'field' => $field);
      drupal_alter('field_available_languages', $languages, $context);
      $field_languages[$entity_type][$field_name] = $languages;
    }
    else {
      $field_languages[$entity_type][$field_name] = array(LANGUAGE_NONE);
    }
  }

  return $field_languages[$entity_type][$field_name];
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
