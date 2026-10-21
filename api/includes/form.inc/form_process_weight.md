# form_process_weight()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4158–4189 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4158-L4189)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_weight($element)
```

## Documentation

```text
Expands a weight element into a select element.
```

## Code

```php
function form_process_weight($element) {
  $element['#is_weight'] = TRUE;

  // If the number of options is small enough, use a select field.
  $max_elements = variable_get('drupal_weight_select_max', DRUPAL_WEIGHT_SELECT_MAX);
  if ($element['#delta'] <= $max_elements) {
    $element['#type'] = 'select';
    $weights = array();
    for ($n = (-1 * $element['#delta']); $n <= $element['#delta']; $n++) {
      $weights[$n] = $n;
    }
    if (isset($element['#default_value'])) {
      $default_value = (int) $element['#default_value'];
      if (!isset($weights[$default_value])) {
        $weights[$default_value] = $default_value;
        ksort($weights);
      }
    }
    $element['#options'] = $weights;
    $element += element_info('select');
  }
  // Otherwise, use a text field.
  else {
    $element['#type'] = 'textfield';
    // Use a field big enough to fit most weights.
    $element['#size'] = 10;
    $element['#element_validate'] = array('element_validate_integer');
    $element += element_info('textfield');
  }

  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
