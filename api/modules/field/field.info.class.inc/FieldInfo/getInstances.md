# FieldInfo::getInstances()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 209–255 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L209-L255)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getInstances($entity_type = NULL)
```

## Documentation

```text
Retrieves all active, non-deleted instances definitions.

@param $entity_type
  (optional) The entity type.

@return
  If $entity_type is not set, all instances keyed by entity type and bundle
  name. If $entity_type is set, all instances for that entity type, keyed
  by bundle name.
```

## Code

```php
  public function getInstances($entity_type = NULL) {
    // If the full list is not present in "static" cache yet.
    if (!$this->loadedAllInstances) {

      // Read from persistent cache.
      if ($cached = cache_get('field_info:instances', 'cache_field')) {
        $this->bundleInstances = $cached->data;
      }
      else {
        // Collect and prepare instances.

        // We also need to populate the static field cache, since it will not
        // be set by subsequent getBundleInstances() calls.
        $this->getFields();

        // Initialize empty arrays for all existing entity types and bundles.
        // This is not strictly needed, but is done to preserve the behavior of
        // field_info_instances() before http://drupal.org/node/1915646.
        foreach (field_info_bundles() as $existing_entity_type => $bundles) {
          foreach ($bundles as $bundle => $bundle_info) {
            $this->bundleInstances[$existing_entity_type][$bundle] = array();
          }
        }

        foreach (field_read_instances() as $instance) {
          $field = $this->getField($instance['field_name']);
          $instance = $this->prepareInstance($instance, $field['type']);
          $this->bundleInstances[$instance['entity_type']][$instance['bundle']][$instance['field_name']] = $instance;
        }

        // Store in persistent cache.
        if (lock_acquire('field_info:instances')) {
          cache_set('field_info:instances', $this->bundleInstances, 'cache_field');
          lock_release('field_info:instances');
        }
      }

      $this->loadedAllInstances = TRUE;
    }

    if (isset($entity_type)) {
      return isset($this->bundleInstances[$entity_type]) ? $this->bundleInstances[$entity_type] : array();
    }
    else {
      return $this->bundleInstances;
    }
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
