# _field_info_collate_types()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 141–235 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L141-L235)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function _field_info_collate_types($reset = FALSE)
```

## Documentation

```text
Collates all information on field types, widget types and related structures.

@param $reset
  If TRUE, clear the cache. The information will be rebuilt from the database
  next time it is needed. Defaults to FALSE.

@return
  If $reset is TRUE, nothing.
  If $reset is FALSE, an array containing the following elements:
  - 'field types': Array of hook_field_info() results, keyed by field_type.
    Each element has the following components: label, description, settings,
    instance_settings, default_widget, default_formatter, and behaviors
    from hook_field_info(), as well as module, giving the module that exposes
    the field type.
  - 'widget types': Array of hook_field_widget_info() results, keyed by
    widget_type. Each element has the following components: label, field
    types, settings, weight, and behaviors from hook_field_widget_info(),
    as well as module, giving the module that exposes the widget type.
  - 'formatter types': Array of hook_field_formatter_info() results, keyed by
    formatter_type. Each element has the following components: label, field
    types, and behaviors from hook_field_formatter_info(), as well as
    module, giving the module that exposes the formatter type.
  - 'storage types': Array of hook_field_storage_info() results, keyed by
    storage type names. Each element has the following components: label,
    description, and settings from hook_field_storage_info(), as well as
    module, giving the module that exposes the storage type.
  - 'fieldable types': Array of hook_entity_info() results, keyed by
    entity_type. Each element has the following components: name, id key,
    revision key, bundle key, cacheable, and bundles from hook_entity_info(),
    as well as module, giving the module that exposes the entity type.
```

## Code

```php
function _field_info_collate_types($reset = FALSE) {
  global $language;
  static $info;

  // The _info() hooks invoked below include translated strings, so each
  // language is cached separately.
  $langcode = $language->language;

  if ($reset) {
    $info = NULL;
    // Clear all languages.
    cache_clear_all('field_info_types:', 'cache_field', TRUE);
    return;
  }

  if (!isset($info)) {
    if ($cached = cache_get("field_info_types:$langcode", 'cache_field')) {
      $info = $cached->data;
    }
    else {
      $info = array(
        'field types' => array(),
        'widget types' => array(),
        'formatter types' => array(),
        'storage types' => array(),
      );

      // Populate field types.
      foreach (module_implements('field_info') as $module) {
        $field_types = (array) module_invoke($module, 'field_info');
        foreach ($field_types as $name => $field_info) {
          // Provide defaults.
          $field_info += array(
            'settings' => array(),
            'instance_settings' => array(),
          );
          $info['field types'][$name] = $field_info;
          $info['field types'][$name]['module'] = $module;
        }
      }
      drupal_alter('field_info', $info['field types']);

      // Populate widget types.
      foreach (module_implements('field_widget_info') as $module) {
        $widget_types = (array) module_invoke($module, 'field_widget_info');
        foreach ($widget_types as $name => $widget_info) {
          // Provide defaults.
          $widget_info += array(
            'settings' => array(),
          );
          $info['widget types'][$name] = $widget_info;
          $info['widget types'][$name]['module'] = $module;
        }
      }
      drupal_alter('field_widget_info', $info['widget types']);
      uasort($info['widget types'], 'drupal_sort_weight');

      // Populate formatter types.
      foreach (module_implements('field_formatter_info') as $module) {
        $formatter_types = (array) module_invoke($module, 'field_formatter_info');
        foreach ($formatter_types as $name => $formatter_info) {
          // Provide defaults.
          $formatter_info += array(
            'settings' => array(),
          );
          $info['formatter types'][$name] = $formatter_info;
          $info['formatter types'][$name]['module'] = $module;
        }
      }
      drupal_alter('field_formatter_info', $info['formatter types']);

      // Populate storage types.
      foreach (module_implements('field_storage_info') as $module) {
        $storage_types = (array) module_invoke($module, 'field_storage_info');
        foreach ($storage_types as $name => $storage_info) {
          // Provide defaults.
          $storage_info += array(
            'settings' => array(),
          );
          $info['storage types'][$name] = $storage_info;
          $info['storage types'][$name]['module'] = $module;
        }
      }
      drupal_alter('field_storage_info', $info['storage types']);

      // Set the cache if we can acquire a lock.
      if (lock_acquire("field_info_types:$langcode")) {
        cache_set("field_info_types:$langcode", $info, 'cache_field');
        lock_release("field_info_types:$langcode");
      }
    }
  }

  return $info;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
