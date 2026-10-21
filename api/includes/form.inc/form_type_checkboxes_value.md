# form_type_checkboxes_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2403–2429 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2403-L2429)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_checkboxes_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a checkboxes form element.

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
function form_type_checkboxes_value($element, $input = FALSE) {
  if ($input === FALSE) {
    $value = array();
    $element += array('#default_value' => array());
    foreach ($element['#default_value'] as $key) {
      $value[$key] = $key;
    }
    return $value;
  }
  elseif (is_array($input)) {
    // Programmatic form submissions use NULL to indicate that a checkbox
    // should be unchecked; see drupal_form_submit(). We therefore remove all
    // NULL elements from the array before constructing the return value, to
    // simulate the behavior of web browsers (which do not send unchecked
    // checkboxes to the server at all). This will not affect non-programmatic
    // form submissions, since all values in $_POST are strings.
    foreach ($input as $key => $value) {
      if (!isset($value)) {
        unset($input[$key]);
      }
    }
    return drupal_map_assoc($input);
  }
  else {
    return array();
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
