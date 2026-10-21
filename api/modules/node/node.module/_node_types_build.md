# _node_types_build()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 706–779 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L706-L779)
- **Module/theme:** node

## Signature

```php
function _node_types_build($rebuild = FALSE)
```

## Documentation

```text
Builds and returns the list of available node types.

The list of types is built by invoking hook_node_info() on all modules and
comparing this information with the node types in the {node_type} table.
These two information sources are not synchronized during module installation
until node_types_rebuild() is called.

@param $rebuild
 TRUE to rebuild node types. Equivalent to calling node_types_rebuild().

@return
  An object with two properties:
  - names: Associative array of the names of node types, keyed by the type.
  - types: Associative array of node type objects, keyed by the type.
  Both of these arrays will include new types that have been defined by
  hook_node_info() implementations but not yet saved in the {node_type}
  table. These are indicated in the type object by $type->is_new being set
  to the value 1. These arrays will also include obsolete types: types that
  were previously defined by modules that have now been disabled, or for
  whatever reason are no longer being defined in hook_node_info()
  implementations, but are still in the database. These are indicated in the
  type object by $type->disabled being set to TRUE.
```

## Code

```php
function _node_types_build($rebuild = FALSE) {
  $cid = 'node_types:' . $GLOBALS['language']->language;

  if (!$rebuild) {
    $_node_types = &drupal_static(__FUNCTION__);
    if (isset($_node_types)) {
      return $_node_types;
    }
    if ($cache = cache_get($cid)) {
      $_node_types = $cache->data;
      return $_node_types;
    }
  }

  $_node_types = (object) array('types' => array(), 'names' => array());

  foreach (module_implements('node_info') as $module) {
    $info_array = module_invoke($module, 'node_info');
    foreach ($info_array as $type => $info) {
      $info['type'] = $type;
      $_node_types->types[$type] = node_type_set_defaults($info);
      $_node_types->types[$type]->module = $module;
      $_node_types->names[$type] = $info['name'];
    }
  }
  $query = db_select('node_type', 'nt')
    ->addTag('translatable')
    ->addTag('node_type_access')
    ->fields('nt')
    ->orderBy('nt.type', 'ASC');
  if (!$rebuild) {
    $query->condition('disabled', 0);
  }
  foreach ($query->execute() as $type_object) {
    $type_db = $type_object->type;
    // Original disabled value.
    $disabled = $type_object->disabled;
    // Check for node types from disabled modules and mark their types for removal.
    // Types defined by the node module in the database (rather than by a separate
    // module using hook_node_info) have a base value of 'node_content'. The isset()
    // check prevents errors on old (pre-Drupal 7) databases.
    if (isset($type_object->base) && $type_object->base != 'node_content' && empty($_node_types->types[$type_db])) {
      $type_object->disabled = TRUE;
    }
    if (isset($_node_types->types[$type_db])) {
      $type_object->disabled = FALSE;
    }
    if (!isset($_node_types->types[$type_db]) || $type_object->modified) {
      $_node_types->types[$type_db] = $type_object;
      $_node_types->names[$type_db] = $type_object->name;

      if ($type_db != $type_object->orig_type) {
        unset($_node_types->types[$type_object->orig_type]);
        unset($_node_types->names[$type_object->orig_type]);
      }
    }
    $_node_types->types[$type_db]->disabled = $type_object->disabled;
    $_node_types->types[$type_db]->disabled_changed = $disabled != $type_object->disabled;
  }

  if ($rebuild) {
    foreach ($_node_types->types as $type => $type_object) {
      if (!empty($type_object->is_new) || !empty($type_object->disabled_changed)) {
        node_type_save($type_object);
      }
    }
  }

  asort($_node_types->names);

  cache_set($cid, $_node_types);

  return $_node_types;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
