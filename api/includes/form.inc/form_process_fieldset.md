# form_process_fieldset()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3778–3812 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3778-L3812)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_fieldset(&$element, &$form_state)
```

## Documentation

```text
Arranges fieldsets into groups.

@param $element
  An associative array containing the properties and children of the
  fieldset. Note that $element must be taken by reference here, so processed
  child elements are taken over into $form_state.
@param $form_state
  The $form_state array for the form this fieldset belongs to.

@return
  The processed element.
```

## Code

```php
function form_process_fieldset(&$element, &$form_state) {
  $parents = implode('][', $element['#parents']);

  // Each fieldset forms a new group. The #type 'vertical_tabs' basically only
  // injects a new fieldset.
  $form_state['groups'][$parents]['#group_exists'] = TRUE;
  $element['#groups'] = &$form_state['groups'];

  // Process vertical tabs group member fieldsets.
  if (isset($element['#group'])) {
    // Add this fieldset to the defined group (by reference).
    $group = $element['#group'];
    $form_state['groups'][$group][] = &$element;
  }

  // Contains form element summary functionalities.
  $element['#attached']['library'][] = array('system', 'drupal.form');

  // The .form-wrapper class is required for #states to treat fieldsets like
  // containers.
  if (!isset($element['#attributes']['class'])) {
    $element['#attributes']['class'] = array();
  }

  // Collapsible fieldsets
  if (!empty($element['#collapsible'])) {
    $element['#attached']['library'][] = array('system', 'drupal.collapse');
    $element['#attributes']['class'][] = 'collapsible';
    if (!empty($element['#collapsed'])) {
      $element['#attributes']['class'][] = 'collapsed';
    }
  }

  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
