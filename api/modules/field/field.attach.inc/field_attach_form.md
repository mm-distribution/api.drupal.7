# field_attach_form()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 564–588 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L564-L588)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_form($entity_type, $entity, &$form, &$form_state, $langcode = NULL, $options = array())
```

## Documentation

```text
Add form elements for all fields for an entity to a form structure.

The form elements for the entity's fields are added by reference as direct
children in the $form parameter. This parameter can be a full form structure
(most common case for entity edit forms), or a sub-element of a larger form.

By default, submitted field values appear at the top-level of
$form_state['values']. A different location within $form_state['values'] can
be specified by setting the '#parents' property on the incoming $form
parameter. Because of name clashes, two instances of the same field cannot
appear within the same $form element, or within the same '#parents' space.

For each call to field_attach_form(), field values are processed by calling
field_attach_form_validate() and field_attach_submit() on the same $form
element.

Sample resulting structure in $form:
@code
  '#parents' => The location of field values in $form_state['values'],
  '#entity_type' => The name of the entity type,
  '#bundle' => The name of the bundle,
  // One sub-array per field appearing in the entity, keyed by field name.
  // The structure of the array differs slightly depending on whether the
  // widget is 'single-value' (provides the input for one field value,
  // most common case), and will therefore be repeated as many times as
  // needed, or 'multiple-values' (one single widget allows the input of
  // several values, e.g checkboxes, select box...).
  // The sub-array is nested into a $langcode key where $langcode has the
  // same value of the $langcode parameter above.
  // The '#language' key holds the same value of $langcode and it is used
  // to access the field sub-array when $langcode is unknown.
  'field_foo' => array(
    '#tree' => TRUE,
    '#field_name' => The name of the field,
    '#language' => $langcode,
    $langcode => array(
      '#field_name' => The name of the field,
      '#language' => $langcode,
      '#field_parents' => The 'parents' space for the field in the form,
         equal to the #parents property of the $form parameter received by
         field_attach_form(),
      '#required' => Whether or not the field is required,
      '#title' => The label of the field instance,
      '#description' => The description text for the field instance,

      // Only for 'single' widgets:
      '#theme' => 'field_multiple_value_form',
      '#cardinality' => The field cardinality,
      // One sub-array per copy of the widget, keyed by delta.
      0 => array(
        '#entity_type' => The name of the entity type,
        '#bundle' => The name of the bundle,
        '#field_name' => The name of the field,
        '#field_parents' => The 'parents' space for the field in the form,
           equal to the #parents property of the $form parameter received by
           field_attach_form(),
        '#title' => The title to be displayed by the widget,
        '#default_value' => The field value for delta 0,
        '#required' => Whether the widget should be marked required,
        '#delta' => 0,
        '#columns' => The array of field columns,
        // The remaining elements in the sub-array depend on the widget.
        '#type' => The type of the widget,
        ...
      ),
      1 => array(
        ...
      ),

      // Only for multiple widgets:
      '#entity_type' => The name of the entity type,
      '#bundle' => $instance['bundle'],
      '#columns'  => array_keys($field['columns']),
      // The remaining elements in the sub-array depend on the widget.
      '#type' => The type of the widget,
      ...
    ),
    ...
  ),
)
@endcode

Additionally, some processing data is placed in $form_state, and can be
accessed by field_form_get_state() and field_form_set_state().

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity for which to load form elements, used to initialize
  default form values.
@param $form
  The form structure to fill in. This can be a full form structure, or a
  sub-element of a larger form. The #parents property can be set to control
  the location of submitted field values within $form_state['values']. If
  not specified, $form['#parents'] is set to an empty array, placing field
  values at the top-level of $form_state['values'].
@param $form_state
  An associative array containing the current state of the form.
@param $langcode
  The language the field values are going to be entered, if no language
  is provided the default site language will be used.
@param array $options
  An associative array of additional options. See _field_invoke() for
  details.

@see field_form_get_state()
@see field_form_set_state()
```

## Code

```php
function field_attach_form($entity_type, $entity, &$form, &$form_state, $langcode = NULL, $options = array()) {
  // Validate $options since this is a new parameter added after Drupal 7 was
  // released.
  $options = is_array($options) ? $options : array();

  // Set #parents to 'top-level' by default.
  $form += array('#parents' => array());

  // If no language is provided use the default site language.
  $options['language'] = field_valid_language($langcode);
  $form += (array) _field_invoke_default('form', $entity_type, $entity, $form, $form_state, $options);

  // Add custom weight handling.
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
  $form['#pre_render'][] = '_field_extra_fields_pre_render';
  $form['#entity_type'] = $entity_type;
  $form['#bundle'] = $bundle;

  // Let other modules make changes to the form.
  // Avoid module_invoke_all() to let parameters be taken by reference.
  foreach (module_implements('field_attach_form') as $module) {
    $function = $module . '_field_attach_form';
    $function($entity_type, $entity, $form, $form_state, $langcode);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
