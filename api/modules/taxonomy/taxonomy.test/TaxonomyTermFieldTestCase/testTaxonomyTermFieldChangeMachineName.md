# TaxonomyTermFieldTestCase::testTaxonomyTermFieldChangeMachineName()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1651–1686 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1651-L1686)
- **Class:** [TaxonomyTermFieldTestCase](../TaxonomyTermFieldTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermFieldChangeMachineName()
```

## Documentation

```text
Tests that vocabulary machine name changes are mirrored in field definitions.
```

## Code

```php
  function testTaxonomyTermFieldChangeMachineName() {
    // Add several entries in the 'allowed_values' setting, to make sure that
    // they all get updated.
    $this->field['settings']['allowed_values'] = array(
      array(
        'vocabulary' => $this->vocabulary->machine_name,
        'parent' => '0',
      ),
      array(
        'vocabulary' => $this->vocabulary->machine_name,
        'parent' => '0',
      ),
      array(
        'vocabulary' => 'foo',
        'parent' => '0',
      ),
    );
    field_update_field($this->field);
    // Change the machine name.
    $old_name = $this->vocabulary->machine_name;
    $new_name = drupal_strtolower($this->randomName());
    $this->vocabulary->machine_name = $new_name;
    taxonomy_vocabulary_save($this->vocabulary);

    // Check that entity bundles are properly updated.
    $info = entity_get_info('taxonomy_term');
    $this->assertFalse(isset($info['bundles'][$old_name]), 'The old bundle name does not appear in entity_get_info().');
    $this->assertTrue(isset($info['bundles'][$new_name]), 'The new bundle name appears in entity_get_info().');

    // Check that the field instance is still attached to the vocabulary.
    $field = field_info_field($this->field_name);
    $allowed_values = $field['settings']['allowed_values'];
    $this->assertEqual($allowed_values[0]['vocabulary'], $new_name, 'Index 0: Machine name was updated correctly.');
    $this->assertEqual($allowed_values[1]['vocabulary'], $new_name, 'Index 1: Machine name was updated correctly.');
    $this->assertEqual($allowed_values[2]['vocabulary'], 'foo', 'Index 2: Machine name was left untouched.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
