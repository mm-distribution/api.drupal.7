# entity_get_info()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8023–8092 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8023-L8092)

## Signature

```php
function entity_get_info($entity_type = NULL)
```

## Documentation

```text
Get the entity info array of an entity type.

@param $entity_type
  The entity type, e.g. node, for which the info shall be returned, or NULL
  to return an array with info about all types.

@see hook_entity_info()
@see hook_entity_info_alter()
```

## Code

```php
function entity_get_info($entity_type = NULL) {
  global $language;

  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['entity_info'] = &drupal_static(__FUNCTION__);
  }
  $entity_info = &$drupal_static_fast['entity_info'];

  // hook_entity_info() includes translated strings, so each language is cached
  // separately.
  $langcode = $language->language;

  if (empty($entity_info)) {
    if ($cache = cache_get("entity_info:$langcode")) {
      $entity_info = $cache->data;
    }
    else {
      $entity_info = module_invoke_all('entity_info');
      // Merge in default values.
      foreach ($entity_info as $name => $data) {
        $entity_info[$name] += array(
          'fieldable' => FALSE,
          'controller class' => 'DrupalDefaultEntityController',
          'static cache' => TRUE,
          'field cache' => TRUE,
          'load hook' => $name . '_load',
          'bundles' => array(),
          'view modes' => array(),
          'entity keys' => array(),
          'translation' => array(),
        );
        $entity_info[$name]['entity keys'] += array(
          'revision' => '',
          'bundle' => '',
        );
        foreach ($entity_info[$name]['view modes'] as $view_mode => $view_mode_info) {
          $entity_info[$name]['view modes'][$view_mode] += array(
            'custom settings' => FALSE,
          );
        }
        // If no bundle key is provided, assume a single bundle, named after
        // the entity type.
        if (empty($entity_info[$name]['entity keys']['bundle']) && empty($entity_info[$name]['bundles'])) {
          $entity_info[$name]['bundles'] = array($name => array('label' => $entity_info[$name]['label']));
        }
        // Prepare entity schema fields SQL info for
        // DrupalEntityControllerInterface::buildQuery().
        if (isset($entity_info[$name]['base table'])) {
          $entity_info[$name]['base table field types'] = drupal_schema_field_types($entity_info[$name]['base table']);
          $entity_info[$name]['schema_fields_sql']['base table'] = drupal_schema_fields_sql($entity_info[$name]['base table']);
          if (isset($entity_info[$name]['revision table'])) {
            $entity_info[$name]['schema_fields_sql']['revision table'] = drupal_schema_fields_sql($entity_info[$name]['revision table']);
          }
        }
      }
      // Let other modules alter the entity info.
      drupal_alter('entity_info', $entity_info);
      cache_set("entity_info:$langcode", $entity_info);
    }
  }

  if (empty($entity_type)) {
    return $entity_info;
  }
  elseif (isset($entity_info[$entity_type])) {
    return $entity_info[$entity_type];
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
