# _update_7000_node_get_types()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 481–502 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L481-L502)
- **Module/theme:** node
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_node_get_types()
```

## Documentation

```text
Utility function: fetch the node types directly from the database.

This function is valid for a database schema version 7000.

@ingroup update_api
```

## Code

```php
function _update_7000_node_get_types() {
  $node_types = db_query('SELECT * FROM {node_type}')->fetchAllAssoc('type', PDO::FETCH_OBJ);

  // Create default settings for orphan nodes.
  $all_types = db_query('SELECT DISTINCT type FROM {node}')->fetchCol();
  $extra_types = array_diff($all_types, array_keys($node_types));

  foreach ($extra_types as $type) {
    $type_object = new stdClass();
    $type_object->type = $type;

    // In Drupal 6, whether you have a body field or not is a flag in the node
    // type table. If it's enabled, nodes may or may not have an empty string
    // for the bodies. As we can't detect what this setting should be in
    // Drupal 7 without access to the Drupal 6 node type settings, we assume
    // the default, which is to enable the body field.
    $type_object->has_body = 1;
    $type_object->body_label = 'Body';
    $node_types[$type_object->type] = $type_object;
  }
  return $node_types;
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
