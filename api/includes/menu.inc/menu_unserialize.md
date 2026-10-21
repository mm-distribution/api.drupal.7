# menu_unserialize()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 406–418 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L406-L418)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_unserialize($data, $map)
```

## Documentation

```text
Unserializes menu data, using a map to replace path elements.

The menu system stores various path-related information (such as the 'page
arguments' and 'access arguments' components of a menu item) in the database
using serialized arrays, where integer values in the arrays represent
arguments to be replaced by values from the path. This function first
unserializes such menu information arrays, and then does the path
replacement.

The path replacement acts on each integer-valued element of the unserialized
menu data array ($data) using a map array ($map, which is typically an array
of path arguments) as a list of replacements. For instance, if there is an
element of $data whose value is the number 2, then it is replaced in $data
with $map[2]; non-integer values in $data are left alone.

As an example, an unserialized $data array with elements ('node_load', 1)
represents instructions for calling the node_load() function. Specifically,
this instruction says to use the path component at index 1 as the input
parameter to node_load(). If the path is 'node/123', then $map will be the
array ('node', 123), and the returned array from this function will have
elements ('node_load', 123), since $map[1] is 123. This return value will
indicate specifically that node_load(123) is to be called to load the node
whose ID is 123 for this menu item.

@param $data
  A serialized array of menu data, as read from the database.
@param $map
  A path argument array, used to replace integer values in $data; an integer
  value N in $data will be replaced by value $map[N]. Typically, the $map
  array is generated from a call to the arg() function.

@return
  The unserialized $data array, with path arguments replaced.
```

## Code

```php
function menu_unserialize($data, $map) {
  if ($data = unserialize($data)) {
    foreach ($data as $k => $v) {
      if (is_int($v)) {
        $data[$k] = isset($map[$v]) ? $map[$v] : '';
      }
    }
    return $data;
  }
  else {
    return array();
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
