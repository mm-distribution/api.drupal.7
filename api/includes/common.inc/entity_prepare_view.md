# entity_prepare_view()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8285–8307 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8285-L8307)

## Signature

```php
function entity_prepare_view($entity_type, $entities, $langcode = NULL)
```

## Documentation

```text
Invoke hook_entity_prepare_view().

If adding a new entity similar to nodes, comments or users, you should
invoke this function during the ENTITY_build_content() or
ENTITY_view_multiple() phases of rendering to allow other modules to alter
the objects during this phase. This is needed for situations where
information needs to be loaded outside of ENTITY_load() - particularly
when loading entities into one another - i.e. a user object into a node, due
to the potential for unwanted side-effects such as caching and infinite
recursion. By convention, entity_prepare_view() is called after
field_attach_prepare_view() to allow entity level hooks to act on content
loaded by field API.

@param $entity_type
  The type of entity, i.e. 'node', 'user'.
@param $entities
  The entity objects which are being prepared for view, keyed by object ID.
@param $langcode
  (optional) A language code to be used for rendering. Defaults to the global
  content language of the current request.

@see hook_entity_prepare_view()
```

## Code

```php
function entity_prepare_view($entity_type, $entities, $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // To ensure hooks are only run once per entity, check for an
  // entity_view_prepared flag and only process items without it.
  // @todo: resolve this more generally for both entity and field level hooks.
  $prepare = array();
  foreach ($entities as $id => $entity) {
    if (empty($entity->entity_view_prepared)) {
      // Add this entity to the items to be prepared.
      $prepare[$id] = $entity;

      // Mark this item as prepared.
      $entity->entity_view_prepared = TRUE;
    }
  }

  if (!empty($prepare)) {
    module_invoke_all('entity_prepare_view', $prepare, $entity_type, $langcode);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
