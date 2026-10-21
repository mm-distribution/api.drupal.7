# ajax_pre_render_element()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 673–810 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L673-L810)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_pre_render_element($element)
```

## Documentation

```text
Adds Ajax information about an element to communicate with JavaScript.

If #ajax['path'] is set on an element, this additional JavaScript is added
to the page header to attach the Ajax behaviors. See ajax.js for more
information.

@param $element
  An associative array containing the properties of the element.
  Properties used:
  - #ajax['event']
  - #ajax['prevent']
  - #ajax['path']
  - #ajax['options']
  - #ajax['wrapper']
  - #ajax['parameters']
  - #ajax['effect']

@return
  The processed element with the necessary JavaScript attached to it.
```

## Code

```php
function ajax_pre_render_element($element) {
  // Skip already processed elements.
  if (isset($element['#ajax_processed'])) {
    return $element;
  }
  // Initialize #ajax_processed, so we do not process this element again.
  $element['#ajax_processed'] = FALSE;

  // Nothing to do if there is neither a callback nor a path.
  if (!(isset($element['#ajax']['callback']) || isset($element['#ajax']['path']))) {
    return $element;
  }

  // Add a reasonable default event handler if none was specified.
  if (isset($element['#ajax']) && !isset($element['#ajax']['event'])) {
    switch ($element['#type']) {
      case 'submit':
      case 'button':
      case 'image_button':
        // Pressing the ENTER key within a textfield triggers the click event of
        // the form's first submit button. Triggering Ajax in this situation
        // leads to problems, like breaking autocomplete textfields, so we bind
        // to mousedown instead of click.
        // @see http://drupal.org/node/216059
        $element['#ajax']['event'] = 'mousedown';
        // Retain keyboard accessibility by setting 'keypress'. This causes
        // ajax.js to trigger 'event' when SPACE or ENTER are pressed while the
        // button has focus.
        $element['#ajax']['keypress'] = TRUE;
        // Binding to mousedown rather than click means that it is possible to
        // trigger a click by pressing the mouse, holding the mouse button down
        // until the Ajax request is complete and the button is re-enabled, and
        // then releasing the mouse button. Set 'prevent' so that ajax.js binds
        // an additional handler to prevent such a click from triggering a
        // non-Ajax form submission. This also prevents a textfield's ENTER
        // press triggering this button's non-Ajax form submission behavior.
        if (!isset($element['#ajax']['prevent'])) {
          $element['#ajax']['prevent'] = 'click';
        }
        break;

      case 'password':
      case 'textfield':
      case 'textarea':
        $element['#ajax']['event'] = 'blur';
        break;

      case 'radio':
      case 'checkbox':
      case 'select':
        $element['#ajax']['event'] = 'change';
        break;

      case 'link':
        $element['#ajax']['event'] = 'click';
        break;

      default:
        return $element;
    }
  }

  // Attach JavaScript settings to the element.
  if (isset($element['#ajax']['event'])) {
    $element['#attached']['library'][] = array('system', 'jquery.form');
    $element['#attached']['library'][] = array('system', 'drupal.ajax');

    $settings = $element['#ajax'];

    // Assign default settings.
    $settings += array(
      'path' => 'system/ajax',
      'options' => array(),
    );

    // @todo Legacy support. Remove in Drupal 8.
    if (isset($settings['method']) && $settings['method'] == 'replace') {
      $settings['method'] = 'replaceWith';
    }

    // Change path to URL.
    $settings['url'] = url($settings['path'], $settings['options']);
    unset($settings['path'], $settings['options']);

    // Add special data to $settings['submit'] so that when this element
    // triggers an Ajax submission, Drupal's form processing can determine which
    // element triggered it.
    // @see _form_element_triggered_scripted_submission()
    if (isset($settings['trigger_as'])) {
      // An element can add a 'trigger_as' key within #ajax to make the element
      // submit as though another one (for example, a non-button can use this
      // to submit the form as though a button were clicked). When using this,
      // the 'name' key is always required to identify the element to trigger
      // as. The 'value' key is optional, and only needed when multiple elements
      // share the same name, which is commonly the case for buttons.
      $settings['submit']['_triggering_element_name'] = $settings['trigger_as']['name'];
      if (isset($settings['trigger_as']['value'])) {
        $settings['submit']['_triggering_element_value'] = $settings['trigger_as']['value'];
      }
      unset($settings['trigger_as']);
    }
    elseif (isset($element['#name'])) {
      // Most of the time, elements can submit as themselves, in which case the
      // 'trigger_as' key isn't needed, and the element's name is used.
      $settings['submit']['_triggering_element_name'] = $element['#name'];
      // If the element is a (non-image) button, its name may not identify it
      // uniquely, in which case a match on value is also needed.
      // @see _form_button_was_clicked()
      if (isset($element['#button_type']) && empty($element['#has_garbage_value'])) {
        $settings['submit']['_triggering_element_value'] = $element['#value'];
      }
    }

    // Convert a simple #ajax['progress'] string into an array.
    if (isset($settings['progress']) && is_string($settings['progress'])) {
      $settings['progress'] = array('type' => $settings['progress']);
    }
    // Change progress path to a full URL.
    if (isset($settings['progress']['path'])) {
      $settings['progress']['url'] = url($settings['progress']['path']);
      unset($settings['progress']['path']);
    }

    $element['#attached']['js'][] = array(
      'type' => 'setting',
      'data' => array(
        'ajax' => array($element['#id'] => $settings),
        'urlIsAjaxTrusted' => array(
          $settings['url'] => TRUE,
        ),
      ),
    );

    // Indicate that Ajax processing was successful.
    $element['#ajax_processed'] = TRUE;
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
