# form_process_vertical_tabs()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3882–3906 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3882-L3906)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_vertical_tabs($element, &$form_state)
```

## Documentation

```text
Creates a group formatted as vertical tabs.

@param $element
  An associative array containing the properties and children of the
  fieldset.
@param $form_state
  The $form_state array for the form this vertical tab widget belongs to.

@return
  The processed element.
```

## Code

```php
function form_process_vertical_tabs($element, &$form_state) {
  // Inject a new fieldset as child, so that form_process_fieldset() processes
  // this fieldset like any other fieldset.
  $element['group'] = array(
    '#type' => 'fieldset',
    '#theme_wrappers' => array(),
    '#parents' => $element['#parents'],
  );

  // The JavaScript stores the currently selected tab in this hidden
  // field so that the active tab can be restored the next time the
  // form is rendered, e.g. on preview pages or when form validation
  // fails.
  $name = implode('__', $element['#parents']);
  if (isset($form_state['values'][$name . '__active_tab'])) {
    $element['#default_tab'] = $form_state['values'][$name . '__active_tab'];
  }
  $element[$name . '__active_tab'] = array(
    '#type' => 'hidden',
    '#default_value' => $element['#default_tab'],
    '#attributes' => array('class' => array('vertical-tabs-active-tab')),
  );

  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
