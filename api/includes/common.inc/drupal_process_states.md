# drupal_process_states()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 4938–4944 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L4938-L4944)

## Signature

```php
function drupal_process_states(&$elements)
```

## Documentation

```text
Adds JavaScript to change the state of an element based on another element.

A "state" means a certain property on a DOM element, such as "visible" or
"checked". A state can be applied to an element, depending on the state of
another element on the page. In general, states depend on HTML attributes and
DOM element properties, which change due to user interaction.

Since states are driven by JavaScript only, it is important to understand
that all states are applied on presentation only, none of the states force
any server-side logic, and that they will not be applied for site visitors
without JavaScript support. All modules implementing states have to make
sure that the intended logic also works without JavaScript being enabled.

#states is an associative array in the form of:
@code
array(
  STATE1 => CONDITIONS_ARRAY1,
  STATE2 => CONDITIONS_ARRAY2,
  ...
)
@endcode
Each key is the name of a state to apply to the element, such as 'visible'.
Each value is a list of conditions that denote when the state should be
applied.

Multiple different states may be specified to act on complex conditions:
@code
array(
  'visible' => CONDITIONS,
  'checked' => OTHER_CONDITIONS,
)
@endcode

Every condition is a key/value pair, whose key is a jQuery selector that
denotes another element on the page, and whose value is an array of
conditions, which must bet met on that element:
@code
array(
  'visible' => array(
    JQUERY_SELECTOR => REMOTE_CONDITIONS,
    JQUERY_SELECTOR => REMOTE_CONDITIONS,
    ...
  ),
)
@endcode
All conditions must be met for the state to be applied.

Each remote condition is a key/value pair specifying conditions on the other
element that need to be met to apply the state to the element:
@code
array(
  'visible' => array(
    ':input[name="remote_checkbox"]' => array('checked' => TRUE),
  ),
)
@endcode

For example, to show a textfield only when a checkbox is checked:
@code
$form['toggle_me'] = array(
  '#type' => 'checkbox',
  '#title' => t('Tick this box to type'),
);
$form['settings'] = array(
  '#type' => 'textfield',
  '#states' => array(
    // Only show this field when the 'toggle_me' checkbox is enabled.
    'visible' => array(
      ':input[name="toggle_me"]' => array('checked' => TRUE),
    ),
  ),
);
@endcode

The following states may be applied to an element:
- enabled
- disabled
- required
- optional
- visible
- invisible
- checked
- unchecked
- expanded
- collapsed

The following states may be used in remote conditions:
- empty
- filled
- checked
- unchecked
- expanded
- collapsed
- value

The following states exist for both elements and remote conditions, but are
not fully implemented and may not change anything on the element:
- relevant
- irrelevant
- valid
- invalid
- touched
- untouched
- readwrite
- readonly

When referencing select lists and radio buttons in remote conditions, a
'value' condition must be used:
@code
  '#states' => array(
    // Show the settings if 'bar' has been selected for 'foo'.
    'visible' => array(
      ':input[name="foo"]' => array('value' => 'bar'),
    ),
  ),
@endcode

@param $elements
  A renderable array element having a #states property as described above.

@see form_example_states_form()
```

## Code

```php
function drupal_process_states(&$elements) {
  $elements['#attached']['library'][] = array('system', 'drupal.states');
  $elements['#attached']['js'][] = array(
    'type' => 'setting',
    'data' => array('states' => array('#' . $elements['#id'] => $elements['#states'])),
  );
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
