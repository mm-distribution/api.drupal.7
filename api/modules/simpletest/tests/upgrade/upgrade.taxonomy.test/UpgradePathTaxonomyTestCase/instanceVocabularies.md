# UpgradePathTaxonomyTestCase::instanceVocabularies()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.taxonomy.test`](../_file.md), lines 28–43 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test#L28-L43)
- **Class:** [UpgradePathTaxonomyTestCase](../UpgradePathTaxonomyTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function instanceVocabularies($entity_type, $bundle)
```

## Documentation

```text
Retrieve an array mapping allowed vocabulary id to field name for
all taxonomy_term_reference fields for which an instance exists
for the specified entity type and bundle.
```

## Code

```php
  function instanceVocabularies($entity_type, $bundle) {
    $instances = array();
    foreach (field_info_instances($entity_type, $bundle) as $instance) {
      $field = field_info_field($instance['field_name']);
      if ($field['type'] == 'taxonomy_term_reference') {
        foreach ($field['settings']['allowed_values'] as $tree) {
          // Prefer valid taxonomy term reference fields for a given vocabulary
          // when they exist.
          if (empty($instances[$tree['vocabulary']]) || $instances[$tree['vocabulary']] == 'taxonomyextra') {
            $instances[$tree['vocabulary']] = $field['field_name'];
          }
        }
      }
    }
    return $instances;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
