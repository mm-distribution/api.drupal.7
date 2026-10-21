# theme_form_element_label()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4368–4406 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4368-L4406)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_form_element_label($variables)
```

## Documentation

```text
Returns HTML for a form element label and required marker.

Form element labels include the #title and a #required marker. The label is
associated with the element itself by the element #id. Labels may appear
before or after elements, depending on theme_form_element() and
#title_display.

This function will not be called for elements with no labels, depending on
#title_display. For elements that have an empty #title and are not required,
this function will output no label (''). For required elements that have an
empty #title, this will output the required marker alone within the label.
The label will use the #id to associate the marker with the field that is
required. That is especially important for screenreader users to know
which field is required.

To associate the label with a different field, set the #label_for property
to the ID of the desired field.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #required, #title, #id, #value, #description,
    #label_for.

@ingroup themeable
```

## Code

```php
function theme_form_element_label($variables) {
  $element = $variables['element'];
  // This is also used in the installer, pre-database setup.
  $t = get_t();

  // If title and required marker are both empty, output no label.
  if ((!isset($element['#title']) || $element['#title'] === '') && empty($element['#required'])) {
    return '';
  }

  // If the element is required, a required marker is appended to the label.
  $required = !empty($element['#required']) ? theme('form_required_marker', array('element' => $element)) : '';

  $title = filter_xss_admin($element['#title']);

  $attributes = array();
  // Style the label as class option to display inline with the element.
  if ($element['#title_display'] == 'after') {
    $attributes['class'] = 'option';
  }
  // Show label only to screen readers to avoid disruption in visual flows.
  elseif ($element['#title_display'] == 'invisible') {
    $attributes['class'] = 'element-invisible';
  }

  // Use the element's ID as the default value of the "for" attribute (to
  // associate the label with this form element), but allow this to be
  // overridden in order to associate the label with a different form element
  // instead.
  if (!empty($element['#label_for'])) {
    $attributes['for'] = $element['#label_for'];
  }
  elseif (!empty($element['#id'])) {
    $attributes['for'] = $element['#id'];
  }

  // The leading whitespace helps visually separate fields from inline labels.
  return ' <label' . drupal_attributes($attributes) . '>' . $t('!title !required', array('!title' => $title, '!required' => $required)) . "</label>\n";
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
