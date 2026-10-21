# text_field_widget_form()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 512–572 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L512-L572)
- **Module/theme:** text
- **Implements:** [hook_field_widget_form()](../../../field.api.php/hook_field_widget_form.md)

## Signature

```php
function text_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element)
```

## Documentation

```text
Implements hook_field_widget_form().
```

## Code

```php
function text_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  $summary_widget = array();
  $main_widget = array();

  switch ($instance['widget']['type']) {
    case 'text_textfield':
      $main_widget = $element + array(
        '#type' => 'textfield',
        '#default_value' => isset($items[$delta]['value']) ? $items[$delta]['value'] : NULL,
        '#size' => $instance['widget']['settings']['size'],
        '#maxlength' => $field['settings']['max_length'],
        '#attributes' => array('class' => array('text-full')),
      );
      break;

    case 'text_textarea_with_summary':
      $display = !empty($items[$delta]['summary']) || !empty($instance['settings']['display_summary']);
      $summary_widget = array(
        '#type' => $display ? 'textarea' : 'value',
        '#default_value' => isset($items[$delta]['summary']) ? $items[$delta]['summary'] : NULL,
        '#title' => t('Summary'),
        '#rows' => $instance['widget']['settings']['summary_rows'],
        '#description' => t('Leave blank to use trimmed value of full text as the summary.'),
        '#attached' => array(
          'js' => array(drupal_get_path('module', 'text') . '/text.js'),
        ),
        '#attributes' => array('class' => array('text-summary')),
        '#prefix' => '<div class="text-summary-wrapper">',
        '#suffix' => '</div>',
        '#weight' => -10,
      );
      // Fall through to the next case.

    case 'text_textarea':
      $main_widget = $element + array(
        '#type' => 'textarea',
        '#default_value' => isset($items[$delta]['value']) ? $items[$delta]['value'] : NULL,
        '#rows' => $instance['widget']['settings']['rows'],
        '#attributes' => array('class' => array('text-full')),
      );
      break;
  }

  if ($main_widget) {
    // Conditionally alter the form element's type if text processing is enabled.
    if ($instance['settings']['text_processing']) {
      $element = $main_widget;
      $element['#type'] = 'text_format';
      $element['#format'] = isset($items[$delta]['format']) ? $items[$delta]['format'] : NULL;
      $element['#base_type'] = $main_widget['#type'];
    }
    else {
      $element['value'] = $main_widget;
    }
  }
  if ($summary_widget) {
    $element['summary'] = $summary_widget;
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
