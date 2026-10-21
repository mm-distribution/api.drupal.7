# field_multiple_value_form()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 180–298 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L180-L298)
- **Module/theme:** field

## Signature

```php
function field_multiple_value_form($field, $instance, $langcode, $items, &$form, &$form_state)
```

## Documentation

```text
Special handling to create form elements for multiple values.

Handles generic features for multiple fields:
- number of widgets
- AHAH-'add more' button
- drag-n-drop value reordering
```

## Code

```php
function field_multiple_value_form($field, $instance, $langcode, $items, &$form, &$form_state) {
  $field_name = $field['field_name'];
  $parents = $form['#parents'];

  // Determine the number of widgets to display.
  switch ($field['cardinality']) {
    case FIELD_CARDINALITY_UNLIMITED:
      $field_state = field_form_get_state($parents, $field_name, $langcode, $form_state);
      $max = $field_state['items_count'];
      break;

    default:
      $max = $field['cardinality'] - 1;
      break;
  }

  $title = check_plain($instance['label']);
  $description = field_filter_xss($instance['description']);

  $id_prefix = implode('-', array_merge($parents, array($field_name)));
  $wrapper_id = drupal_html_id($id_prefix . '-add-more-wrapper');

  $field_elements = array();

  $function = $instance['widget']['module'] . '_field_widget_form';
  if (function_exists($function)) {
    for ($delta = 0; $delta <= $max; $delta++) {
      $multiple = $field['cardinality'] > 1 || $field['cardinality'] == FIELD_CARDINALITY_UNLIMITED;
      $element = array(
        '#entity_type' => $instance['entity_type'],
        '#entity' => $form['#entity'],
        '#bundle' => $instance['bundle'],
        '#field_name' => $field_name,
        '#language' => $langcode,
        '#field_parents' => $parents,
        '#columns' => array_keys($field['columns']),
        '#title' => $title,
        '#description' => $description,
        // Only the first widget should be required.
        '#required' => $delta == 0 && $instance['required'],
        '#delta' => $delta,
        '#weight' => $delta,
      );
      // For multiple fields, title and description are handled by the wrapping
      // table.
      if ($multiple) {
        if ($delta == 0) {
          $element['#title'] = $title;
        }
        else {
          $element['#title'] = t('!title (value @number)', array('@number' => $delta + 1, '!title' => $title));
        }
        $element['#title_display'] = 'invisible';
        $element['#description'] = '';
      }
      if ($element = $function($form, $form_state, $field, $instance, $langcode, $items, $delta, $element)) {
        // Input field for the delta (drag-n-drop reordering).
        if ($multiple) {
          // We name the element '_weight' to avoid clashing with elements
          // defined by widget.
          $element['_weight'] = array(
            '#type' => 'weight',
            '#title' => t('Weight for row @number', array('@number' => $delta + 1)),
            '#title_display' => 'invisible',
             // Note: this 'delta' is the FAPI 'weight' element's property.
            '#delta' => $max,
            '#default_value' => isset($items[$delta]['_weight']) ? $items[$delta]['_weight'] : $delta,
            '#weight' => 100,
          );
        }

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

        $field_elements[$delta] = $element;
      }
    }

    if ($field_elements) {
      $field_elements += array(
        '#theme' => 'field_multiple_value_form',
        '#field_name' => $field['field_name'],
        '#cardinality' => $field['cardinality'],
        '#title' => $title,
        '#required' => $instance['required'],
        '#description' => $description,
        '#prefix' => '<div id="' . $wrapper_id . '">',
        '#suffix' => '</div>',
        '#max_delta' => $max,
      );
      // Add 'add more' button, if not working with a programmed form.
      if ($field['cardinality'] == FIELD_CARDINALITY_UNLIMITED && empty($form_state['programmed'])) {
        $field_elements['add_more'] = array(
          '#type' => 'submit',
          '#name' => strtr($id_prefix, '-', '_') . '_add_more',
          '#value' => t('Add another item'),
          '#attributes' => array('class' => array('field-add-more-submit')),
          '#limit_validation_errors' => array(array_merge($parents, array($field_name, $langcode))),
          '#submit' => array('field_add_more_submit'),
          '#ajax' => array(
            'callback' => 'field_add_more_js',
            'wrapper' => $wrapper_id,
            'effect' => 'fade',
          ),
        );
      }
    }
  }

  return $field_elements;
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
