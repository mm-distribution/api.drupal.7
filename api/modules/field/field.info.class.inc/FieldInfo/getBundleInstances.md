# FieldInfo::getBundleInstances()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 350–438 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L350-L438)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getBundleInstances($entity_type, $bundle)
```

## Documentation

```text
Retrieves the instances for a bundle.

The function also populates the corresponding field definitions in the
"static" cache.

@param $entity_type
  The entity type.
@param $bundle
  The bundle name.

@return
  The array of instance definitions, keyed by field name.
```

## Code

```php
  public function getBundleInstances($entity_type, $bundle) {
    // Read from the "static" cache.
    if (isset($this->bundleInstances[$entity_type][$bundle])) {
      return $this->bundleInstances[$entity_type][$bundle];
    }
    if (isset($this->emptyBundles[$entity_type][$bundle])) {
      return array();
    }

    // Read from the persistent cache.
    if ($cached = cache_get("field_info:bundle:$entity_type:$bundle", 'cache_field')) {
      $info = $cached->data;

      // Extract the field definitions and save them in the "static" cache.
      foreach ($info['fields'] as $field) {
        if (!isset($this->fieldsById[$field['id']])) {
          $this->fieldsById[$field['id']] = $field;
          if (!$field['deleted']) {
            $this->fieldIdsByName[$field['field_name']] = $field['id'];
          }
        }
      }
      unset($info['fields']);

      // Store the instance definitions in the "static" cache'. Empty (or
      // non-existent) bundles are stored separately, so that they do not
      // pollute the global list returned by getInstances().
      if ($info['instances']) {
        $this->bundleInstances[$entity_type][$bundle] = $info['instances'];
      }
      else {
        $this->emptyBundles[$entity_type][$bundle] = TRUE;
      }

      return $info['instances'];
    }

    // Cache miss: collect from the definitions.

    $instances = array();

    // Collect the fields in the bundle.
    $params = array('entity_type' => $entity_type, 'bundle' => $bundle);
    $fields = field_read_fields($params);

    // This iterates on non-deleted instances, so deleted fields are kept out of
    // the persistent caches.
    foreach (field_read_instances($params) as $instance) {
      $field = $fields[$instance['field_name']];

      $instance = $this->prepareInstance($instance, $field['type']);
      $instances[$field['field_name']] = $instance;

      // If the field is not in our global "static" list yet, add it.
      if (!isset($this->fieldsById[$field['id']])) {
        $field = $this->prepareField($field);

        $this->fieldsById[$field['id']] = $field;
        $this->fieldIdsByName[$field['field_name']] = $field['id'];
      }
    }

    // Store in the 'static' cache'. Empty (or non-existent) bundles are stored
    // separately, so that they do not pollute the global list returned by
    // getInstances().
    if ($instances) {
      $this->bundleInstances[$entity_type][$bundle] = $instances;
    }
    else {
      $this->emptyBundles[$entity_type][$bundle] = TRUE;
    }

    // The persistent cache additionally contains the definitions of the fields
    // involved in the bundle.
    $cache = array(
      'instances' => $instances,
      'fields' => array()
    );
    foreach ($instances as $instance) {
      $cache['fields'][] = $this->fieldsById[$instance['field_id']];
    }

    if (lock_acquire("field_info:bundle:$entity_type:$bundle")) {
      cache_set("field_info:bundle:$entity_type:$bundle", $cache, 'cache_field');
      lock_release("field_info:bundle:$entity_type:$bundle");
    }

    return $instances;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
