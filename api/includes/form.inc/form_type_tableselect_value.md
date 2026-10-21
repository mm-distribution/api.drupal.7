# form_type_tableselect_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2444–2465 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2444-L2465)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_tableselect_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a tableselect form element.

@param $element
  The form element whose value is being populated.
@param $input
  The incoming input to populate the form element. If this is FALSE,
  the element's default value should be returned.

@return
  The data that will appear in $form_state['values'] for this element, or
  nothing to use the default.
```

## Code

```php
function form_type_tableselect_value($element, $input = FALSE) {
  // If $element['#multiple'] == FALSE, then radio buttons are displayed and
  // the default value handling is used.
  if (isset($element['#multiple']) && $element['#multiple']) {
    // Checkboxes are being displayed with the default value coming from the
    // keys of the #default_value property. This differs from the checkboxes
    // element which uses the array values.
    if ($input === FALSE) {
      $value = array();
      $element += array('#default_value' => array());
      foreach ($element['#default_value'] as $key => $flag) {
        if ($flag) {
          $value[$key] = $key;
        }
      }
      return $value;
    }
    else {
      return is_array($input) ? drupal_map_assoc($input) : array();
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
