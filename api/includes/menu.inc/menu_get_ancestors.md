# menu_get_ancestors()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 327–369 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L327-L369)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_ancestors($parts)
```

## Documentation

```text
Returns the ancestors (and relevant placeholders) for any given path.

For example, the ancestors of node/12345/edit are:
- node/12345/edit
- node/12345/%
- node/%/edit
- node/%/%
- node/12345
- node/%
- node

To generate these, we will use binary numbers. Each bit represents a
part of the path. If the bit is 1, then it represents the original
value while 0 means wildcard. If the path is node/12/edit/foo
then the 1011 bitstring represents node/%/edit/foo where % means that
any argument matches that part. We limit ourselves to using binary
numbers that correspond the patterns of wildcards of router items that
actually exists. This list of 'masks' is built in menu_rebuild().

@param $parts
  An array of path parts; for the above example,
  array('node', '12345', 'edit').

@return
  An array which contains the ancestors and placeholders. Placeholders
  simply contain as many '%s' as the ancestors.
```

## Code

```php
function menu_get_ancestors($parts) {
  $number_parts = count($parts);
  $ancestors = array();
  $length =  $number_parts - 1;
  $end = (1 << $number_parts) - 1;
  $masks = variable_get('menu_masks');
  // If the optimized menu_masks array is not available use brute force to get
  // the correct $ancestors and $placeholders returned. Do not use this as the
  // default value of the menu_masks variable to avoid building such a big
  // array.
  if (!$masks) {
    $masks = range(511, 1);
  }
  // Only examine patterns that actually exist as router items (the masks).
  foreach ($masks as $i) {
    if ($i > $end) {
      // Only look at masks that are not longer than the path of interest.
      continue;
    }
    elseif ($i < (1 << $length)) {
      // We have exhausted the masks of a given length, so decrease the length.
      --$length;
    }
    $current = '';
    for ($j = $length; $j >= 0; $j--) {
      // Check the bit on the $j offset.
      if ($i & (1 << $j)) {
        // Bit one means the original value.
        $current .= $parts[$length - $j];
      }
      else {
        // Bit zero means means wildcard.
        $current .= '%';
      }
      // Unless we are at offset 0, add a slash.
      if ($j) {
        $current .= '/';
      }
    }
    $ancestors[] = $current;
  }
  return $ancestors;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
