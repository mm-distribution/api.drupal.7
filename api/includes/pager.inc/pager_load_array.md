# pager_load_array()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 697–709 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L697-L709)

## Signature

```php
function pager_load_array($value, $element, $old_array)
```

## Documentation

```text
Helper function

Copies $old_array to $new_array and sets $new_array[$element] = $value
Fills in $new_array[0 .. $element - 1] = 0
```

## Code

```php
function pager_load_array($value, $element, $old_array) {
  $new_array = $old_array;
  // Look for empty elements.
  for ($i = 0; $i < $element; $i++) {
    if (empty($new_array[$i])) {
      // Load found empty element with 0.
      $new_array[$i] = 0;
    }
  }
  // Update the changed element.
  $new_array[$element] = (int) $value;
  return $new_array;
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
