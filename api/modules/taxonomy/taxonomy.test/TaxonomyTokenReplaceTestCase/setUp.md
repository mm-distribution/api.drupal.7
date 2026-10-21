# TaxonomyTokenReplaceTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1853–1889 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1853-L1889)
- **Class:** [TaxonomyTokenReplaceTestCase](../TaxonomyTokenReplaceTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    $this->admin_user = $this->drupalCreateUser(array('administer taxonomy', 'bypass node access'));
    $this->drupalLogin($this->admin_user);
    $this->vocabulary = $this->createVocabulary();
    $this->langcode = LANGUAGE_NONE;

    $field = array(
      'field_name' => 'taxonomy_' . $this->vocabulary->machine_name,
      'type' => 'taxonomy_term_reference',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $this->vocabulary->machine_name,
            'parent' => 0,
          ),
        ),
      ),
    );
    field_create_field($field);

    $this->instance = array(
      'field_name' => 'taxonomy_' . $this->vocabulary->machine_name,
      'bundle' => 'article',
      'entity_type' => 'node',
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
        ),
      ),
    );
    field_create_instance($this->instance);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
