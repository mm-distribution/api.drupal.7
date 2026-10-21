# comment_modules_enabled()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 64–77 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L64-L77)
- **Module/theme:** comment
- **Implements:** [hook_modules_enabled()](../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function comment_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().

Creates comment body fields for node types existing before the comment module
is enabled. We use hook_modules_enabled() rather than hook_enable() so we can
react to node types of existing modules, and those of modules being enabled
both before and after comment module in the loop of module_enable().

There is a separate comment bundle for each node type to allow for
per-node-type customization of comment fields. Each one of these bundles
needs a comment body field instance. A comment bundle is needed even for
node types whose comments are disabled by default, because individual nodes
may override that default.

@see comment_node_type_insert()
```

## Code

```php
function comment_modules_enabled($modules) {
  // Only react if comment module is one of the modules being enabled.
  // hook_node_type_insert() is used to create body fields while the comment
  // module is enabled.
  if (in_array('comment', $modules)) {
    // Ensure that the list of node types reflects newly enabled modules.
    node_types_rebuild();

    // Create comment body fields for each node type, if needed.
    foreach (node_type_get_types() as $type => $info) {
      _comment_body_field_create($info);
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
