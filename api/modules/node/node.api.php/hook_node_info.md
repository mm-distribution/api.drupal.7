# hook_node_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 916–924 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L916-L924)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_info()
```

## Documentation

```text
Define module-provided node types.

This hook allows a module to define one or more of its own node types. For
example, the blog module uses it to define a blog node-type named "Blog
entry." The name and attributes of each desired node type are specified in an
array returned by the hook.

Only module-provided node types should be defined through this hook. User-
provided (or 'custom') node types should be defined only in the 'node_type'
database table, and should be maintained by using the node_type_save() and
node_type_delete() functions.

@return
  An array of information defining the module's node types. The array
  contains a sub-array for each node type, with the machine-readable type
  name as the key. Each sub-array has up to 10 attributes. Possible
  attributes:
  - name: (required) The human-readable name of the node type.
  - base: (required) The base name for implementations of node-type-specific
    hooks that respond to this node type. Base is usually the name of the
    module or 'node_content', but not always. See
    @link node_api_hooks Node API hooks @endlink for more information.
  - description: (required) A brief description of the node type.
  - help: (optional) Help information shown to the user when creating a node
    of this type.
  - has_title: (optional) A Boolean indicating whether or not this node type
    has a title field.
  - title_label: (optional) The label for the title field of this content
    type.
  - locked: (optional) A Boolean indicating whether the administrator can
    change the machine name of this type. FALSE = changeable (not locked),
    TRUE = unchangeable (locked).

The machine name of a node type should contain only letters, numbers, and
underscores. Underscores will be converted into hyphens for the purpose of
constructing URLs.

All attributes of a node type that are defined through this hook (except for
'locked') can be edited by a site administrator. This includes the
machine-readable name of a node type, if 'locked' is set to FALSE.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_info() {
  return array(
    'blog' => array(
      'name' => t('Blog entry'),
      'base' => 'blog',
      'description' => t('Use for multi-user blogs. Every user gets a personal blog.'),
    )
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_info()".

- [blog_node_info()](../../blog/blog.module/blog_node_info.md) — `modules/blog/blog.module`
- [forum_node_info()](../../forum/forum.module/forum_node_info.md) — `modules/forum/forum.module`
- [poll_node_info()](../../poll/poll.module/poll_node_info.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
