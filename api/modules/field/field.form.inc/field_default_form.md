# field_default_form()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 42–170 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L42-L170)
- **Module/theme:** field

## Signature

```php
function field_default_form($entity_type, $entity, $field, $instance, $langcode, $items, &$form, &$form_state, $get_delta = NULL)
```

## Documentation

```text
Creates a form element for a field and can populate it with a default value.

If the form element is not associated with an entity (i.e., $entity is NULL)
field_get_default_value will be called to supply the default value for the
field. Also allows other modules to alter the form element by implementing
their own hooks.

@param $entity_type
  The type of entity (for example 'node' or 'user') that the field belongs
  to.
@param $entity
  The entity object that the field belongs to. This may be NULL if creating a
  form element with a default value.
@param $field
  An array representing the field whose editing element is being created.
@param $instance
  An array representing the structure for $field in its current context.
@param $langcode
  The language associated with the field.
@param $items
  An array of the field values. When creating a new entity this may be NULL
  or an empty array to use default values.
@param $form
  An array representing the form that the editing element will be attached
  to.
@param $form_state
  An array containing the current state of the form.
@param $get_delta
  Used to get only a specific delta value of a multiple value field.

@return
 The form element array created for this field.
```

## Code

```php
function field_default_form($entity_type, $entity, $field, $instance, $langcode, $items, &$form, &$form_state, $get_delta = NULL) {
  // This could be called with no entity, as when a UI module creates a
  // dummy form to set default values.
  if ($entity) {
    list($id, , ) = entity_extract_ids($entity_type, $entity);
  }

  $parents = $form['#parents'];

  $addition = array();
  $field_name = $field['field_name'];
  $addition[$field_name] = array();

  // Populate widgets with default values when creating a new entity.
  if (empty($items) && empty($id)) {
    $items = field_get_default_value($entity_type, $entity, $field, $instance, $langcode);
  }

  // Let modules alter the widget properties.
  $context = array(
    'entity_type' => $entity_type,
    'entity' => $entity,
    'field' => $field,
    'instance' => $instance,
  );
  drupal_alter(array('field_widget_properties', 'field_widget_properties_' . $entity_type), $instance['widget'], $context);

  // Collect widget elements.
  $elements = array();

  // Store field information in $form_state.
  if (!field_form_get_state($parents, $field_name, $langcode, $form_state)) {
    $field_state = array(
      'field' => $field,
      'instance' => $instance,
      'items_count' => count($items),
      'array_parents' => array(),
      'errors' => array(),
    );
    field_form_set_state($parents, $field_name, $langcode, $form_state, $field_state);
  }

  // If field module handles multiple values for this form element, and we are
  // not displaying an individual element, process the multiple value form.
  if (!isset($get_delta) && field_behaviors_widget('multiple values', $instance) == FIELD_BEHAVIOR_DEFAULT) {
    // Store the entity in the form.
    $form['#entity'] = $entity;
    $elements = field_multiple_value_form($field, $instance, $langcode, $items, $form, $form_state);
  }
  // If the widget is handling multiple values (e.g Options), or if we are
  // displaying an individual element, just get a single form element and make
  // it the $delta value.
  else {
    $delta = isset($get_delta) ? $get_delta : 0;
    $function = $instance['widget']['module'] . '_field_widget_form';
    if (function_exists($function)) {
      $element = array(
        '#entity' => $entity,
        '#entity_type' => $instance['entity_type'],
        '#bundle' => $instance['bundle'],
        '#field_name' => $field_name,
        '#language' => $langcode,
        '#field_parents' => $parents,
        '#columns' => array_keys($field['columns']),
        '#title' => check_plain($instance['label']),
        '#description' => field_filter_xss($instance['description']),
        // Only the first widget should be required.
        '#required' => $delta == 0 && $instance['required'],
        '#delta' => $delta,
      );
      if ($element = $function($form, $form_state, $field, $instance, $langcode, $items, $delta, $element)) {
        // Allow modules to alter the field widget form element.
        $context = array(
          'form' => $form,
          'field' => $field,
          'instance' => $instance,
          'langcode' => $langcode,
          'items' => $items,
          'delta' => $delta,
        );
        drupal_alter(array('field_widget_form', 'field_widget_' . $instance['widget']['type'] . '_form'), $element, $form_state, $context);

        // If we're processing a specific delta value for a field where the
        // field module handles multiples, set the delta in the result.
        // For fields that handle their own processing, we can't make
        // assumptions about how the field is structured, just merge in the
        // returned element.
        if (field_behaviors_widget('multiple values', $instance) == FIELD_BEHAVIOR_DEFAULT) {
          $elements[$delta] = $element;
        }
        else {
          $elements = $element;
        }
      }
    }
  }

  // Also aid in theming of field widgets by rendering a classified container.
  $addition[$field_name] = array(
    '#type' => 'container',
    '#attributes' => array(
      'class' => array(
        'field-type-' . drupal_html_class($field['type']),
        'field-name-' . drupal_html_class($field_name),
        'field-widget-' . drupal_html_class($instance['widget']['type']),
      ),
    ),
    '#weight' => $instance['widget']['weight'],
  );

  // Populate the 'array_parents' information in $form_state['field'] after
  // the form is built, so that we catch changes in the form structure performed
  // in alter() hooks.
  $elements['#after_build'][] = 'field_form_element_after_build';
  $elements['#field_name'] = $field_name;
  $elements['#language'] = $langcode;
  $elements['#field_parents'] = $parents;

  $addition[$field_name] += array(
    '#tree' => TRUE,
    // The '#language' key can be used to access the field's form element
    // when $langcode is unknown.
    '#language' => $langcode,
    $langcode => $elements,
    '#access' => field_access('edit', $field, $entity_type, $entity),
  );

  return $addition;
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
