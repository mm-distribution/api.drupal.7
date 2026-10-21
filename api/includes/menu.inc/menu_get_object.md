# menu_get_object()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 982–987 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L982-L987)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_object($type = 'node', $position = 1, $path = NULL)
```

## Documentation

```text
Gets a loaded object from a router item.

menu_get_object() provides access to objects loaded by the current router
item. For example, on the page node/%node, the router loads the %node object,
and calling menu_get_object() will return that. Normally, it is necessary to
specify the type of object referenced, however node is the default.
The following example tests to see whether the node being displayed is of the
"story" content type:
@code
$node = menu_get_object();
$story = $node->type == 'story';
@endcode

@param $type
  Type of the object. These appear in hook_menu definitions as %type. Core
  provides aggregator_feed, aggregator_category, contact, filter_format,
  forum_term, menu, menu_link, node, taxonomy_vocabulary, user. See the
  relevant {$type}_load function for more on each. Defaults to node.
@param $position
  The position of the object in the path, where the first path segment is 0.
  For node/%node, the position of %node is 1, but for comment/reply/%node,
  it's 2. Defaults to 1.
@param $path
  See menu_get_item() for more on this. Defaults to the current path.
```

## Code

```php
function menu_get_object($type = 'node', $position = 1, $path = NULL) {
  $router_item = menu_get_item($path);
  if (isset($router_item['load_functions'][$position]) && !empty($router_item['map'][$position]) && $router_item['load_functions'][$position] == $type . '_load') {
    return $router_item['map'][$position];
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
