# node_list_permissions()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3142–3165 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3142-L3165)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_list_permissions($type)
```

## Documentation

```text
Helper function to generate standard node permission list for a given type.

@param $type
  The machine-readable name of the node type.

@return array
  An array of permission names and descriptions.
```

## Code

```php
function node_list_permissions($type) {
  $info = node_type_get_type($type);

  // Build standard list of node permissions for this type.
  $perms = array(
    "create $type content" => array(
      'title' => t('%type_name: Create new content', array('%type_name' => $info->name)),
    ),
    "edit own $type content" => array(
      'title' => t('%type_name: Edit own content', array('%type_name' => $info->name)),
    ),
    "edit any $type content" => array(
      'title' => t('%type_name: Edit any content', array('%type_name' => $info->name)),
    ),
    "delete own $type content" => array(
      'title' => t('%type_name: Delete own content', array('%type_name' => $info->name)),
    ),
    "delete any $type content" => array(
      'title' => t('%type_name: Delete any content', array('%type_name' => $info->name)),
    ),
  );

  return $perms;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
