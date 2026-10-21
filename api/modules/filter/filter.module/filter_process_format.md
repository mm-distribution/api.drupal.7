# filter_process_format()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 851–980 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L851-L980)
- **Module/theme:** filter

## Signature

```php
function filter_process_format($element)
```

## Documentation

```text
Expands an element into a base element with text format selector attached.

The form element will be expanded into two separate form elements, one
holding the original element, and the other holding the text format selector:
- value: Holds the original element, having its #type changed to the value of
  #base_type or 'textarea' by default.
- format: Holds the text format fieldset and the text format selection, using
  the text format id specified in #format or the user's default format by
  default, if NULL.

The resulting value for the element will be an array holding the value and
the format. For example, the value for the body element will be:
@code
  $form_state['values']['body']['value'] = 'foo';
  $form_state['values']['body']['format'] = 'foo';
@endcode

@param $element
  The form element to process. Properties used:
  - #base_type: The form element #type to use for the 'value' element.
    'textarea' by default.
  - #format: (optional) The text format ID to preselect. If NULL or not set,
    the default format for the current user will be used.

@return
  The expanded element.
```

## Code

```php
function filter_process_format($element) {
  global $user;

  // Ensure that children appear as subkeys of this element.
  $element['#tree'] = TRUE;
  $blacklist = array(
    // Make form_builder() regenerate child properties.
    '#parents',
    '#id',
    '#name',
    // Do not copy this #process function to prevent form_builder() from
    // recursing infinitely.
    '#process',
    // Description is handled by theme_text_format_wrapper().
    '#description',
    // Ensure proper ordering of children.
    '#weight',
    // Properties already processed for the parent element.
    '#prefix',
    '#suffix',
    '#attached',
    '#processed',
    '#theme_wrappers',
  );
  // Move this element into sub-element 'value'.
  unset($element['value']);
  foreach (element_properties($element) as $key) {
    if (!in_array($key, $blacklist)) {
      $element['value'][$key] = $element[$key];
    }
  }

  $element['value']['#type'] = $element['#base_type'];
  $element['value'] += element_info($element['#base_type']);

  // Turn original element into a text format wrapper.
  $path = drupal_get_path('module', 'filter');
  $element['#attached']['js'][] = $path . '/filter.js';
  $element['#attached']['css'][] = $path . '/filter.css';

  // Setup child container for the text format widget.
  $element['format'] = array(
    '#type' => 'fieldset',
    '#attributes' => array('class' => array('filter-wrapper')),
  );

  // Prepare text format guidelines.
  $element['format']['guidelines'] = array(
    '#type' => 'container',
    '#attributes' => array('class' => array('filter-guidelines')),
    '#weight' => 20,
  );
  // Get a list of formats that the current user has access to.
  $formats = filter_formats($user);
  foreach ($formats as $format) {
    $options[$format->format] = $format->name;
    $element['format']['guidelines'][$format->format] = array(
      '#theme' => 'filter_guidelines',
      '#format' => $format,
    );
  }

  // Use the default format for this user if none was selected.
  if (!isset($element['#format'])) {
    $element['#format'] = filter_default_format($user);
  }

  $element['format']['format'] = array(
    '#type' => 'select',
    '#title' => t('Text format'),
    '#options' => $options,
    '#default_value' => $element['#format'],
    '#access' => count($formats) > 1,
    '#weight' => 10,
    '#attributes' => array('class' => array('filter-list')),
    '#parents' => array_merge($element['#parents'], array('format')),
  );

  $element['format']['help'] = array(
    '#type' => 'container',
    '#theme' => 'filter_tips_more_info',
    '#attributes' => array('class' => array('filter-help')),
    '#weight' => 0,
  );

  $all_formats = filter_formats();
  $format_exists = isset($all_formats[$element['#format']]);
  $user_has_access = isset($formats[$element['#format']]);
  $user_is_admin = user_access('administer filters');

  // If the stored format does not exist, administrators have to assign a new
  // format.
  if (!$format_exists && $user_is_admin) {
    $element['format']['format']['#required'] = TRUE;
    $element['format']['format']['#default_value'] = NULL;
    // Force access to the format selector (it may have been denied above if
    // the user only has access to a single format).
    $element['format']['format']['#access'] = TRUE;
  }
  // Disable this widget, if the user is not allowed to use the stored format,
  // or if the stored format does not exist. The 'administer filters' permission
  // only grants access to the filter administration, not to all formats.
  elseif (!$user_has_access || !$format_exists) {
    // Overload default values into #value to make them unalterable.
    $element['value']['#value'] = $element['value']['#default_value'];
    $element['format']['format']['#value'] = $element['format']['format']['#default_value'];

    // Prepend #pre_render callback to replace field value with user notice
    // prior to rendering.
    $element['value'] += array('#pre_render' => array());
    array_unshift($element['value']['#pre_render'], 'filter_form_access_denied');

    // Cosmetic adjustments.
    if (isset($element['value']['#rows'])) {
      $element['value']['#rows'] = 3;
    }
    $element['value']['#disabled'] = TRUE;
    $element['value']['#resizable'] = FALSE;

    // Hide the text format selector and any other child element (such as text
    // field's summary).
    foreach (element_children($element) as $key) {
      if ($key != 'value') {
        $element[$key]['#access'] = FALSE;
      }
    }
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
