# ajax_form_callback()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 385–413 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L385-L413)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_form_callback()
```

## Documentation

```text
Menu callback; handles Ajax requests for the #ajax Form API property.

This rebuilds the form from cache and invokes the defined #ajax['callback']
to return an Ajax command structure for JavaScript. In case no 'callback' has
been defined, nothing will happen.

The Form API #ajax property can be set both for buttons and other input
elements.

This function is also the canonical example of how to implement
#ajax['path']. If processing is required that cannot be accomplished with
a callback, re-implement this function and set #ajax['path'] to the
enhanced function.

@see system_menu()
```

## Code

```php
function ajax_form_callback() {
  list($form, $form_state, $form_id, $form_build_id, $commands) = ajax_get_form();
  drupal_process_form($form['#form_id'], $form, $form_state);

  // We need to return the part of the form (or some other content) that needs
  // to be re-rendered so the browser can update the page with changed content.
  // Since this is the generic menu callback used by many Ajax elements, it is
  // up to the #ajax['callback'] function of the element (may or may not be a
  // button) that triggered the Ajax request to determine what needs to be
  // rendered.
  if (!empty($form_state['triggering_element'])) {
    $callback = $form_state['triggering_element']['#ajax']['callback'];
  }
  if (!empty($callback) && is_callable($callback)) {
    $result = $callback($form, $form_state);

    if (!(is_array($result) && isset($result['#type']) && $result['#type'] == 'ajax')) {
      // Turn the response into a #type=ajax array if it isn't one already.
      $result = array(
        '#type' => 'ajax',
        '#commands' => ajax_prepare_response($result),
      );
    }

    $result['#commands'] = array_merge($commands, $result['#commands']);

    return $result;
  }
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
