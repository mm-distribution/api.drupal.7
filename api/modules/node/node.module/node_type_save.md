# node_type_save()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 526–574 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L526-L574)
- **Module/theme:** node

## Signature

```php
function node_type_save($info)
```

## Documentation

```text
Saves a node type to the database.

@param object $info
  The node type to save; an object with the following properties:
  - type: A string giving the machine name of the node type.
  - name: A string giving the human-readable name of the node type.
  - base: A string that indicates the base string for hook functions. For
    example, 'node_content' is the value used by the UI when creating a new
    node type.
  - description: A string that describes the node type.
  - help: A string giving the help information shown to the user when
    creating a node of this type.
  - custom: TRUE or FALSE indicating whether this type is defined by a module
    (FALSE) or by a user (TRUE) via Add Content Type.
  - modified: TRUE or FALSE indicating whether this type has been modified by
    an administrator. When modifying an existing node type, set to TRUE, or
    the change will be ignored on node_types_rebuild().
  - locked: TRUE or FALSE indicating whether the administrator can change the
    machine name of this type.
  - disabled: TRUE or FALSE indicating whether this type has been disabled.
  - has_title: TRUE or FALSE indicating whether this type uses the node title
    field.
  - title_label: A string containing the label for the title.
  - module: A string giving the module defining this type of node.
  - orig_type: A string giving the original machine-readable name of this
    node type. This may be different from the current type name if the
    'locked' key is FALSE.

@return int
  A status flag indicating the outcome of the operation, either SAVED_NEW or
  SAVED_UPDATED.
```

## Code

```php
function node_type_save($info) {
  $existing_type = !empty($info->old_type) ? $info->old_type : $info->type;
  $is_existing = (bool) db_query_range('SELECT 1 FROM {node_type} WHERE type = :type', 0, 1, array(':type' => $existing_type))->fetchField();
  $type = node_type_set_defaults($info);

  $fields = array(
    'type' => (string) $type->type,
    'name' => (string) $type->name,
    'base' => (string) $type->base,
    'has_title' => (int) $type->has_title,
    'title_label' => (string) $type->title_label,
    'description' => (string) $type->description,
    'help' => (string) $type->help,
    'custom' => (int) $type->custom,
    'modified' => (int) $type->modified,
    'locked' => (int) $type->locked,
    'disabled' => (int) $type->disabled,
    'module' => $type->module,
  );

  if ($is_existing) {
    db_update('node_type')
      ->fields($fields)
      ->condition('type', $existing_type)
      ->execute();

    if (!empty($type->old_type) && $type->old_type != $type->type) {
      field_attach_rename_bundle('node', $type->old_type, $type->type);
    }
    module_invoke_all('node_type_update', $type);
    $status = SAVED_UPDATED;
  }
  else {
    $fields['orig_type'] = (string) $type->orig_type;
    db_insert('node_type')
      ->fields($fields)
      ->execute();

    field_attach_create_bundle('node', $type->type);

    module_invoke_all('node_type_insert', $type);
    $status = SAVED_NEW;
  }

  // Clear the node type cache.
  node_type_cache_reset();

  return $status;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
