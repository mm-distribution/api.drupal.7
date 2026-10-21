# field_attach_prepare_view()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1133–1165 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1133-L1165)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_prepare_view($entity_type, $entities, $view_mode, $langcode = NULL, $options = array())
```

## Documentation

```text
Prepare field data prior to display.

This function lets field types and formatters load additional data
needed for display that is not automatically loaded during
field_attach_load(). It accepts an array of entities to allow query
optimisation when displaying lists of entities.

field_attach_prepare_view() and field_attach_view() are two halves
of the same operation. It is safe to call
field_attach_prepare_view() multiple times on the same entity
before calling field_attach_view() on it, but calling any Field
API operation on an entity between passing that entity to these two
functions may yield incorrect results.

@param $entity_type
  The type of $entities; e.g. 'node' or 'user'.
@param $entities
  An array of entities, keyed by entity id.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (Optional) The language the field values are to be shown in. If no language
  is provided the current language is used.
@param array $options
  An associative array of additional options. See _field_invoke() for
  details.
```

## Code

```php
function field_attach_prepare_view($entity_type, $entities, $view_mode, $langcode = NULL, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  $options['language'] = array();

  // To ensure hooks are only run once per entity, only process items without
  // the _field_view_prepared flag.
  // @todo: resolve this more generally for both entity and field level hooks.
  $prepare = array();
  foreach ($entities as $id => $entity) {
    if (empty($entity->_field_view_prepared)) {
      // Add this entity to the items to be prepared.
      $prepare[$id] = $entity;

      // Determine the actual language to display for each field, given the
      // languages available in the field data.
      $options['language'][$id] = field_language($entity_type, $entity, NULL, $langcode);

      // Mark this item as prepared.
      $entity->_field_view_prepared = TRUE;
    }
  }

  $null = NULL;
  // First let the field types do their preparation.
  _field_invoke_multiple('prepare_view', $entity_type, $prepare, $null, $null, $options);
  // Then let the formatters do their own specific massaging.
  // field_default_prepare_view() takes care of dispatching to the correct
  // formatters according to the display settings for the view mode.
  _field_invoke_multiple_default('prepare_view', $entity_type, $prepare, $view_mode, $null, $options);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
