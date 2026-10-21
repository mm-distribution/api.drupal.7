# form_type_image_button_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2316–2347 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2316-L2347)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_image_button_value($form, $input, $form_state)
```

## Documentation

```text
Determines the value for an image button form element.

@param $form
  The form element whose value is being populated.
@param $input
  The incoming input to populate the form element. If this is FALSE,
  the element's default value should be returned.
@param $form_state
  A keyed array containing the current state of the form.

@return
  The data that will appear in $form_state['values'] for this element, or
  nothing to use the default.
```

## Code

```php
function form_type_image_button_value($form, $input, $form_state) {
  if ($input !== FALSE) {
    if (!empty($input)) {
      // If we're dealing with Mozilla or Opera, we're lucky. It will
      // return a proper value, and we can get on with things.
      return $form['#return_value'];
    }
    else {
      // Unfortunately, in IE we never get back a proper value for THIS
      // form element. Instead, we get back two split values: one for the
      // X and one for the Y coordinates on which the user clicked the
      // button. We'll find this element in the #post data, and search
      // in the same spot for its name, with '_x'.
      $input = $form_state['input'];
      foreach (explode('[', $form['#name']) as $element_name) {
        // chop off the ] that may exist.
        if (substr($element_name, -1) == ']') {
          $element_name = substr($element_name, 0, -1);
        }

        if (!isset($input[$element_name])) {
          if (isset($input[$element_name . '_x'])) {
            return $form['#return_value'];
          }
          return NULL;
        }
        $input = $input[$element_name];
      }
      return $form['#return_value'];
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
