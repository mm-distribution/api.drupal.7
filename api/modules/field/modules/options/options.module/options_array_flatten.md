# options_array_flatten()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 376–389 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L376-L389)
- **Module/theme:** options

## Signature

```php
function options_array_flatten($array)
```

## Documentation

```text
Flattens an array of allowed values.

@param $array
  A single or multidimensional array.
@return
  A flattened array.
```

## Code

```php
function options_array_flatten($array) {
  $result = array();
  if (is_array($array)) {
    foreach ($array as $key => $value) {
      if (is_array($value)) {
        $result += options_array_flatten($value);
      }
      else {
        $result[$key] = $value;
      }
    }
  }
  return $result;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
