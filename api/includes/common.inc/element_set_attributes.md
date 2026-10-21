# element_set_attributes()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6840–6851 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6840-L6851)

## Signature

```php
function element_set_attributes(array &$element, array $map)
```

## Documentation

```text
Sets HTML attributes based on element properties.

@param $element
  The renderable element to process.
@param $map
  An associative array whose keys are element property names and whose values
  are the HTML attribute names to set for corresponding the property; e.g.,
  array('#propertyname' => 'attributename'). If both names are identical
  except for the leading '#', then an attribute name value is sufficient and
  no property name needs to be specified.
```

## Code

```php
function element_set_attributes(array &$element, array $map) {
  foreach ($map as $property => $attribute) {
    // If the key is numeric, the attribute name needs to be taken over.
    if (is_int($property)) {
      $property = '#' . $attribute;
    }
    // Do not overwrite already existing attributes.
    if (isset($element[$property]) && !isset($element['#attributes'][$attribute])) {
      $element['#attributes'][$attribute] = $element[$property];
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
