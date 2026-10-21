# entity_language()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8436–8461 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8436-L8461)

## Signature

```php
function entity_language($entity_type, $entity)
```

## Documentation

```text
Returns the language of an entity.

@param $entity_type
  The entity type; e.g., 'node' or 'user'.
@param $entity
  The entity for which to get the language.

@return
  A valid language code or NULL if the entity has no language support.
```

## Code

```php
function entity_language($entity_type, $entity) {
  $info = entity_get_info($entity_type);

  // Invoke the callback to get the language. If there is no callback, try to
  // get it from a property of the entity, otherwise NULL.
  if (isset($info['language callback']) && function_exists($info['language callback'])) {
    $langcode = $info['language callback']($entity_type, $entity);
  }
  elseif (!empty($info['entity keys']['language']) && isset($entity->{$info['entity keys']['language']})) {
    $langcode = $entity->{$info['entity keys']['language']};
  }
  else {
    // The value returned in D8 would be LANGUAGE_NONE, we cannot use it here to
    // preserve backward compatibility. In fact this function has been
    // introduced very late in the D7 life cycle, mainly as the proper default
    // for field_attach_form(). By returning LANGUAGE_NONE when no language
    // information is available, we would introduce a potentially BC-breaking
    // API change, since field_attach_form() defaults to the default language
    // instead of LANGUAGE_NONE. Moreover this allows us to distinguish between
    // entities that have no language specified from ones that do not have
    // language support at all.
    $langcode = NULL;
  }

  return $langcode;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
