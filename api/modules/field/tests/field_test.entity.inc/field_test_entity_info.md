# field_test_entity_info()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 11–127 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L11-L127)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_entity_info()](../../../system/system.api.php/hook_entity_info.md)

## Signature

```php
function field_test_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function field_test_entity_info() {
  // If requested, clear the field cache while this hook is being called. See
  // testFieldInfoCache().
  if (variable_get('field_test_clear_info_cache_in_hook_entity_info', FALSE)) {
    field_info_cache_clear();
  }

  $bundles = variable_get('field_test_bundles', array('test_bundle' => array('label' => 'Test Bundle')));
  $test_entity_modes = array(
    'full' => array(
      'label' => t('Full object'),
      'custom settings' => TRUE,
    ),
    'teaser' => array(
      'label' => t('Teaser'),
      'custom settings' => TRUE,
    ),
  );

  return array(
    'test_entity' => array(
      'label' => t('Test Entity'),
      'fieldable' => TRUE,
      'field cache' => FALSE,
      'base table' => 'test_entity',
      'revision table' => 'test_entity_revision',
      'entity keys' => array(
        'id' => 'ftid',
        'revision' => 'ftvid',
        'bundle' => 'fttype',
      ),
      'bundles' => $bundles,
      'view modes' => $test_entity_modes,
    ),
    // This entity type doesn't get form handling for now...
    'test_cacheable_entity' => array(
      'label' => t('Test Entity, cacheable'),
      'fieldable' => TRUE,
      'field cache' => TRUE,
      'entity keys' => array(
        'id' => 'ftid',
        'revision' => 'ftvid',
        'bundle' => 'fttype',
      ),
      'bundles' => $bundles,
      'view modes' => $test_entity_modes,
    ),
    'test_entity_bundle_key' => array(
      'label' => t('Test Entity with a bundle key.'),
      'base table' => 'test_entity_bundle_key',
      'fieldable' => TRUE,
      'field cache' => FALSE,
      'entity keys' => array(
        'id' => 'ftid',
        'bundle' => 'fttype',
      ),
      'bundles' => array('bundle1' => array('label' => 'Bundle1'), 'bundle2' => array('label' => 'Bundle2')) + $bundles,
      'view modes' => $test_entity_modes,
    ),
    // In this case, the bundle key is not stored in the database.
    'test_entity_bundle' => array(
      'label' => t('Test Entity with a specified bundle.'),
      'base table' => 'test_entity_bundle',
      'fieldable' => TRUE,
      'controller class' => 'TestEntityBundleController',
      'field cache' => FALSE,
      'entity keys' => array(
        'id' => 'ftid',
        'bundle' => 'fttype',
      ),
      'bundles' => array('test_entity_2' => array('label' => 'Test entity 2')) + $bundles,
      'view modes' => $test_entity_modes,
    ),
    // @see EntityPropertiesTestCase::testEntityLabel()
    'test_entity_no_label' => array(
      'label' => t('Test entity without label'),
      'fieldable' => TRUE,
      'field cache' => FALSE,
      'base table' => 'test_entity',
      'entity keys' => array(
        'id' => 'ftid',
        'revision' => 'ftvid',
        'bundle' => 'fttype',
      ),
      'bundles' => $bundles,
      'view modes' => $test_entity_modes,
    ),
    'test_entity_label' => array(
      'label' => t('Test entity label'),
      'fieldable' => TRUE,
      'field cache' => FALSE,
      'base table' => 'test_entity',
      'entity keys' => array(
        'id' => 'ftid',
        'revision' => 'ftvid',
        'bundle' => 'fttype',
        'label' => 'ftlabel',
      ),
      'bundles' => $bundles,
      'view modes' => $test_entity_modes,
    ),
    'test_entity_label_callback' => array(
      'label' => t('Test entity label callback'),
      'fieldable' => TRUE,
      'field cache' => FALSE,
      'base table' => 'test_entity',
      'label callback' => 'field_test_entity_label_callback',
      'entity keys' => array(
        'id' => 'ftid',
        'revision' => 'ftvid',
        'bundle' => 'fttype',
      ),
      'bundles' => $bundles,
      'view modes' => $test_entity_modes,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
