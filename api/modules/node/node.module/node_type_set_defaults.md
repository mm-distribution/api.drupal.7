# node_type_set_defaults()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 806–834 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L806-L834)
- **Module/theme:** node

## Signature

```php
function node_type_set_defaults($info = array())
```

## Documentation

```text
Sets the default values for a node type.

The defaults are appropriate for a type defined through hook_node_info(),
since 'custom' is TRUE for types defined in the user interface, and FALSE
for types defined by modules. (The 'custom' flag prevents types from being
deleted through the user interface.) Also, the default for 'locked' is TRUE,
which prevents users from changing the machine name of the type.

@param $info
  (optional) An object or array containing values to override the defaults.
  See hook_node_info() for details on what the array elements mean. Defaults
  to an empty array.

@return
  A node type object, with missing values in $info set to their defaults.
```

## Code

```php
function node_type_set_defaults($info = array()) {
  $info = (array) $info;
  $new_type = $info + array(
    'type' => '',
    'name' => '',
    'base' => '',
    'description' => '',
    'help' => '',
    'custom' => 0,
    'modified' => 0,
    'locked' => 1,
    'disabled' => 0,
    'is_new' => 1,
    'has_title' => 1,
    'title_label' => 'Title',
  );
  $new_type = (object) $new_type;

  // If the type has no title, set an empty label.
  if (!$new_type->has_title) {
    $new_type->title_label = '';
  }
  if (empty($new_type->module)) {
    $new_type->module = $new_type->base == 'node_content' ? 'node' : '';
  }
  $new_type->orig_type = isset($info['type']) ? $info['type'] : '';

  return $new_type;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
