# drupal_array_set_nested_value()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6951–6962 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6951-L6962)

## Signature

```php
function drupal_array_set_nested_value(array &$array, array $parents, $value, $force = FALSE)
```

## Documentation

```text
Sets a value in a nested array with variable depth.

This helper function should be used when the depth of the array element you
are changing may vary (that is, the number of parent keys is variable). It
is primarily used for form structures and renderable arrays.

Example:
@code
// Assume you have a 'signature' element somewhere in a form. It might be:
$form['signature_settings']['signature'] = array(
  '#type' => 'text_format',
  '#title' => t('Signature'),
);
// Or, it might be further nested:
$form['signature_settings']['user']['signature'] = array(
  '#type' => 'text_format',
  '#title' => t('Signature'),
);
@endcode

To deal with the situation, the code needs to figure out the route to the
element, given an array of parents that is either
@code array('signature_settings', 'signature') @endcode in the first case or
@code array('signature_settings', 'user', 'signature') @endcode in the second
case.

Without this helper function the only way to set the signature element in one
line would be using eval(), which should be avoided:
@code
// Do not do this! Avoid eval().
eval('$form[\'' . implode("']['", $parents) . '\'] = $element;');
@endcode

Instead, use this helper function:
@code
drupal_array_set_nested_value($form, $parents, $element);
@endcode

However if the number of array parent keys is static, the value should always
be set directly rather than calling this function. For instance, for the
first example we could just do:
@code
$form['signature_settings']['signature'] = $element;
@endcode

@param $array
  A reference to the array to modify.
@param $parents
  An array of parent keys, starting with the outermost key.
@param $value
  The value to set.
@param $force
  (Optional) If TRUE, the value is forced into the structure even if it
  requires the deletion of an already existing non-array parent value. If
  FALSE, PHP throws an error if trying to add into a value that is not an
  array. Defaults to FALSE.

@see drupal_array_get_nested_value()
```

## Code

```php
function drupal_array_set_nested_value(array &$array, array $parents, $value, $force = FALSE) {
  $ref = &$array;
  foreach ($parents as $parent) {
    // PHP auto-creates container arrays and NULL entries without error if $ref
    // is NULL, but throws an error if $ref is set, but not an array.
    if ($force && isset($ref) && !is_array($ref)) {
      $ref = array();
    }
    $ref = &$ref[$parent];
  }
  $ref = $value;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
