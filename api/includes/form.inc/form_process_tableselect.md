# form_process_tableselect()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3553–3618 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3553-L3618)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_tableselect($element)
```

## Documentation

```text
Creates checkbox or radio elements to populate a tableselect table.

@param $element
  An associative array containing the properties and children of the
  tableselect element.

@return
  The processed element.
```

## Code

```php
function form_process_tableselect($element) {

  if ($element['#multiple']) {
    $value = is_array($element['#value']) ? $element['#value'] : array();
  }
  else {
    // Advanced selection behavior makes no sense for radios.
    $element['#js_select'] = FALSE;
  }

  $element['#tree'] = TRUE;

  if (count($element['#options']) > 0) {
    if (!isset($element['#default_value']) || $element['#default_value'] === 0) {
      $element['#default_value'] = array();
    }

    // Create a checkbox or radio for each item in #options in such a way that
    // the value of the tableselect element behaves as if it had been of type
    // checkboxes or radios.
    foreach ($element['#options'] as $key => $choice) {
      // Do not overwrite manually created children.
      if (!isset($element[$key])) {
        if ($element['#multiple']) {
          $title = '';
          if (!empty($element['#options'][$key]['title']['data']['#title'])) {
            $title = t('Update @title', array(
              '@title' => $element['#options'][$key]['title']['data']['#title'],
            ));
          }
          $element[$key] = array(
            '#type' => 'checkbox',
            '#title' => $title,
            '#title_display' => 'invisible',
            '#return_value' => $key,
            '#default_value' => isset($value[$key]) ? $key : NULL,
            '#attributes' => $element['#attributes'],
            '#ajax' => isset($element['#ajax']) ? $element['#ajax'] : NULL,
          );
        }
        else {
          // Generate the parents as the autogenerator does, so we will have a
          // unique id for each radio button.
          $parents_for_id = array_merge($element['#parents'], array($key));
          $element[$key] = array(
            '#type' => 'radio',
            '#title' => '',
            '#return_value' => $key,
            '#default_value' => ($element['#default_value'] == $key) ? $key : NULL,
            '#attributes' => $element['#attributes'],
            '#parents' => $element['#parents'],
            '#id' => drupal_html_id('edit-' . implode('-', $parents_for_id)),
            '#ajax' => isset($element['#ajax']) ? $element['#ajax'] : NULL,
          );
        }
        if (isset($element['#options'][$key]['#weight'])) {
          $element[$key]['#weight'] = $element['#options'][$key]['#weight'];
        }
      }
    }
  }
  else {
    $element['#value'] = array();
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
