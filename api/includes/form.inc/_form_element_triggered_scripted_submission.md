# _form_element_triggered_scripted_submission()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2197–2204 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2197-L2204)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_element_triggered_scripted_submission($element, &$form_state)
```

## Documentation

```text
Detects if an element triggered the form submission via Ajax.

This detects button or non-button controls that trigger a form submission via
Ajax or some other scriptable environment. These environments can set the
special input key '_triggering_element_name' to identify the triggering
element. If the name alone doesn't identify the element uniquely, the input
key '_triggering_element_value' may also be set to require a match on element
value. An example where this is needed is if there are several buttons all
named 'op', and only differing in their value.
```

## Code

```php
function _form_element_triggered_scripted_submission($element, &$form_state) {
  if (!empty($form_state['input']['_triggering_element_name']) && $element['#name'] == $form_state['input']['_triggering_element_name']) {
    if (empty($form_state['input']['_triggering_element_value']) || $form_state['input']['_triggering_element_value'] == $element['#value']) {
      return TRUE;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
