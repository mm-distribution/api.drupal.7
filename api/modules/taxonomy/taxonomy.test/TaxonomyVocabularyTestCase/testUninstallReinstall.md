# TaxonomyVocabularyTestCase::testUninstallReinstall()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 377–405 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L377-L405)
- **Class:** [TaxonomyVocabularyTestCase](../TaxonomyVocabularyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testUninstallReinstall()
```

## Documentation

```text
Test uninstall and reinstall of the taxonomy module.
```

## Code

```php
  function testUninstallReinstall() {
    // Fields and field instances attached to taxonomy term bundles should be
    // removed when the module is uninstalled.
    $this->field_name = drupal_strtolower($this->randomName() . '_field_name');
    $this->field = array('field_name' => $this->field_name, 'type' => 'text', 'cardinality' => 4);
    $this->field = field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'taxonomy_term',
      'bundle' => $this->vocabulary->machine_name,
      'label' => $this->randomName() . '_label',
    );
    field_create_instance($this->instance);

    module_disable(array('taxonomy'));
    require_once DRUPAL_ROOT . '/includes/install.inc';
    drupal_uninstall_modules(array('taxonomy'));
    module_enable(array('taxonomy'));

    // Now create a vocabulary with the same name. All field instances
    // connected to this vocabulary name should have been removed when the
    // module was uninstalled. Creating a new field with the same name and
    // an instance of this field on the same bundle name should be successful.
    unset($this->vocabulary->vid);
    taxonomy_vocabulary_save($this->vocabulary);
    unset($this->field['id']);
    field_create_field($this->field);
    field_create_instance($this->instance);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
