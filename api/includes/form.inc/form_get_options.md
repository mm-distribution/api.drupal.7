# form_get_options()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2909–2925 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2909-L2925)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_get_options($element, $key)
```

## Documentation

```text
Returns the indexes of a select element's options matching a given key.

This function is useful if you need to modify the options that are
already in a form element; for example, to remove choices which are
not valid because of additional filters imposed by another module.
One example might be altering the choices in a taxonomy selector.
To correctly handle the case of a multiple hierarchy taxonomy,
#options arrays can now hold an array of objects, instead of a
direct mapping of keys to labels, so that multiple choices in the
selector can have the same key (and label). This makes it difficult
to manipulate directly, which is why this helper function exists.

This function does not support optgroups (when the elements of the
#options array are themselves arrays), and will return FALSE if
arrays are found. The caller must either flatten/restore or
manually do their manipulations in this case, since returning the
index is not sufficient, and supporting this would make the
"helper" too complicated and cumbersome to be of any help.

As usual with functions that can return array() or FALSE, do not
forget to use === and !== if needed.

@param $element
  The select element to search.
@param $key
  The key to look for.

@return
  An array of indexes that match the given $key. Array will be
  empty if no elements were found. FALSE if optgroups were found.
```

## Code

```php
function form_get_options($element, $key) {
  $keys = array();
  foreach ($element['#options'] as $index => $choice) {
    if (is_array($choice)) {
      return FALSE;
    }
    elseif (is_object($choice)) {
      if (isset($choice->option[$key])) {
        $keys[] = $index;
      }
    }
    elseif ($index == $key) {
      $keys[] = $index;
    }
  }
  return $keys;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
