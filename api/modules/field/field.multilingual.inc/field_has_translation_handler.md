# field_has_translation_handler()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 195–211 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L195-L211)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)

## Signature

```php
function field_has_translation_handler($entity_type, $handler = NULL)
```

## Documentation

```text
Checks if a module is registered as a translation handler for a given entity.

If no handler is passed, simply check if there is any translation handler
enabled for the given entity type.

@param $entity_type
  The type of the entity whose fields are to be translated.
@param $handler
  (optional) The name of the handler to be checked. Defaults to NULL.

@return
  TRUE, if the given handler is allowed to manage field translations. If no
  handler is passed, TRUE means there is at least one registered translation
  handler.
```

## Code

```php
function field_has_translation_handler($entity_type, $handler = NULL) {
  $entity_info = entity_get_info($entity_type);

  if (isset($handler)) {
    return !empty($entity_info['translation'][$handler]);
  }
  elseif (isset($entity_info['translation'])) {
    foreach ($entity_info['translation'] as $handler_info) {
      // The translation handler must use a non-empty data structure.
      if (!empty($handler_info)) {
        return TRUE;
      }
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
