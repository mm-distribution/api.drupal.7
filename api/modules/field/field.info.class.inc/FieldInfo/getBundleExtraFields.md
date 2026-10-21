# FieldInfo::getBundleExtraFields()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 451–482 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L451-L482)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function getBundleExtraFields($entity_type, $bundle)
```

## Documentation

```text
Retrieves the "extra fields" for a bundle.

@param $entity_type
  The entity type.
@param $bundle
  The bundle name.

@return
  The array of extra fields.
```

## Code

```php
  public function getBundleExtraFields($entity_type, $bundle) {
    // Read from the "static" cache.
    if (isset($this->bundleExtraFields[$entity_type][$bundle])) {
      return $this->bundleExtraFields[$entity_type][$bundle];
    }

    // Read from the persistent cache.
    if ($cached = cache_get("field_info:bundle_extra:$entity_type:$bundle", 'cache_field')) {
      $this->bundleExtraFields[$entity_type][$bundle] = $cached->data;
      return $this->bundleExtraFields[$entity_type][$bundle];
    }

    // Cache miss: read from hook_field_extra_fields(). Note: given the current
    // shape of the hook, we have no other way than collecting extra fields on
    // all bundles.
    $info = array();
    $extra = module_invoke_all('field_extra_fields');
    drupal_alter('field_extra_fields', $extra);
    // Merge in saved settings.
    if (isset($extra[$entity_type][$bundle])) {
      $info = $this->prepareExtraFields($extra[$entity_type][$bundle], $entity_type, $bundle);
    }

    // Store in the 'static' and persistent caches.
    $this->bundleExtraFields[$entity_type][$bundle] = $info;
    if (lock_acquire("field_info:bundle_extra:$entity_type:$bundle")) {
      cache_set("field_info:bundle_extra:$entity_type:$bundle", $info, 'cache_field');
      lock_release("field_info:bundle_extra:$entity_type:$bundle");
    }

    return $this->bundleExtraFields[$entity_type][$bundle];
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
