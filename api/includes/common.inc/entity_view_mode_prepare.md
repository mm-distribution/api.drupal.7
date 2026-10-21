# entity_view_mode_prepare()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8332–8357 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8332-L8357)

## Signature

```php
function entity_view_mode_prepare($entity_type, $entities, $view_mode, $langcode = NULL)
```

## Documentation

```text
Invoke hook_entity_view_mode_alter().

If adding a new entity similar to nodes, comments or users, you should invoke
this function during the ENTITY_build_content() or ENTITY_view_multiple()
phases of rendering to allow other modules to alter the view mode during this
phase. This function needs to be called before field_attach_prepare_view() to
ensure that the correct content is loaded by field API.

@param $entity_type
  The type of entity, i.e. 'node', 'user'.
@param $entities
  The entity objects which are being prepared for view, keyed by object ID.
@param $view_mode
  The original view mode e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to be used for rendering. Defaults to the global
  content language of the current request.
@return
  An associative array with arrays of entities keyed by view mode.

@see hook_entity_view_mode_alter()
```

## Code

```php
function entity_view_mode_prepare($entity_type, $entities, $view_mode, $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // To ensure hooks are never run after field_attach_prepare_view() only
  // process items without the entity_view_prepared flag.
  $entities_by_view_mode = array();
  foreach ($entities as $id => $entity) {
    $entity_view_mode = $view_mode;
    if (empty($entity->entity_view_prepared)) {

      // Allow modules to change the view mode.
      $context = array(
        'entity_type' => $entity_type,
        'entity' => $entity,
        'langcode' => $langcode,
      );
      drupal_alter('entity_view_mode', $entity_view_mode, $context);
    }

    $entities_by_view_mode[$entity_view_mode][$id] = $entity;
  }

  return $entities_by_view_mode;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
