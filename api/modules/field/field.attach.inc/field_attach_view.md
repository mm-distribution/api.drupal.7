# field_attach_view()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1216–1252 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1216-L1252)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_view($entity_type, $entity, $view_mode, $langcode = NULL, $options = array())
```

## Documentation

```text
Returns a renderable array for the fields on an entity.

Each field is displayed according to the display options specified in the
$instance definition for the given $view_mode.

field_attach_prepare_view() and field_attach_view() are two halves
of the same operation. It is safe to call
field_attach_prepare_view() multiple times on the same entity
before calling field_attach_view() on it, but calling any Field
API operation on an entity between passing that entity to these two
functions may yield incorrect results.

Sample structure:
@code
array(
  'field_foo' => array(
    '#theme' => 'field',
    '#title' => the label of the field instance,
    '#label_display' => the label display mode,
    '#object' => the fieldable entity being displayed,
    '#entity_type' => the type of the entity being displayed,
    '#language' => the language of the field values being displayed,
    '#view_mode' => the view mode,
    '#field_name' => the name of the field,
    '#field_type' => the type of the field,
    '#formatter' => the name of the formatter,
    '#items' => the field values being displayed,
    // The element's children are the formatted values returned by
    // hook_field_formatter_view().
  ),
);
@endcode

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to render.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  The language the field values are to be shown in. If no language is
  provided the current language is used.
@param array $options
  An associative array of additional options. See _field_invoke() for
  details.
@return
  A renderable array for the field values.
```

## Code

```php
function field_attach_view($entity_type, $entity, $view_mode, $langcode = NULL, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  // Determine the actual language to display for each field, given the
  // languages available in the field data.
  $display_language = field_language($entity_type, $entity, NULL, $langcode);
  $options['language'] = $display_language;

  // Invoke field_default_view().
  $null = NULL;
  $output = _field_invoke_default('view', $entity_type, $entity, $view_mode, $null, $options);

  // Add custom weight handling.
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  $output['#pre_render'][] = '_field_extra_fields_pre_render';
  $output['#entity_type'] = $entity_type;
  $output['#bundle'] = $bundle;

  // Let other modules alter the renderable array.
  $context = array(
    'entity_type' => $entity_type,
    'entity' => $entity,
    'view_mode' => $view_mode,
    'display' => $view_mode,
    'language' => $langcode,
  );
  drupal_alter('field_attach_view', $output, $context);

  // Reset the _field_view_prepared flag set in field_attach_prepare_view(),
  // in case the same entity is displayed with different settings later in
  // the request.
  unset($entity->_field_view_prepared);

  return $output;
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
