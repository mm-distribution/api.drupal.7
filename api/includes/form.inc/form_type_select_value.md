# form_type_select_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2550–2576 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2550-L2576)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_select_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a select form element.

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
function form_type_select_value($element, $input = FALSE) {
  if ($input !== FALSE) {
    if (isset($element['#multiple']) && $element['#multiple']) {
      // If an enabled multi-select submits NULL, it means all items are
      // unselected. A disabled multi-select always submits NULL, and the
      // default value should be used.
      if (empty($element['#disabled'])) {
        return (is_array($input)) ? drupal_map_assoc($input) : array();
      }
      else {
        return (isset($element['#default_value']) && is_array($element['#default_value'])) ? $element['#default_value'] : array();
      }
    }
    // Non-multiple select elements may have an empty option preprended to them
    // (see form_process_select()). When this occurs, usually #empty_value is
    // an empty string, but some forms set #empty_value to integer 0 or some
    // other non-string constant. PHP receives all submitted form input as
    // strings, but if the empty option is selected, set the value to match the
    // empty value exactly.
    elseif (isset($element['#empty_value']) && $input === (string) $element['#empty_value']) {
      return $element['#empty_value'];
    }
    else {
      return $input;
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
