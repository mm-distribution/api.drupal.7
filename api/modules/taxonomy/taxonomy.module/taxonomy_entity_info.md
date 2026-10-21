# taxonomy_entity_info()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 91–140 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L91-L140)
- **Module/theme:** taxonomy
- **Implements:** [hook_entity_info()](../../system/system.api.php/hook_entity_info.md)

## Signature

```php
function taxonomy_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function taxonomy_entity_info() {
  $return = array(
    'taxonomy_term' => array(
      'label' => t('Taxonomy term'),
      'controller class' => 'TaxonomyTermController',
      'base table' => 'taxonomy_term_data',
      'uri callback' => 'taxonomy_term_uri',
      'fieldable' => TRUE,
      'entity keys' => array(
        'id' => 'tid',
        'bundle' => 'vocabulary_machine_name',
        'label' => 'name',
      ),
      'bundle keys' => array(
        'bundle' => 'machine_name',
      ),
      'bundles' => array(),
      'view modes' => array(
        // @todo View mode for display as a field (when attached to nodes etc).
        'full' => array(
          'label' => t('Taxonomy term page'),
          'custom settings' => FALSE,
        ),
      ),
    ),
  );
  foreach (taxonomy_vocabulary_get_names() as $machine_name => $vocabulary) {
    $return['taxonomy_term']['bundles'][$machine_name] = array(
      'label' => $vocabulary->name,
      'admin' => array(
        'path' => 'admin/structure/taxonomy/%taxonomy_vocabulary_machine_name',
        'real path' => 'admin/structure/taxonomy/' . $machine_name,
        'bundle argument' => 3,
        'access arguments' => array('administer taxonomy'),
      ),
    );
  }
  $return['taxonomy_vocabulary'] = array(
    'label' => t('Taxonomy vocabulary'),
    'controller class' => 'TaxonomyVocabularyController',
    'base table' => 'taxonomy_vocabulary',
    'entity keys' => array(
      'id' => 'vid',
      'label' => 'name',
    ),
    'fieldable' => FALSE,
  );

  return $return;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
