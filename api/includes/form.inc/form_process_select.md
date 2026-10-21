# form_process_select()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2753–2781 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2753-L2781)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_select($element)
```

## Documentation

```text
Processes a select list form element.

This process callback is mandatory for select fields, since all user agents
automatically preselect the first available option of single (non-multiple)
select lists.

@param $element
  The form element to process. Properties used:
  - #multiple: (optional) Indicates whether one or more options can be
    selected. Defaults to FALSE.
  - #default_value: Must be NULL or not set in case there is no value for the
    element yet, in which case a first default option is inserted by default.
    Whether this first option is a valid option depends on whether the field
    is #required or not.
  - #required: (optional) Whether the user needs to select an option (TRUE)
    or not (FALSE). Defaults to FALSE.
  - #empty_option: (optional) The label to show for the first default option.
    By default, the label is automatically set to "- Select -" for a required
    field and "- None -" for an optional field.
  - #empty_value: (optional) The value for the first default option, which is
    used to determine whether the user submitted a value or not.
    - If #required is TRUE, this defaults to '' (an empty string).
    - If #required is not TRUE and this value isn't set, then no extra option
      is added to the select control, leaving the control in a slightly
      illogical state, because there's no way for the user to select nothing,
      since all user agents automatically preselect the first available
      option. But people are used to this being the behavior of select
      controls.
      @todo Address the above issue in Drupal 8.
    - If #required is not TRUE and this value is set (most commonly to an
      empty string), then an extra option (see #empty_option above)
      representing a "non-selection" is added with this as its value.

@see _form_validate()
```

## Code

```php
function form_process_select($element) {
  // #multiple select fields need a special #name.
  if ($element['#multiple']) {
    $element['#attributes']['multiple'] = 'multiple';
    $element['#attributes']['name'] = $element['#name'] . '[]';
  }
  // A non-#multiple select needs special handling to prevent user agents from
  // preselecting the first option without intention. #multiple select lists do
  // not get an empty option, as it would not make sense, user interface-wise.
  else {
    $required = $element['#required'];
    // If the element is required and there is no #default_value, then add an
    // empty option that will fail validation, so that the user is required to
    // make a choice. Also, if there's a value for #empty_value or
    // #empty_option, then add an option that represents emptiness.
    if (($required && !isset($element['#default_value'])) || isset($element['#empty_value']) || isset($element['#empty_option'])) {
      $element += array(
        '#empty_value' => '',
        '#empty_option' => $required ? t('- Select -') : t('- None -'),
      );
      // The empty option is prepended to #options and purposively not merged
      // to prevent another option in #options mistakenly using the same value
      // as #empty_value.
      $empty_option = array($element['#empty_value'] => $element['#empty_option']);
      $element['#options'] = $empty_option + $element['#options'];
    }
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
