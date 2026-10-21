# form_process_radios()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3195–3226 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3195-L3226)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_radios($element)
```

## Documentation

```text
Expands a radios element into individual radio elements.
```

## Code

```php
function form_process_radios($element) {
  if (count($element['#options']) > 0) {
    $weight = 0;
    foreach ($element['#options'] as $key => $choice) {
      // Maintain order of options as defined in #options, in case the element
      // defines custom option sub-elements, but does not define all option
      // sub-elements.
      $weight += 0.001;

      $element += array($key => array());
      // Generate the parents as the autogenerator does, so we will have a
      // unique id for each radio button.
      $parents_for_id = array_merge($element['#parents'], array($key));
      $element[$key] += array(
        '#type' => 'radio',
        '#title' => $choice,
        // The key is sanitized in drupal_attributes() during output from the
        // theme function.
        '#return_value' => $key,
        // Use default or FALSE. A value of FALSE means that the radio button is
        // not 'checked'.
        '#default_value' => isset($element['#default_value']) ? $element['#default_value'] : FALSE,
        '#attributes' => $element['#attributes'],
        '#parents' => $element['#parents'],
        '#id' => drupal_html_id('edit-' . implode('-', $parents_for_id)),
        '#ajax' => isset($element['#ajax']) ? $element['#ajax'] : NULL,
        '#weight' => $weight,
      );
    }
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
