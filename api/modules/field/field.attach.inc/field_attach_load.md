# field_attach_load()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 622–734 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L622-L734)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_load($entity_type, $entities, $age = FIELD_LOAD_CURRENT, $options = array())
```

## Documentation

```text
Loads fields for the current revisions of a group of entities.

Loads all fields for each entity object in a group of a single entity type.
The loaded field values are added directly to the entity objects.

field_attach_load() is automatically called by the default entity controller
class, and thus, in most cases, doesn't need to be explicitly called by the
entity type module.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entities
  An array of entities for which to load fields, keyed by entity ID.
  Each entity needs to have its 'bundle', 'id' and (if applicable)
  'revision' keys filled in. The function adds the loaded field data
  directly in the entity objects of the $entities array.
@param $age
  FIELD_LOAD_CURRENT to load the most recent revision for all
  fields, or FIELD_LOAD_REVISION to load the version indicated by
  each entity. Defaults to FIELD_LOAD_CURRENT; use
  field_attach_load_revision() instead of passing FIELD_LOAD_REVISION.
@param $options
  An associative array of additional options, with the following keys:
  - 'field_id': The field ID that should be loaded, instead of
    loading all fields, for each entity. Note that returned entities
    may contain data for other fields, for example if they are read
    from a cache.
  - 'deleted': If TRUE, the function will operate on deleted fields
    as well as non-deleted fields. If unset or FALSE, only
    non-deleted fields are operated on.
```

## Code

```php
function field_attach_load($entity_type, $entities, $age = FIELD_LOAD_CURRENT, $options = array()) {
  $load_current = $age == FIELD_LOAD_CURRENT;

  // Merge default options.
  $default_options = array(
    'deleted' => FALSE,
  );
  $options += $default_options;

  $info = entity_get_info($entity_type);
  // Only the most current revision of non-deleted fields for cacheable entity
  // types can be cached.
  $cache_read = $load_current && $info['field cache'] && empty($options['deleted']);
  // In addition, do not write to the cache when loading a single field.
  $cache_write = $cache_read && !isset($options['field_id']);

  if (empty($entities)) {
    return;
  }

  // Assume all entities will need to be queried. Entities found in the cache
  // will be removed from the list.
  $queried_entities = $entities;

  // Fetch available entities from cache, if applicable.
  if ($cache_read) {
    // Build the list of cache entries to retrieve.
    $cids = array();
    foreach ($entities as $id => $entity) {
      $cids[] = "field:$entity_type:$id";
    }
    $cache = cache_get_multiple($cids, 'cache_field');
    // Put the cached field values back into the entities and remove them from
    // the list of entities to query.
    foreach ($entities as $id => $entity) {
      $cid = "field:$entity_type:$id";
      if (isset($cache[$cid])) {
        unset($queried_entities[$id]);
        foreach ($cache[$cid]->data as $field_name => $values) {
          $entity->$field_name = $values;
        }
      }
    }
  }

  // Fetch other entities from their storage location.
  if ($queried_entities) {
    // The invoke order is:
    // - hook_field_storage_pre_load()
    // - storage backend's hook_field_storage_load()
    // - field-type module's hook_field_load()
    // - hook_field_attach_load()

    // Invoke hook_field_storage_pre_load(): let any module load field
    // data before the storage engine, accumulating along the way.
    $skip_fields = array();
    foreach (module_implements('field_storage_pre_load') as $module) {
      $function = $module . '_field_storage_pre_load';
      $function($entity_type, $queried_entities, $age, $skip_fields, $options);
    }

    $instances = array();

    // Collect the storage backends used by the remaining fields in the entities.
    $storages = array();
    foreach ($queried_entities as $entity) {
      list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
      $instances = _field_invoke_get_instances($entity_type, $bundle, $options);

      foreach ($instances as $instance) {
        $field_name = $instance['field_name'];
        $field_id = $instance['field_id'];
        // Make sure all fields are present at least as empty arrays.
        if (!isset($queried_entities[$id]->{$field_name})) {
          $queried_entities[$id]->{$field_name} = array();
        }
        // Collect the storage backend if the field has not been loaded yet.
        if (!isset($skip_fields[$field_id])) {
          $field = field_info_field_by_id($field_id);
          $storages[$field['storage']['type']][$field_id][] = $load_current ? $id : $vid;
        }
      }
    }

    // Invoke hook_field_storage_load() on the relevant storage backends.
    foreach ($storages as $storage => $fields) {
      $storage_info = field_info_storage_types($storage);
      module_invoke($storage_info['module'], 'field_storage_load', $entity_type, $queried_entities, $age, $fields, $options);
    }

    // Invoke field-type module's hook_field_load().
    $null = NULL;
    _field_invoke_multiple('load', $entity_type, $queried_entities, $age, $null, $options);

    // Invoke hook_field_attach_load(): let other modules act on loading the
    // entity.
    module_invoke_all('field_attach_load', $entity_type, $queried_entities, $age, $options);

    // Build cache data.
    if ($cache_write) {
      foreach ($queried_entities as $id => $entity) {
        $data = array();
        list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);
        $instances = field_info_instances($entity_type, $bundle);
        foreach ($instances as $instance) {
          $data[$instance['field_name']] = $queried_entities[$id]->{$instance['field_name']};
        }
        $cid = "field:$entity_type:$id";
        cache_set($cid, $data, 'cache_field');
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
